from car import Car

class UberBlack(Car):
    typeAccepted    = []
    seatsMaterial   = []

    def __init__(self, license, driver, typeAccepted, seatsMaterial):
        super().__init__(license, driver)
        self.typeAccepted   = typeAccepted
        self.seatsMaterial  = seatsMaterial