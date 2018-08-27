public class Armstrongint {

    public static void main(String[] args) {

        int lim1 = 360, lim2 = 380;

        for(int number = lim1 + 1; number < lim2; ++number) {
            int digits = 0;
            int result = 0;
            int originalNumber = number;

          
            while (originalNumber != 0) {
                originalNumber /= 10;
                ++digits;
            }

            originalNumber = number;

            
            while (originalNumber != 0) {
                int remainder = originalNumber % 10;
                result += Math.pow(remainder, digits);
                originalNumber /= 10;
            }

            if (result == number)
                System.out.print(number + " ");
        }
    }
}
