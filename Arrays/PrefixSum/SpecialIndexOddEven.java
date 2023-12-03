package PrefixSum;

import java.util.ArrayList;
import java.util.List;

public class SpecialIndexOddEven {

    public static void main(String[] args) {
        ArrayList<Integer> a = new ArrayList<>(List.of(2, 1, 6, 4));
        System.out.println(solve(a));
        System.out.println(solve1(a));
    }

    public static int solve(ArrayList<Integer> A) {
        int c = 0;
        PrefixSumArray pf = new PrefixSumArray();
        int[] pfEven = pf.pfEven(A);
        int[] pfOdd = pf.pfOdd(A);
        int t_even, t_odd, n = A.size();
        for (int i = 0; i < n; i++){
            if (i == 0){
                t_even = pfOdd[n-1];
                t_odd = pfEven[n-1] - pfEven[0];
            }
            else {
                t_even = pfEven[i-1] + pfOdd[n-1] - pfOdd[i];
                t_odd = pfOdd[i-1] + pfEven[n-1] - pfEven[i];
            }
            if (t_even == t_odd) c++;
        }
        return c;
    }

    /**Simple solution without using prefix sum concept, Solution provided by lee215 of leetcode.
     * Initially we take of sum of odd, even elements in right array, right[0] = even sum, right[1] = odd sum,
     * At any element there will be two parts, split array into left and right. When we iterate through Array A,
     * and split at each A[i], we move one element from right to left array, reduce the sum in right array
     * according to element index, check if it's fair, since we removed one element, right[0] has odd sum and
     * right[1] has even sum of right side elements of ith index. Add the removed element from right into left sum.
     * So that left[0] and left[1] has even sum and odd sum respectively.*/

    public static int solve1(ArrayList<Integer> A){
        int c = 0, n = A.size();
        int[] right = new int[2];
        int[] left = new int[2];
        for (int i = 0; i < n; i++) right[i%2] += A.get(i);
        for (int i = 0; i < n; i++){
            right[i%2] -= A.get(i);
            if (right[0] + left[1] == right[1] + left[0]) c++;
            left[i%2] += A.get(i);
        }

        return c;
    }
}
