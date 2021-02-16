package tehtava1;

public class Main {
    public static void main(String[] args) {
		Rahtilaiva rahtilaiva1 = new Rahtilaiva("Rahtilautta",10.0,5.0,10.0,100.0,20.0);
		Autolautta autolautta1 = new Autolautta("Autolautta", 10.0, 5.0, 10.0, 300, 20, 700);

		System.out.println(autolautta1.nimi + ": " + Autolautta.kapasiteettiaJaljella());
		System.out.println(rahtilaiva1.nimi + ": " + Rahtilaiva.laskeNopeus(Rahtilaiva.rahti));
	}
}
