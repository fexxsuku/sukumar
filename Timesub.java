import java.util.*;

import java.io.*;

class Timesub

{

public static void main(String args[])

{

               try
        {
         System.out.println("enter time 1 hours");

Scanner sc=new Scanner(System.in);

int num=sc.nextInt();


System.out.println("enter time 1 minutes");

Scanner sc1=new Scanner(System.in);

int num1=sc1.nextInt();



System.out.println("enter time 2 hours");

Scanner sc2=new Scanner(System.in);

int num2=sc2.nextInt();



System.out.println("enter time 1 minutes");

Scanner sc3=new Scanner(System.in);

int num3=sc3.nextInt();

int hnum=num-num2;
int mnum=num1-num3;

System.out.println("subtracted time is"+hnum+ " hours and "+mnum+"minutes");

        }
catch(Exception e)
{
}

}
}
