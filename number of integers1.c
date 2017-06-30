
void main()
{
int n,count=0;
clrscr();
printf("\n enter the number ");
scanf("%d",&n);
while(n!=0)
{
n/=10;
++count;
}
printf("\n tne number of integers are %d",count);
getch();
}
