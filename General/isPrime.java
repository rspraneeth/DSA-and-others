import java.util.Scanner;

public class isPrime {
    public static void main(String[] args){
    	Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int count = 0;
        for(int i = 1; i <= n; i++) if (n%i == 0) count++;
        if (count == 2) System.out.println("YES");
        else System.out.println("NO");
    }
}

/*Take an integer A as input, you have to tell whether it is a prime number or not.

A prime number is a natural number greater than 1 which is divisible only by 1 and itself.

So it has only 2 factors.*/
