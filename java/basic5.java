//enum
package javaproject;



public class Program {

	public static void main(String[] args) {
		//User usr1 = new User();
		//usr1.abc = User.abc.A;
		
		Animal ani = new Animal();
		ani.abc = Animal.weigth.Good;
		
		//System.out.println(ani.abc);
		
		switch(ani.abc) {
		case Bad:
			System.out.println("Bad");
			break;
		default:
			System.out.println("NO");
			break;
		}
		
		
		
		
	}

}
