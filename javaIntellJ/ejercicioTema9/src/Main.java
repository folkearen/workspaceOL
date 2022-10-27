public class Main {
    public static void main(String[] args) {
        Cliente comprador = new Cliente();
        comprador.edad = 23;
        comprador.nombre = "Conral";
        comprador.telefono = 65423413;
        comprador.credito = 100;
        System.out.println("Hola "+ comprador.nombre + ", tenes  "+ comprador.edad + " años, su numero telefonico es " + comprador.telefono + " y sus credistos son " + comprador.credito);

        Trabajador recepcionista = new Trabajador();
        recepcionista.edad = 35;
        recepcionista.nombre = "Robert";
        recepcionista.telefono = 877667373;
        recepcionista.salario = 2000;
        System.out.println("Hola "+ recepcionista.nombre + ", tenes  "+ recepcionista.edad + " años, su numero telefonico es " + recepcionista.telefono + " y su salario es " + recepcionista.salario);
    }
}

class Persona {
    int edad;
    String nombre;
    int telefono;
}

class Cliente extends Persona {
    int credito;
}

class Trabajador extends Persona {
    int salario;
}