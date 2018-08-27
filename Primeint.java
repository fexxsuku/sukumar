public class Primeint {

    public static void main(String[] args) {

        int lim1 = 8, lim2 = 17;

        while (lim1 < lim2) {
            boolean flag = false;

            for(int i = 2; i <= lim1/2; ++i) {
             
                if(lim1 % i == 0) {
                    flag = true;
                    break;
                }
            }

            if (!flag)
                System.out.print(lim1 + " ");

            ++lim1;
        }
    }
}
