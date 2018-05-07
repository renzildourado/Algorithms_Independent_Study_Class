import java.util.Scanner;

/**
 * Created by Renzil Dourado on 1/28/2018.
 */
public class Non_divisible_subset {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int[] arr = new int[n];
        for(int arr_i = 0; arr_i < n; arr_i++){
            arr[arr_i] = in.nextInt();
        }
        int result = nonDivisibleSubset(k, arr);
        System.out.println(result);
        in.close();
    }


    public static int nonDivisibleSubset(int k, int[] arr) {

        int remainders[] = new int[k];
        int count = 0;
        int midLimit = (k/2) +1;

        for(int i=0; i<arr.length; i++){
            remainders[arr[i]%k] += 1;
        }

        if(remainders[0]>=1)
            count += 1;            //add ony one from set with 0 remainder

        for(int i=1; i<midLimit; i++) {
            if (i != k - i)
                count += Math.max(remainders[i], remainders[k - i]);
            else
                count += 1;         //add only 1 from the central remainder set
        }

        return count;


    }
}
