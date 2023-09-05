

public class fiboExample {

	public static void main(String[] args) {

		fibomemo2();
	}

	private static void fibomemo2() {
		for (int i = 5; i < 51; i += 5) {
			valeur = new int[i+1];
			nbop=0;
			fiboMemo(i);
			System.out.println( i + " "+nbop );
		}
	}

	public static void fibomemo1() {
		for (int i = 5; i < 30; i += 5) {
			nbop = 0;
			fiboAvecMemo(i);

			System.out.print("" + i + " : " + nbop);
			nbop = 0;
			fibo(i);
			System.out.println(" " + nbop);
		}

	}

	public static void time() {
		// for( int i =0; i<101; i++)
		// System.out.println(i+"--->"+mesure_temps(i));
		int N = 45;
		System.out.println(fibo(N) + " " + fibodc(N) + " " + fibodyn(N) + " " + fiboAvecMemo(N));
		System.out.println(mesure_tempsclassic(N) + " " + mesure_tempsdc(N) + " " + mesure_tempsdyn(N) + " "
				+ mesure_tempsAvecMemo(N));
	}

	private static long mesure_tempsdc(int i) {
		long t0 = System.currentTimeMillis();
		fibodc(i);

		return System.currentTimeMillis() - t0;
	}

	private static long mesure_tempsclassic(int i) {
		long t0 = System.currentTimeMillis();
		fibo(i);

		return System.currentTimeMillis() - t0;
	}

	private static long mesure_tempsdyn(int i) {
		long t0 = System.currentTimeMillis();
		fibodyn(i);
		return System.currentTimeMillis() - t0;
	}

	private static long mesure_tempsAvecMemo(int i) {
		long t0 = System.currentTimeMillis();
		fiboAvecMemo(i);

		return System.currentTimeMillis() - t0;
	}

	public static int fibo(int n) {
		nbop++;
		if (n <= 1) {
			return n;
		} else {
			return fibo(n - 1) + fibo(n - 2);
		}

	}

	public static int fibodc(int n) {
		if (n == 0 || n == 1) {
			return n;
		} else {
			int a = fibodc((n + 1) / 2);
			int b = fibodc((n + 1) / 2 - 1);
			if (n % 2 == 0) {
				return a * (a + 2 * b);
			} else {
				return a * a + b * b;
			}
		}
	}

	public static int fibodyn(int n) {
		int sum, prev, res;
		sum = 0;
		prev = -1;
		res = 1;

		for (int i = 0; i <= n; i++) {
			sum = res + prev;
			prev = res;
			res = sum;
		}
		return res;
	}

	private static int[] value;
	private static int inconnu = -1;
	private static int nbop = 0;
	private static int[] valeur;

	public static int fiboAvecMemo(int n) {
		value = new int[n + 1];
		for (int i = 0; i < value.length; i++) {
			value[i] = inconnu;
		}
		return fiboM(n);
	}

	public static int fiboMemo(int n) {
		nbop++;
		if (n <= 1) {
			return n;
		} else {
			if (valeur[n] != 0) {
				return valeur[n];
			}
			int res = fiboMemo(n - 1) + fiboMemo(n - 2);
			valeur[n] = res;
			return res;
		}
	}

	public static int fiboM(int n) {

		if (dejaVu(n)) {
			nbop++;
			return solution(n);
		} else {
			nbop++;
			int sol = FiboR(n);
			stocke(n, sol);
			return sol;
		}
	}

	private static void stocke(int n, int sol) {
		value[n] = sol;

	}

	private static int FiboR(int n) {
		nbop++;
		if (n <= 1) {
			return n;
		} else
			return fiboM(n - 1) + fiboM(n - 2);

	}

	private static int solution(int n) {

		return value[n];
	}

	private static boolean dejaVu(int n) {
		return solution(n) != inconnu;
	}
}
