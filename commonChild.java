import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class commonChild {

    static int commonChild(String s1, String s2){
        // Complete this function

        int m = s1.length()+1;
        int n = s2.length()+1;

        int dynamicArray[][] = new int[m][n];

        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                dynamicArray[i][j] = Math.max(dynamicArray[i-1][j], dynamicArray[i][j-1]);

                if(s1.charAt(i-1)==s2.charAt(j-1))
                    dynamicArray[i][j] = dynamicArray[i-1][j-1] + 1;

            }
        }

        return dynamicArray[m-1][n-1];
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s1 = in.next();
        String s2 = in.next();
        int result = commonChild(s1, s2);
        System.out.println(result);
    }
}
