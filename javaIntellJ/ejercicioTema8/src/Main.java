public class Main {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.setNombre("Alan");
        System.out.println(persona1.getNombre());
        persona1.setEdad(34);
        System.out.println(persona1.getEdad());
        persona1.setTelefono(973731003);
        System.out.println(persona1.getTelefono());

    }

}
class Persona {
    private String nombre;
    private int edad;
    private int telefono;

    public String getNombre() {
        return this.nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getEdad() {
        return this.edad;
    }
    public void setEdad(int edad) {
        this.edad = edad;
    }

    public int getTelefono() {
        return this.telefono;
    }
    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }



}
