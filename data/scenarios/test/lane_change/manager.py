import numpy as np
from tpl.simulation.state import SimTrafficLight


class SimulationManager:

    def __init__(self, sim):

        sim.ego.v = np.random.uniform(5, 10)

        for c in sim.cars:
            c.x += np.random.uniform(-20, 20)
            c.v_target = np.random.uniform(5, 15)

    def update(self, sim):

        if sim.ego.x > -100.0:
            sim.finished = True
