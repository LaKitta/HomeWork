package javaproject;

public class Animal extends User implements say_something {

	public Animal(String fn, String ln) {
		super(fn, ln);
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public void say_something() {
		System.out.println("This is Animal");
	}

	@Override
	public void say() {
		// TODO Auto-generated method stub
		System.out.println("This is Animal");
	}		

}
