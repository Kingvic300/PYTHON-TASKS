import java.util.Scanner; 
public class Add{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("input a number: "); 
		int digit = input.nextInt();

		if (digit>0 || digit<1000){
			int number = digit;
			int digit1 = number%10;
			int digit2 = number/10;
			int digit3 = digit2%10;
			int digit4 = digit2/10;
	
			int add = digit1+digit3+digit4;
			System.out.print(add);
		}else{
			System.out.print("ERROR");
		}
	}
}