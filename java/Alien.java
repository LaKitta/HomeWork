package javaproject;

public class Alien extends User implements say_something{

	public Alien(String fn, String ln) {
		super(fn, ln);
		// TODO Auto-generated constructor stub
	}
	
	@Override
	public void say_something() {
		System.out.println("This is Alien");
	}

	@Override
	public void say() {
		// TODO Auto-generated method stub
		
	}

}
