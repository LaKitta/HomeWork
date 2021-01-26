package javaproject;

public class User {
	//members
	public String first_name = "Good";
	public String last_name = "One";
	
	public void set_name(String name) {
		first_name = name;
	}
	
	public String get_name() {
		return first_name + " " + last_name;
	}
	
	public User(){}
	
	public User(String fn, String ln) {
		first_name = fn;
		last_name = ln;
	}
	
	public static String print_name(User user) {
		return user.first_name + " " + user.last_name;
	}
	
	
	//Method Overloading
	public String dosth() {
		return get_name();
	}
	
	public String dosth(boolean bool) {
		if(bool) return "GOOD";
		return "NO";
	}

	@Override
	public String toString() {
		return "User [first_name=" + first_name + ", last_name=" + last_name + "]";
	}
	
	//Abstract -> method without body
	public void say_something() {
		System.out.println("This is User");
	}
	
	//Interface
	//public abstract void say();
	
	

}
