//Loop & control flow
package javaproject;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		/*
		String guess = "NOK";
		Scanner scanner = new Scanner(System.in);
		String word;
		
		do {
			System.out.println("guess pls");
			word = scanner.nextLine();	
		}while(!guess.toLowerCase().equals(word.toLowerCase()));
		
		scanner.close();
		*/
		
		//ternary operator
		//expression ? true : false;
		//single line if statement
		//if(expression) statement;
		//pyramid
		
		int[] array1 = new int[4];
		//int[] array1 = {2, 3, 5, 4};
		int i = 0;
		for (int item : array1) {
			item = i++;
			System.out.println(item);
		}
		System.out.println(Arrays.toString(array1));
		for(int j = 0; j < array1.length; j++) {
			array1[j] = i++;
		}
		System.out.println(Arrays.toString(array1));
		/*
		List<Integer> list1 = new ArrayList<Integer>();
		//list1 = Arrays.asList(5, 2, 3, 5, 6);
		for(int item : list1) {
			item.
		}

		System.out.print(Arrays.toString(array1));
		*/
		/*
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < 10; j++) {
				if((j >= i) && (j < (10 - i))) {
					System.out.print(j + " ");
				}else {
					System.out.print(" " + " ");
				}
			}
			System.out.println();
		}
		*/
	
	}

}
