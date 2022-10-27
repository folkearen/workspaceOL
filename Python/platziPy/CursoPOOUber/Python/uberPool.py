from car import Car #Importo la clase padre

class UberPoll(Car): #Creo una nueva clase heradada de la lcase CAR (Car)
    brand   = str
    model   = str

    #Metodo Constructor
    def __init__(self, license, driver, brand, model):
        super().__init__(license, driver)
        self.brand = brand
        self.model = model