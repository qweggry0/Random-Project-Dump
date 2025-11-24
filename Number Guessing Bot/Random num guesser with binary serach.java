import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
import java.util.List;

public class Game {
    public static void main(String args[]) {

        List<Integer> attempt_list = new ArrayList<>();
        double attempt_average = 0;
        int attempt_total = 0;
        
        for (int i = 0; i < 100; i++) {
            attempt_list.add(BotSearch());
            }


        System.out.println("ATTEMPT LIST --> " + attempt_list);
        
        int attempt_len = attempt_list.size();
        for (int attempt : attempt_list){
            attempt_total = attempt_total + attempt;
        }
        attempt_average = (double) attempt_total / attempt_len;
        
        System.out.println("ATTEMPT AVERAGE " + attempt_average);
    }


    public static int BotSearch() {
        int attempts = 0;

        List<Integer> numbers = new ArrayList<>();
        for (int i = 1; i <= 100; i++) {
            numbers.add(i);
        }

        Scanner scanner = new Scanner(System.in);
        int bound = 100;
        Random random = new Random();
        int rand_int = random.nextInt(bound) + 1;

        boolean run = true;

        int high = numbers.size();
        int low = 1;
        int middle = (high + low) / 2;
        
        System.out.println("TARGET: " + rand_int);
        while (run == true) {
            System.out.println("I am searching " + middle);
            attempts = attempts + 1;

            if (rand_int == middle) {
                System.out.println("FOUND  " + rand_int + " AT TOTAL ATTEMPT: " + attempts);
                run = false;
                continue;
            } else if (rand_int > middle) {
                low = middle + 1;
                middle = (high + low) / 2;
            } else if (rand_int < middle) {
                high = middle - 1;
                middle = (high + low) / 2;
            }
            
        }
        return attempts;
    }
}
