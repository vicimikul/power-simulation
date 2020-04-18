import time


class PowerSimulation:
    """
    abstract class, in where rand, historical, sim should be implemented
    """
    def __init__(self, battery, max_iter, delay):
        self.active_power_in = None
        self.reactive_power_in = None
        self.active_power_out = None
        self.reactive_power_out = None
        self.start_soc = None
        self.t = 0
        self.delay = delay
        self.max_iter = max_iter
        self.battery = battery
        self.graph = None

    def get_power(self):
        api = self.active_power_in
        rpi = self.reactive_power_in
        apo = self.active_power_out
        rpo = self.reactive_power_out
        self.update()
        return api, rpi, apo, rpo

    def update(self):
        """
        should be implemented by subclass
        """
        raise NotImplementedError

    def run(self):
        for i in range(0, self.max_iter):
            print(i)
            api, rpi, apo, rpo = self.get_power()
            self.battery.update(api, rpi, apo, rpo)
            self.graph.api.append(api)
            self.graph.t.append(i)
            self.graph.apo.append(apo)
            time.sleep(self.delay)


