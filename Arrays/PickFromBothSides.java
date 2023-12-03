import java.util.ArrayList;
import java.util.List;

public class PickFromBothSides {
    public static void main(String[] args) {
        ArrayList<Integer>  a = new ArrayList<>(List.of(5, -2, 3 , 1, 2));
        int b = 3;
        System.out.println(solve(a, b));
    }

    public static int solve(ArrayList<Integer> A, int B) {
        int max_sum, sum = 0;
        for (int i = 0; i < B; i++) sum += A.get(i);
        max_sum = sum;
        int j = A.size()-1;
        for (int i = B-1; i >= 0; i--){
            sum = sum - A.get(i) + A.get(j);
            max_sum = Math.max(max_sum, sum);
            j--;
        }
        return max_sum;
    }
}
