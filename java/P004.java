/*
 * A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 * Find the largest palindrome made from the product of two 3-digit numbers.
 */
public final class P004 implements Solution {

	public static void main(String[] args) {
		System.out.println(new P004().run());
	}

	public String run() {
		int best = 0;
		for (int i = 100; i < 1000; i++) {
			for (int j = i; j < 1000; j++) {
				int ij = i * j;
				if (pallin(Integer.toString(ij))) {
					best = Math.max(ij, best);
				}
			}
		}
		return Integer.toString(best);
	}

	private static boolean pallin(String s) {
		int n = s.length();
		for (int i = 0; i < n / 2; i++) {
			if (s.charAt(i) != s.charAt(n - i - 1)) {
				return false;
			}
		}
		return true;
	}
}
