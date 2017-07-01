int main()
{
    int base, power;

    long long result = 1;

    printf("Enter a base number: ");
    scanf("%d", &base);

    printf("Enter an power: ");
    scanf("%d", &expower);

    while (exponent != 0)
    {
        result *= base;
        --power;
    }

    printf("Answer = %lld", result);

    return 0;
}
