package ForceBrute.Entier;
import java.util.ArrayList;
import java.util.List;

import ForceBrute.Candidate;
import ForceBrute.Etat;

public abstract class EtatNbre extends Etat {
	int max;
	Candidate current;
	List<Nb> l;

	public EtatNbre(int m) {
		max = m;
		l = new ArrayList<Nb>();
	}

	@Override
	public Candidate first() {
		if (max > 0) {
			return current = new Nb(1);
		} else
			return null;
	}

	@Override
	public Candidate next() {

		if (((Nb) current).n == max) {
			return current = null;
		} else {
			return current = current.next();
		}
	}

	@Override
	public abstract boolean valid();

	@Override
	public void output() {
		l.add(new Nb((Nb) current));
	}

}
