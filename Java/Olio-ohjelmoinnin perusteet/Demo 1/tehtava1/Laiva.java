import java.util.*;

class Laiva {
    String nimi;
    int pituus;
    int syvays;
    double nopeus;


    public Laiva(String nimi, int pituus, int syvays, double nopeus) {
        this.nimi = nimi;
        this.pituus = pituus;
        this.syvays = syvays;
        this.nopeus = nopeus;
    }

    public static double matkanLaskeminen(double matka, double nopeus) {
        return matka/(nopeus/2);
    }

    public static void main(String[] args) {
        Scanner lukija = new Scanner(System.in);
        System.out.println("Anna laivan pituus metreinä: ");
        int pituus = Integer.valueOf(lukija.nextLine());
        System.out.println("Anna laivan syväys: ");
        int syvays = Integer.valueOf(lukija.nextLine());
        System.out.println("Anna laivan nopeus solmuina: ");
        double nopeus = lukija.nextDouble();
        System.out.println("Laivan nimi: ");
        String nimi = lukija.next();
        System.out.println("");
        System.out.println("");
        System.out.println("");
        System.out.println("Laiva: " + nimi + "\n"
        + "Pituus: " + pituus + " metriä" + "\n"
        + "Syväys: " + syvays + "\n"
        + "Nopeus: " + nopeus + " solmua");
        System.out.println("");
        System.out.println("");
        System.out.println("");
        System.out.println("");
        System.out.println("Syötä matka metreinä jolle haluat laskea laivalla kuluvan matkan. ");
        double matka = lukija.nextInt();
        System.out.println("Kuluva aika: " + matkanLaskeminen(matka,nopeus) + "sekunttia");
        lukija.close();
    } 
}
