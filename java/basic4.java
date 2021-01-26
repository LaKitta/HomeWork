//OOP
package javaproject;

import java.util.ArrayList;
import java.util.List;

public class Program {

	public static void main(String[] args) {
		
		List<User> users = new ArrayList<User>();
		/*
		String[] fns = {"A", "B", "C"};
		String[] lns = {"1", "2", "3"};
		
		for(int i = 0; i < 3; i++) {
			User user = new User(fns[i], lns[i]);
			users.add(user);
		}
		*/
		/*
		for ( User user : users) {
			System.out.println(User.print_name(user));
		}
		*/
		
		//System.out.println(users.get(0));
		//System.out.println(users.get(0).dosth(true));
		//System.out.println(users.get(0).dosth(false));
		
		//Inheritance
		Animal animal = new Animal("P", "IG");
		Alien alien = new Alien("BO", "BO");
		users.add(animal); users.add(alien);
		
		//animal.say_something();
		for(User user : users) user.say_something();
	}

}



