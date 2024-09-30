import java.Random;
import java.util.Scanner; 
public class RandomNumber{
	public static void main(String[] args){
	Scanner scan = new Scanner(System.in);
	Random input = new Random();

	int number1 = input.nextInt(100);
	System.out.println(number1);

	int number2 = input.nextInt(100);
	System.out.println(number2);

	int sum = number1 + number2;

	System.out.println("Enter the sum of the numbers ");
	int number3 = scan.nextInt();

	System.out.print(sum);
	if sum == number3{
		System.out.print("True");
	}else{
		System.out.print("False");
	}
	}

} 