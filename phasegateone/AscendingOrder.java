import java.util.Scanner;
public class AscendingOrder{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);

		System.out.println("First number");
		int number1 = input.nextInt();

		System.out.println("Second number");
		int number2 = input.nextInt();
 
		System.out.println("Third number");
		int number3 = input.nextInt(); 

		if (number1>number2 && number2>number3){
			System.out.println(number3);
			System.out.println(number2);
			System.out.println(number1);

		}else if(number2>number1 && number1>number3){
			System.out.println(number3);
			System.out.println(number1);
			System.out.println(number2);

		}else if(number3>number1 && number1>number2){
			System.out.println(number2);
			System.out.println(number1);
			System.out.println(number3);

		}else if(number1>number3 && number3>number2){
			System.out.println(number2);
			System.out.println(number3);
			System.out.println(number1);

		}else if(number2>number3 && number3>number1){
			System.out.println(number1);
			System.out.println(number3);
			System.out.println(number2);

		}else if(number3>number2 && number2>number1){
			System.out.println(number1);								System.out.println(number2);
			System.out.println(number3);
		}
	}
}