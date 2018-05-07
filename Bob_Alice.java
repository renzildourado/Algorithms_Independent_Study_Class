import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Bob_Alice {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int g = in.nextInt();
        boolean[] map = new boolean[1000001];
        ArrayList<Integer> primes = new ArrayList<>();


        for(int i= 2; i<=Math.sqrt(100000); i++){
            if(!map[i]){

                for(int j = i*2; j<=100000; j+=i){
                    map[j] = true;
                }
            }
        }

        for(int i=2; i<=100000; i++)
            if(!map[i])
                primes.add(i);

        for(int a0 = 0; a0 < g; a0++){
            int n = in.nextInt();
            int primeCount = 0;
            int i = 0;

            while(primes.get(i) <= n ){
                primeCount++;
                i++;

                if(i == primes.size())
                    break;
            }

            if(primeCount%2 ==0)
                System.out.println("Bob");
            else
                System.out.println("Alice");
        }
    }

}
