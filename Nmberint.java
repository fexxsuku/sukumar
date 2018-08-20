import java.util.*;
import java.io.*;
class Numberint
{
  public static void main(String args[])
  {
    System.out.println("enter the first and last number");
    Scanner sc=new Scanner(System.in);
    int num1=sc.nextInt();
    Scanner ss=new Scanner(System.in);
    int num2=ss.nextInt();
    for(int i=num1;i<num2;i++)
    {
      if(i%2==0)
      {
        System.out.println(+i);
      }
    }
  }
}
