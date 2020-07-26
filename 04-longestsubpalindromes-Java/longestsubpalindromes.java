// # Write the function longestSubpalindrome(s), that takes a string s and returns 
// the longest palindrome that occurs as consecutive characters (not just letters, but 
// 	any characters) in s. So:
// #    	longestSubpalindrome("ab-4-be!!!") 
// # returns "b-4-b". If there is a tie, return the lexicographically larger value -- 
// in java, a string s1 is lexicographically greater than a string s2 if (s1 > s2). So:
// #    	longestSubpalindrome("abcbce") 
// # returns "cbc", since ("cbc" > "bcb"). Note that unlike the previous functions, 
// this function is case-sensitive (so "A" is not treated the same as "a" here). Also, 
// from the explanation above, we see that longestSubpalindrome("aba") is "aba", 
// and longestSubpalindrome("a") is "a".

class longestsubpalindromes {
	public String fun_longestsubpalindromes(String s){
		String ss = "";
		for(int i=0; i<=s.length();i++){
			for(int j=i;j<=s.length();j++){
				String s1 = s.substring(i,j);
				String s2="";
				for (int k=s1.length()-1; k>=0;k--){
					s2+=s1.charAt(k);
				}
				if (s1.equals(s2)){
					if  (ss.length()<=s1.length()){
						ss = s1;
					}
				}
			}
		}
		return ss;
	}
}
