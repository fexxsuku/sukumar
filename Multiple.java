import java.util.*;

import java.io.*;

class Multiple

{

public static void main(String args[])

{

System.out.println("enter number");

Scanner sc=new Scanner(System.in);

int num=sc.nextInt();

for(int i=1;i<=5;i++)
{
int mul=num*i;
System.out.println(mul);
}
}
}
