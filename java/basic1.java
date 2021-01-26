//Datatype, method, primitives
package javaproject;

import java.util.Scanner;

public class Program {
	//public static final double PI = 3.14;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		User user1 = new User();
		user1.set_name("Google");
		System.out.println(user1.get_name());
		//Scanner scanner = new Scanner(System.in);
		//String word = scanner.nextLine();
		//System.out.println(word + " :) ");
		//System.out.println(args[0]);
		//scanner.close();
		//constant -> final
		//casting -> double r = (double) (2.0/3);
		/* Integer static method
		Integer.max(0, 0);
		Integer.compare(0, 0);
		Integer.valueOf(string);
		Integer.parseInt(sting);
		*/
		/* String method
		String x = "ABCDEFG\n";
		x.length();
		x.contains("ABC");
		x.indexOf("ABC", index);
		x.indexOf("template", x.indexOf("template") + 1);
		x.lastIndexOf("template");
		x.toUpperCase()/toLowerCase();
		x.strip();
		x.substring(index, index);
		x.charAt(index);
		x.equals(sting);
		String.format(" ... %s", string);
		*/
	}

}
