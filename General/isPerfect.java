import java.util.Scanner;

public class isPerfect {
    public static void main(String[] args){
    	Scanner in = new Scanner(System.in);
        int T = in.nextInt();
        while(T-- > 0){
            int n = in.nextInt();
            int sum = 0;
            for(int i = 1; i < n/2 + 1; i++){
                if(n%i == 0) sum+= i;
                if(sum > n) break;
            }
            if(sum==n) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}

// You are given N positive integers. For each given integer A,
// you have to tell whether it is a perfect number or not.
// A perfect number is a positive integer which is equal
// to the sum of its proper positive divisors.
// A positive proper divisor divides a number without leaving any remainder.