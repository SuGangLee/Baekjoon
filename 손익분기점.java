//총비용 (가격 * n-판 개수) > 고정비용 + 가변비용*n 
//n = A/C-B 이다. 이때 C<B -> 분모가 음수가 되므로 -1 출력 
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
