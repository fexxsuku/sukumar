class Palindrome
{  
public static void main(String args[])
{  
int a,sum=0,temp;    
int n=454; 
temp=n;    
while(n>0)
{    
r=n%10; 
sum=(sum*10)+r;    
n=n/10;    
}    
if(temp==sum)    
System.out.println("given number is the palindrome number ");    
else    
System.out.println("given number is the not palindrome");    
}  
}  
