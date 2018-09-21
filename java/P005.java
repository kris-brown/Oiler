// Lowest number that divides 1 - 20  (2520 given as example for 1-10)
public final class P005 implements Solution {

	public static void main(String[] args) {
		System.out.println(new P005().run());
	}
	
	public String run() {
		long[] factors = {11,12,13,14,15,16,17,18,19,2520};
		return Long.toString(gcds(factors));
	}
	
	private long gcds(long[] xs) {
		for (int i=1;i<xs.length;i++) {
			xs[i] = lcm((long)xs[i-1],(long)xs[i]);
		}
		return xs[xs.length-1];
	}
   private long lcm(long a, long b) {
	   return a*b / gcd(a,b);
   }
   
   // Euclidean algorithm
   private long gcd(long a,long b) {
	   if (b==0) {
		   return a;
	   }
	   else {
		   return gcd(b,a % b);
	   }
   }
}
