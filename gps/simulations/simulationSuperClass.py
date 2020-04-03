class PowerSimulation:
    """
    abstract class, in where rand, historical, sim should be implemented
    """
    def __init__(self):
        self.active_power_in = None
        self.reactive_power_in = None
        self.active_power_out = None
        self.reactive_power_out = None

    def get_power(self):
        self.update()
        api = self.active_power_in
        rpi = self.reactive_power_in
        apo = self.active_power_out
        rpo = self.reactive_power_out
        return api, rpi, apo, rpo

    def update(self):
        """
        should be implemented by subclass
        """
        raise NotImplementedError