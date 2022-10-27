import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car {
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatMaterial;
    protected Integer passenger;

    public UberVan(String license, Account driver, Map<String, Map<String,Integer>> typeCarAccepted, ArrayList<String>seatMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatMaterial = seatMaterial;
    }
    @Override //Sobre escribe == po,imorfismo
    public void setPassenger(Integer passenger) {
        // TODO Auto-generated method stub
        if(passenger == 6){
            this.passenger = passenger;
        }else {
            System.out.println("Necesitas asingar 6 pasajeros");
        }
    }  
}
