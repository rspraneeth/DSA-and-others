

import java.util.Arrays;
import java.util.Scanner;
/** Approach is to reverse the array, and then reverse first b elements,
 * then reverse elements from b index to n-1 index */
public class rotation {
    /**Reversing the array based on given start and end indices*/
    public static void reverse(int[] A, int start, int end){
        while (start < end){
            int temp = A[start];
            A[start] = A[end];
            A[end] = temp;
            start ++;
            end --;
        }
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] a = new int[n];
        for (int i = 0; i<n; i++){
            a[i] = in.nextInt();
        }
        int b = in.nextInt()%n;
        reverse(a, 0, n-1);
        reverse(a, 0, b-1);
        reverse(a, b, n-1);
        System.out.println(Arrays.toString(a));
    }
}

//Given an integer array A of size N and an integer B, you have to print the same array after
// rotating it B times towards the right.
