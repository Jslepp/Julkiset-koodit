package tehtava1;

public class Main {
    public static void main(String[] args) {
        Laiva laiva1 = new Laiva("Titanic", 100, 20, 10);
        System.out.println(laiva1.nimi + ": " + Laiva.matkanLaskeminen(30));
    } 
}
