import java.lang.Math;
public class Table{
	public static void main(String[] args){
	System.out.println("A"+"\t"+"B"+"\t"+"A**B");
	for(int count = 1; count<=5;count++){
		int counter = count+1; 
		double power = Math.pow(count,counter);
		System.out.println(count+"\t"+counter+"\t"+power);
	} 
	}

}