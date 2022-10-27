class UberPool extends Car {
    String brand;
    String model;

    public UberPool(String license, Account driver, String brand, String model) {
        super(license, driver); //Super Hace referencia a los atributos y metodos de la clase padre
        this.brand = brand; //This Hace referenica a los emtodos y atributos de esta clase, hija
        this.model = model;
    }
    
}
