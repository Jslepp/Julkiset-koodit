package tehtava1;

public class Laiva {
    String nimi;
    int pituus;
    int syvays;
    static double nopeus;

    // Pituus metreinä
    // syvays metreinä
    // nopeus solmuina

    public Laiva(String nimi, int pituus, int syvays, double nopeus) {
        this.nimi = nimi;
        this.pituus = pituus;
        this.syvays = syvays;
        Laiva.nopeus = nopeus;
    }

    // Matka metreinä

    public static double matkanLaskeminen(double matka) {
        return matka/(nopeus/2);
    }

}