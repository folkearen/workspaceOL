public class Main {
    public static void main(String[] args) {
        System.out.println( suma(10,10,10));

        Coche miCoche = new Coche();
        miCoche.numeroPuertas(1);
        System.out.println(miCoche.puertas);
    }
    public static int suma(int a, int b, int c) {
        return a + b + c;
    }
}
class Coche {
    public int puertas = 0;
    public int numeroPuertas(int n){
        return this.puertas = n;
    }
}

//class Coche {
//    public int numeroDePuertas = 4;

//    public void sumarPuertas(){
//
//        this.numeroDePuertas++;
//    }
//}