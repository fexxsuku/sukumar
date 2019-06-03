import java.util.*;

public class Sort
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
     

 for (int element: nums) {
            System.out.println(element);
        }   
}

}
