package tehtava1;

public class Laiva {
	String nimi;
	double pituus;
	double syvays;
	double nopeus;
	
	/*
	 * @param pituus Laivan pituus metreinä
	 * @param syvays Laivan syväys metreinä
	 * @param nopeus Laivan nopeus solmuina
	 */
	public Laiva(String nimi, double pituus, double syvays, double nopeus) {
		this.nimi = nimi;
		this.pituus = pituus;
		this.syvays = syvays;
		this.nopeus = nopeus;
	}
	
	/*
	 * @param matka Laivan kulkema matka meripeninkulmina (1 mpk = 1,852 km)
	 * @return Laivan kulkeman matkan kesto tunteina
	 */
	public double laskeKesto(double matka) {
		return matka / nopeus;
	}
}
