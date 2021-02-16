package tehtava1;

public class Laiva2 {
	String nimi;
	double pituus;
	double syvays;
	static double nopeus;
	double kapasiteetti;
	public double rahti;

	public Laiva2(String nimi, double pituus, double syvays, double nopeus) {
		this.nimi = nimi;
		this.pituus = pituus;
		this.syvays = syvays;
		Laiva2.nopeus = nopeus;

	}

	public double laskeKesto(double matka) {
		return matka / nopeus;
	}

}

class Rahtilaiva extends Laiva2 {
	static double kapasiteetti;
	static double rahti;

	public Rahtilaiva(String nimi, double pituus, double syvays, double nopeus, double kapasiteetti, double rahti) {
		super(nimi, pituus, syvays, nopeus);
		Rahtilaiva.kapasiteetti = kapasiteetti;
		Rahtilaiva.rahti = rahti;

	}

	public static double laskeNopeus(double rahti) {
		return (1 - (rahti / kapasiteetti)) * nopeus;
	}

}

class Autolautta extends Laiva2  {
	static int kapasiteetti;
	static int matkustajakpl;
	static int ajoneuvokpl;

	public Autolautta(String nimi, double pituus, double syvays, double nopeus, int matkustajakpl, int ajoneuvokpl, int kapasiteetti) {
		super(nimi, pituus, syvays, nopeus);
		Autolautta.matkustajakpl = matkustajakpl;
		Autolautta.ajoneuvokpl = ajoneuvokpl;
		Autolautta.kapasiteetti = kapasiteetti;
	}

	public static int kapasiteettiaJaljella() {
		return kapasiteetti - (matkustajakpl + (ajoneuvokpl * 10));
	}
}

