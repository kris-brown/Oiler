/* 
 * Finds the sum of the even-valued Fibonacci terms < 4e6
 */

public final class P002 implements Solution {

	/*
	 * Static class acts as a generator of Fib numbers which retains memory of previous two numbers
	 */
	static class FibGen {
		public static int m1 = 1;
		public static int m2 = 1;

		public static int next() {
			int m3 = m1;
			m1 = m2;
			m2 = m3 + m2;
			return m2;
		}

	}	
	
	public static void main(String[] args) {
		System.out.println(new P002().run());

	}

	public String run() {
		int n = 1;   // current fibonacci number
		int sum = 0;
		while (n < 4000000) {
			n = FibGen.next();
			if (n % 2 == 0) {
				sum += n;
			}
		}
		return Integer.toString(sum);
	}
}


