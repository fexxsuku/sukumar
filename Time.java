import java.util.*;

import java.io.*;

class Time

{

public static void main(String args[])

{

        System.out.println("enter time in mintues");

Scanner sc=new Scanner(System.in);

int num=sc.nextInt();

int co=num/60;
int re=num%60;

System.out.println("the "+num+" minutes is equals to "+co+"hour and "+re+" minutes");

}
}
