package LeetCode;

public class LongestIncSubSeq {
    public static int pos(int[] ar, int l, int h, int x ){
        while (l<=h){
            int m = (l+h)/2;
            if (ar[m] < x) l = m+1;
            else h = m-1;
        }
        return l;
    }

    public int lengthOfLIS(int[] nums) {
        int n = nums.length; int k = 0;
        int[] a = new int[n];
        a[k] = nums[0];
        for (int num:nums){
            if(num < a[k]) a[pos(a, 0, k, num)] = num;
            else if (a[k] < num) a[++k] = num;
        }
        return k+1;
    }

    public static void main(String[] args){
        LongestIncSubSeq lis = new LongestIncSubSeq();
        int[] arr = new int[]{10,9,2,5,3,7,101,18};
        System.out.println(lis.lengthOfLIS(arr));
    }
}

// 300. Longest Increasing Subsequence
//Given an integer array nums, return the length of the longest strictly increasing subsequence.
//A subsequence is a sequence that can be derived from an array by deleting some or no elements without
// changing the order of the remaining elements.
