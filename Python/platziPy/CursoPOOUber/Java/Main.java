class Main {
    public static void main(String[] args) {
       Car car = new Car("AMQ123", new Account("Andres Herrera", "123"));
       car.setPassenger(3);
       car.printDatacar();

       //Car car2 = new Car("RTY303", new Account("Maritormez de Asturias", "456"));
       //car2.printDatacar();

    }
}