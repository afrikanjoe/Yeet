/*

Sum of all prime numbers between 1 and 100 that are 1 
less than a multiple of 5 and 1 greater than a multiple of 4.


*/


public class SumOfPrimes5and4 {

    //1 less than multiple of 5 has final digit of 4 or 9
    //no prime numbers have the number 4 cause its divisible by 2

    //find all prime digits with final digit of 9
        //of those find all digits that are a multiple of 4 when adding 1
            //find the sum


    public static int findPrimeNumSum(int n){

        int sum = 0;
        for (int i=0; i<n; i++){
            if(isPrime(i)){
                if((i % 10 == 9) && ((i-1) % 4 == 0)) {
                        sum += i;
                    }         
            }   
        }
        
        return sum;


    }
    private static boolean isPrime(int num){

        if(num <=1) return false;
        for(int i = 2; i <= Math.sqrt(num); i++){
            if (num % i == 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {

        System.out.println(findPrimeNumSum(100));



    }

    
}
