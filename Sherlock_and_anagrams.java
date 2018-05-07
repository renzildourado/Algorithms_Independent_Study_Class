/**
 * Created by Renzil Dourado on 1/26/2018.
 */
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
public class Sherlock_and_anagrams {

    public static void main(String[] args){
       Scanner sc = new Scanner(System.in);
       int n = sc.nextInt();
       String[] words = new String[n];

       for(int i=0; i<n; i++){
           words[i] = sc.next();
       }

       for(int i=0; i<n; i++){
           System.out.println(calculatePairs(words[i]));
       }

    }

    public static int calculatePairs(String word){
        int length = word.length();
        int subSize = (length*(length+1)/2);
        String[] subStrings = new String[subSize];
        int index = 0, count = 0;
        HashMap<String, Integer> map = new HashMap<>();

        for(int i=0; i<length; i++){
            for(int size=1; i+size<=length; size++) {
                subStrings[index] = word.substring(i, i + size);
                index++;
            }
        }

        for(int i=0; i<subSize; i++){
            char temp[] = subStrings[i].toCharArray();
            Arrays.sort(temp);
            subStrings[i] = new String(temp);

            if(map.containsKey(subStrings[i]))
                map.put(subStrings[i], map.get(subStrings[i])+1);
            else
                map.put(subStrings[i], 1);

        }

        for(Map.Entry<String, Integer> entry : map.entrySet()){
            int value = entry.getValue();
            if(value>=2)
                count += (value*(value-1))/2;
        }

        return count;

    }
}
