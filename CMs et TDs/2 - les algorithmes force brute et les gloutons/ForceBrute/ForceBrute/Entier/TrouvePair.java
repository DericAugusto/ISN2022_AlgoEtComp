package ForceBrute.Entier;

import ForceBrute.Candidate;

public class TrouvePair {

	public static void main(String[] args) {
		EtatNbre sol = new EtatNbre(10){
			public boolean valid() {
			return ((Nb)current).n%2 ==0;};
		};
		Candidate c = sol.first();
		while (c !=null){
			if (sol.valid()){sol.output();}
			c=sol.next();
		}
		System.out.println(sol.l);
		

	}

}
