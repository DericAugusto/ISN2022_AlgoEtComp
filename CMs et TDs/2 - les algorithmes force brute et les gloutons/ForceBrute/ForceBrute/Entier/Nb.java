package ForceBrute.Entier;
import ForceBrute.Candidate;

public class Nb implements Candidate {
	int n;
	public Nb(Nb c) {
			n = c.n;
		}
		@Override
		public String toString() {
			return ""+ n + " ";
		}
		public Nb(int i) {
			n = i;
		}
		@Override
		public Candidate next() {
			n++;
			return this;
		}
		@Override
		public Candidate first() {
			n = 1;
			return this;
		}
	}