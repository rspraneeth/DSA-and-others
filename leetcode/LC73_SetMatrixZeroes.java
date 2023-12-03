package LeetCode;

public class LC73_SetMatrixZeroes {
    public static void main(String[] args) {
        int[][] m = {{0, 1, 2, 0}, {3, 4, 5, 2}, {1, 3, 1, 5}};
        setZeroes(m);
        PrintMatrix(m);
    }

    static void PrintMatrix(int[][] a){
        for (int[] ints : a) {
            for (int j = 0; j < a[0].length; j++) {
                System.out.print(ints[j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
    static void setZeroes(int[][] matrix){
        int m = matrix.length;
        int n = matrix[0].length;

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if (matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }
        PrintMatrix(matrix);

        for(int j = 0; j < n; j++){
            if(matrix[0][j] == 0){
                for(int i = 1; i < m; i++){
                    matrix[i][j] = 0;
                }
            }
        }
        PrintMatrix(matrix);

        for(int i = 0; i < m; i++){
            if(matrix[i][0] == 0){
                for(int j = 1; j < n; j++){
                    matrix[i][j] = 0;
                }
            }
        }
        PrintMatrix(matrix);
    }
}
