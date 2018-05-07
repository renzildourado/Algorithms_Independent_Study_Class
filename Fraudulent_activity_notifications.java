import java.util.*;


public class Fraudulent_activity_notifications {

    static int activityNotifications(int[] expenditure, int d) {
        // Complete this function
        int start = d;
        int number_of_days = expenditure.length;
        int number_counts[] = new int[201];
        int count = 0;

        int mid;
        if(d%2 !=0)
            mid = (d/2) +1;
        else
            mid = d/2;


        for(int i=0; i<start; i++)
            number_counts[expenditure[i]] += 1;


        for(int i=start; i<number_of_days; i++){

            float median = 0;

            int sum = 0;
            int j;

            for(j=0; j<number_counts.length; j++) {
                sum += number_counts[j];
                if (mid <= sum)
                    break;
            }

            if(d%2!=0)
                median =  j;
            else
            {
                if(mid<sum)
                    median =  j;
                else{
                    int k=j+1;
                    while(number_counts[k]==0)
                        k++;
                    median =  (float)(j + k)/2;
                }

            }

            if(expenditure[i]>=2*median)
                count++;

            number_counts[expenditure[i-d]] -= 1;
            number_counts[expenditure[i]] += 1;
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int d = in.nextInt();
        int[] expenditure = new int[n];
        for(int expenditure_i = 0; expenditure_i < n; expenditure_i++){
            expenditure[expenditure_i] = in.nextInt();
        }
        int result = activityNotifications(expenditure, d);
        System.out.println(result);
        in.close();
    }
}
