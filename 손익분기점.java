package Algotrithm;

import java.util.Scanner;

public class 손익분기점 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int A,B,C; 
		Scanner scan = new Scanner(System.in);
		A = scan.nextInt();
		B = scan.nextInt();
		C = scan.nextInt();
		
		if (C <= B) {
			System.out.println("-1");
		} 
		else {
			System.out.println((A/(C-B))+1);
		}
	}
}
