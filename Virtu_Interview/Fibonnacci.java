public class Fibonnacci {

    public static int fib1(int fib) {

        if (fib == 0)
            return 0;

        int first = 0;
        int second = 1;
        int third = 1;

        for (int i = 3; i <= fib; i++) {
            first = second;
            second = third;
            third = second + third;

        }

        return third;

    }

    public static void main(String[] args) {

        System.out.println(fib1(2));

    }

}
