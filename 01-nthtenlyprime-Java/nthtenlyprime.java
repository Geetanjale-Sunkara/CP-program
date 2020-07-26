// nthTenlyPrime(n)
// We will say that a number is “tenly” (a made-up term) if the digits of the 
// number add up to 10. So 1153 is tenly, but 153 is not. With this in mind, write 
// the function nthTenlyPrime(n) that takes a non-negative int n and returns the 
// nth number that is both tenly and prime. You should also write all the required 
// helper functions. The first several tenly primes are: 19, 37, 73, 109, 127…


class nthtenlyprime {
	public int fun_nthtenlyprime(int n){
		int i = 19;
		int cnt = 0;
		while (cnt<n){
			i+=9;
			int nn = i;
			int sum = 0;
			while (nn >0){
				sum += nn%10;
				nn = nn/10;
			}
			if (sum == 10){
				boolean f = true;
				for(int j =2;j<i/2;j++){
					if (i%j == 0){
						f = false;
					}
				}
				if (f){
					cnt+=1;
				}
				
			}
		}
		return i;
	}
}