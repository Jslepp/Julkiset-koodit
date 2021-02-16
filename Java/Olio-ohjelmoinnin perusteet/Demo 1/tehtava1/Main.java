package tehtava1;

public class Main {

	public static void main(String[] args) {
		Laiva laiva1 = new Laiva("Titanic", 269.0, 10.0, 23.0);
		Laiva laiva2 = new Laiva("Mayflower", 27.5, 4.0, 3.0);
		
		System.out.println(laiva1.nimi + ": "+ laiva1.laskeKesto(30));
		System.out.println(laiva2.nimi + ": "+ laiva2.laskeKesto(30));
	}
	
}
