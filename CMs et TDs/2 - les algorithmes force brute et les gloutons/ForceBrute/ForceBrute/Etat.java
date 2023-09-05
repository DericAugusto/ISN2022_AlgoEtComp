package ForceBrute;

public abstract class Etat {
	
	
	public abstract Candidate first ();
	public abstract Candidate next();
	public abstract boolean valid();
	public abstract void output();

}
