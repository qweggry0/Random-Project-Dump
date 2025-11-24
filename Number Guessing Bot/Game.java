import java.util.Scanner;
import java.util.Random;

public class Game {
  public static void main(String args[]) {
    //Start();
    MainGameLoop();
  }
  public static void Start(){
      Scanner scanner = new Scanner(System.in);
      System.out.println("Welcome to slot machines");
      System.out.print("Press Enter to play: ");
      String filler = scanner.nextLine();

  }
  
  public static void MainGameLoop(){
      int attempts = 0;
      
      Scanner scanner = new Scanner(System.in);
      int bound = 101;
      Random random = new Random();
      int rand_int = random.nextInt(bound);
      
      boolean run = true;
      while(run == true){
          System.out.print("Guess a random integer: ");
          int guess = scanner.nextInt();
          if(guess == rand_int){
              System.out.println("you guessed the number correctly in " + attempts + "attempts");
              run = false;
              continue;
          }
          else{
              System.out.println(ColdWarm(guess, rand_int));
              attempts = attempts + 1;
              
          }
          
      }
      
  }
  public static String ColdWarm(int num, int target){
      double perc_diff = 0.0;
      if (num > target){
          perc_diff = (double) target / num;
      }
      else{
          perc_diff = (double) num / target;
      }
      if (perc_diff >= 0.95){
          return "SCORCHING HOT";
      }
      else if (perc_diff >= 0.9){
          return "BOILING";
      }
      else if (perc_diff >= 0.85){
          return "VERY HOT";
      }
      else if (perc_diff >= 0.8){
          return "HOT";
      }
      else if (perc_diff > 0.7){
          return "WARM";
      }
      else if (perc_diff > 0.6){
          return "SLIGHTLY WARM";
      }
      else{
          return "COLD";
      }
    }
      
      

          
     
}

    


