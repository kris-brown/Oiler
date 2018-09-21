/*
 * Determine largest prime factor of 600851475143
 */
public final class P003 implements Solution {

	public static void main(String[] args) {
		System.out.println(new P003().run());
	}

	public String run() {
		long n = 600851475143L;
		int largest_factor = 1;
		while (n > 1) {
			boolean found = false ;
			int max_i = (int) Math.sqrt(n);
			for (int i = 2; i <= max_i; i++) {
				if (n % i == 0) {
					largest_factor = Math.max(i, largest_factor);
					n = n / i ;
					found= true ;
					break;
				}
			}
			if (! found) {
				largest_factor = Math.max((int)n,largest_factor);
				n = 1;
			}
		}
		return Integer.toString(largest_factor);
	}

}
