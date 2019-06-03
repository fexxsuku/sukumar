import java.util.*;

public class Min
{

     
public static void main(String []args)
{
    
System.out.println("enter no of elements");
    
Scanner sc=new Scanner (System.in);
     
int a=sc.nextInt();
     
    
int nums[]=new int[a];
   
System.out.println("enter elements");
  
for(int i=0;i<a;i++)
     
{
         
nums[i]=sc.nextInt();
     
}
     
Arrays.sort(nums);
     
System.out.println("Minimum = " + nums[0]);
     
}

}
