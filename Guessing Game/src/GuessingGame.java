import java.util.Scanner;

public class GuessingGame //Kyle Whitaker's Code
{
	
	public static void main(String[] args) 
	{
		boolean x = true;//Begins loop of program if you want to play again
		while (x = true)
		{
			Scanner cin = new Scanner(System.in);
			System.out.println("How high should the numbers go? ENTER UPPER LIMIT");
					
			int U = cin.nextInt();	//takes in a number to set as the upper limit of the range of random numbers
			int random = (int)(1 + U*Math.random()); //makes a random number based on the limit of 1-U
					
			System.out.println("Take a guess, take a gander, pick a number!");
					
			boolean n = true;//sets loop of the reactions to guesses
			while (n = true)
			{
				int guess = cin.nextInt();
				if(guess<random)// is the guess less than the generated number?
				{
					System.out.println("Too low, try again...");
				}
				if(guess>random)//is the guess greater than the generated number?
				{
					System.out.println("Too high, try again...");				
				}				
				else if(guess==random)//the player guesses correctly
				{
					System.out.println("A WINNER IS YOU! Play again? If so...");
					break;// stops this loop
				}
			}
		} 
	}
}	

