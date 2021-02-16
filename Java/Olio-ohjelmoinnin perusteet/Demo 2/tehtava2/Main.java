package tehtava2;

public class Main {
    public static void main(String[] args) {
        Jalkapallojoukkue tiimi = new Jalkapallojoukkue("Real Madrid.", "Estadio Santiago Bernabéu");
        System.out.println(tiimi);
        Jalkapallopelaaja.generoiPelaajat();
    }
}
