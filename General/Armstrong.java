import java.util.Scanner;
public class Armstrong {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		for(int i = 1; i <= N; i++) {
			int num = i;
			int sum = 0;
			while (num > 0) {
				int d = num%10;
				sum += d*d*d;
				num = num/10;
			}
			if (sum == i) System.out.println(i+" is armstrong number");
		}
	}
}

/*You are given an integer N you need to print all the Armstrong Numbers between 1 to N. (N inclusive).

If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.

For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )*/