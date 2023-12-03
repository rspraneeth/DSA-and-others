import java.util.ArrayList;
import java.util.Arrays;

/**Given an array of integers A and multiple values in B, which represents the number of times array A
 * needs to be left rotated. Find the rotated array for each value and return the result in the form of a
 * matrix where ith row represents the rotated array for the ith value in B.*/
public class MultipleRotations {
    public static void main(String[] args) {
        ArrayList<Integer> A = new ArrayList<>(Arrays.asList(1,2,3,4,5));
        ArrayList<Integer> B = new ArrayList<>(2);
        B.add(2);B.add(3);
        Sol s = new Sol();
        System.out.println(s.solve(A, B));
    }
}

class Sol {
    public ArrayList<ArrayList<Integer>> solve(ArrayList<Integer> A, ArrayList<Integer> B) {
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();
        int n = A.size();
        for (int r: B){
            ArrayList<Integer> temp = new ArrayList<>();
            for (int i = 0; i<n; i++)temp.add(A.get((i+r)%n));
            arr.add(temp);
        }
        return arr;
    }
}
