class Car {
    private Integer id;
    private String license;
    private Account driver;
    private Integer passenger; //Encapsulamiento

    public Car(String license, Account driver){
        this.license = license; //This representa a la variable global de la clase,
        //la variable a secas es la variable local llamada en el metodo construtor.
        this.driver = driver;
    }
    
    void printDatacar() {
        if(passenger != null) {

        
        System.out.println("License: " + license + " Driver: " + driver.name + " Passenger :" + passenger);
        }
    }

    public Integer getPassenger() {
        return passenger;
    }

    public void setPassenger(Integer passenger) {
        if(passenger == 4){
            this.passenger = passenger;
        }else {
            System.out.println("Necesitas asingar 4 pasajeros");
        }
    
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }

    public Account getDriver() {
        return driver;
    }

    public void setDriver(Account driver) {
        this.driver = driver;
    }
}
