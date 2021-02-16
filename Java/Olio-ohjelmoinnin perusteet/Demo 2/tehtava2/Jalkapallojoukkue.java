package tehtava2;

public class Jalkapallojoukkue {
    public String nimi;
    public String stadion;
    

    public Jalkapallojoukkue(String nimi, String stadion) {
        this.nimi= nimi;
        this.stadion= stadion;
        
    }

    public String getNimi() {

        return this.nimi;
    }
    public String getStadion() {
        
        return this.stadion;
    }
    
    public void setNimi(String nimi) {
        this.nimi=nimi;
        
    }
    public void setStadion(String stadion) {
        this.stadion=stadion;
    }
    @Override
    public String toString() {
        return "Tiimin nimi: " + this.nimi + "\n" + "Kotistadion: " +  this.stadion;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }

        if (obj == null) {
            return false;
        }
        
        if (obj.getClass() != Jalkapallojoukkue.class) {
            return false;
        }

        Jalkapallojoukkue toinen = (Jalkapallojoukkue) obj;

        return nimi.equals(toinen.nimi);
    }
}	