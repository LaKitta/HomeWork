//Collections, array, list
package javaproject;

import java.util.ArrayList;
import java.util.Arrays;
//import java.util.Arrays;
import java.util.List;
public class Program {

	public static void main(String[] args) {
		
		/*
		int[][] ar1 = {{1, 2, 3}, {5, 6}, {7, 8, 9, 0}};
		System.out.println(Arrays.deepToString(ar1));
		*/
		
		List<Integer> ar2 = new ArrayList<Integer>();
		List<Integer> ar3 = Arrays.asList(1, 2, 3, 4, 5);
		List<List<Integer>> ar4 = new ArrayList<List<Integer>>();
				
		ar2.add(11);
		ar2.add(1,7);
		
		ar4.add(Arrays.asList(1, 3, 5));
		ar4.add(Arrays.asList(3, 5));
		ar4.add(Arrays.asList(5));
		
		System.out.println(ar2.get(0));
		System.out.println(Arrays.toString(ar3.toArray()));
		
		for(List<Integer> item : ar4) {
			for(int item2 : item) {
				System.out.print(item2 + " ");
			}
			System.out.println();
		}
		
		/* list method
		list.indexof()/contains();
		list.isEmpty();
		list.add()/get()/set()/remove()/clear();
		list.size();
		Collections.sort(list);
		Collection.reverse(list);
		 */
		
		
	}

}
