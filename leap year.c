void main()
{
int n;
clrscr();
printf("\n enter the year");
scanf("%d",&n);
if((n%400==0)||(n%100==0)||(n%4==0))
{
printf("\n entered year is a leap year");
}
else
{
printf("\n entered year is a not leap year");
}
getch();
}
