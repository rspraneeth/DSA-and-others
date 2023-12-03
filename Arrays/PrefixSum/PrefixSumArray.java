package PrefixSum;

import java.util.ArrayList;

public class PrefixSumArray {
    public int[] pfSumArray(ArrayList<Integer> A){
        int[] pf = new int[A.size()];
        pf[0]= A.get(0);
        for (int i = 1; i < A.size(); i++) pf[i] = pf[i-1] + A.get(i);
        return pf;
    }

    public int[] pfEven(ArrayList<Integer> A){
        int[] pfe = new int[A.size()];
        pfe[0] = A.get(0);
        for (int i = 1; i < A.size(); i++){
            if (i % 2 == 1) pfe[i] = pfe[i-1];
            else pfe[i] = pfe[i-1] + A.get(i);
        }
        return pfe;
    }

    public int[] pfOdd(ArrayList<Integer> A){
        int[] pfo = new int[A.size()];
        pfo[0] = 0;
        for (int i = 1; i < A.size(); i++){
            if (i % 2 == 0) pfo[i] = pfo[i-1];
            else pfo[i] = pfo[i-1] + A.get(i);
        }
        return pfo;
    }
}
