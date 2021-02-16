package tehtava2;
import java.util.Random;
import java.util.ArrayList;

public class Jalkapallopelaaja {
    String pelaajannimi;
    int numero;

    public Jalkapallopelaaja(String pelaajannimi, int numero) {
        this.pelaajannimi = pelaajannimi;
        this.numero = numero;
        
    }
 
    public String getPelaajannimi() {
        return this.pelaajannimi;
    }
    
    public int getNumero() {
        return this.numero;
    }

    public void setPelaajannimi(String pelaajannimi) {
        this.pelaajannimi = pelaajannimi;
    }
    
    
    public void setNumero(int numero) {
        this.numero = numero;
    }

     @Override
     public String toString() {
        return this.pelaajannimi + ", " + this.numero;
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }

        if (obj == null) {
            return false;
        }
        
        if (obj.getClass() != Jalkapallopelaaja.class) {
            return false;
        }

        Jalkapallopelaaja toinen = (Jalkapallopelaaja) obj;

        return pelaajannimi.equals(toinen.pelaajannimi);
    }
    
    public static void generoiPelaajat() {
        Jalkapallopelaaja[] jalkapallopelaaja = new Jalkapallopelaaja[22];
        int pelaajaArpa = 0;
        Random rand = new Random();
        ArrayList<String> nimet = new ArrayList<String>();
        ArrayList<String> sukunimet = new ArrayList<String>();
        nimet.add("Heikki");
        nimet.add("Matti");
        nimet.add("Leo");
        nimet.add("Santeri");
        nimet.add("Jaakko");
        nimet.add("Juuso");
        nimet.add("Ossi");
        nimet.add("Kalle");
        nimet.add("Jouni");
        nimet.add("Jussi");
        sukunimet.add("Puro");
        sukunimet.add("Havu");
        sukunimet.add("Hainari");
        sukunimet.add("Alkio");
        sukunimet.add("Turkka");
        sukunimet.add("Hattara");
        sukunimet.add("Saarenpää");
        sukunimet.add("Soini");
        sukunimet.add("Harki");
        sukunimet.add("Hiekkala");
        for (int i = 0; i < 22; i++) {
            pelaajaArpa = rand.nextInt(10);
            String etunimi = nimet.get(pelaajaArpa);
            pelaajaArpa = rand.nextInt(10);
            String sukunimi = sukunimet.get(pelaajaArpa);
            int pelinumero = rand.nextInt(99);
            jalkapallopelaaja[i] = new Jalkapallopelaaja(etunimi + " " + sukunimi, pelinumero);
            System.out.println(jalkapallopelaaja[i]);
        }
    }
}
    
