package LeetCode;

public class countVowels_LC1220 {
    private static final int mod = 1000000007;
    public int countVowelPermutation(int n){
        int a, e, i, o, u;
        a = e = i = o = u = 1;
        for(int j = 1; j < n; j++){
            int na = e;
            int ne = (a + i)%mod;
            int ni = ((a + e)%mod + (o + u)%mod)%mod;
            int no = (u + i)%mod;
            int nu = a;
            a = na; e = ne; i = ni; o = no; u = nu;
        }
        return ((a+e)%mod+((i+o)%mod+u)%mod)%mod;
    }

    public static void main(String[] args) {
        countVowels_LC1220 cv = new countVowels_LC1220();
        System.out.println(cv.countVowelPermutation(5));
    }
}

//leet code 1220. Count Vowels Permutation
//Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
//Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
//Each vowel 'a' may only be followed by an 'e'.
//Each vowel 'e' may only be followed by an 'a' or an 'i'.
//Each vowel 'i' may not be followed by another 'i'.
//Each vowel 'o' may only be followed by an 'i' or a 'u'.
//Each vowel 'u' may only be followed by an 'a'.
//Since the answer may be too large, return it modulo 10^9 + 7.
