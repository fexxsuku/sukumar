import java.util.*;

public class Min
{

     
public static void main(String []args)
{
    
    
Scanner sc=new Scanner (System.in);
     
int a=sc.nextInt();
     
    
int nums[]=new int[a];
   

  
for(int i=0;i<a;i++)
     
{
         
nums[i]=sc.nextInt();
     
}
     
Arrays.sort(nums);
     
System.out.println("Minimum = " + nums[0]);
     
}

}
