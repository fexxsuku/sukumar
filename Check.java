import java.util.*;

public class Check
{

     
public static void main(String []args)
{
    
 int sum=0;   
Scanner sc=new Scanner (System.in);
     
int a=sc.nextInt();
     
    
int nums[]=new int[a];
   
 
for(int i=0;i<a;i++)
     
{
         
nums[i]=sc.nextInt();
     
sum=sum+nums[i];
}
     
int median=sum/a;

for (int element :nums)
{
if(element==median)
{
System.out.println(""+median);
}
}
}

}
