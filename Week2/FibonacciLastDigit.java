package ntl;

import java.util.Scanner;

public class NTL {
   
    public static void main(String[] args) {
            Scanner in = new Scanner(System.in);
            int n = in.nextInt();
            System.out.println(calc_fib(n));
        
    }
    public static int calc_fib (int n){
         int a =0 ;
         int b = 1;
         int t=0;
     for( int i =0; i <n ; i++){
   
    
    t=a+b ; a=b ; b=t;
    
    }
    return a;}
     
            
	
    
    
}
