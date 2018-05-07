import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Coin_change {

    static long getWays(long n, long[] c){
        // Complete this function
        int noOfCoins = c.length;
        int sum = (int)n +1;
        long[][] dynamic_array = new long[noOfCoins][sum];

        for(int i=0; i<noOfCoins; i++)
            dynamic_array[i][0] = 1;

        for(int j=0; j<sum; j++) {
            if (j%c[0]==0)
                dynamic_array[0][j] = 1;
            else
                dynamic_array[0][j] = 0;
        }

        for(int i=1; i<noOfCoins; i++){
            for(int j=1; j<sum; j++){
                if(j >= c[i]){
                    dynamic_array[i][j] = dynamic_array[i-1][j] + dynamic_array[i][j-(int)c[i]];
                }
                else{
                    dynamic_array[i][j] = dynamic_array[i-1][j];
                }
            }
        }

        return (long)dynamic_array[noOfCoins-1][sum-1];
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        long[] c = new long[m];
        for(int c_i=0; c_i < m; c_i++){
            c[c_i] = in.nextLong();
        }
        // Print the number of ways of making change for 'n' units using coins having the values given by 'c'
        long ways = getWays(n, c);
        System.out.println(ways);
    }
}