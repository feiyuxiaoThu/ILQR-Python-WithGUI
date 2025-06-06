import os
import imviz as viz
import numpy as np

from imdash.utils import DataSource, ColorEdit
from imdash.views.view_2d import View2DComponent

from tpl.gui.renderers import MapObjectsRenderer


class MapObjectsComponent(View2DComponent):

    DISPLAY_NAME = "Tpl/Map objects"

    def __init__(self):

        super().__init__()

        self.label = "map_objects"

        self.tpl_env = DataSource(path="{/structstores/tpl_env}")

        self.renderer = MapObjectsRenderer()

    def render(self, idx, view):

        viz.plot_dummy(label=f"{self.label}###{idx}", legend_color=(1.0, 1.0, 1.0))

        src = self.tpl_env.get_used_source()
        env = src.store
        with env.lock():
            maps_dict = {s: env.maps[s] for s in env.maps.__slots__}
            self.renderer.render_map_store(maps_dict, env.selected_map)
