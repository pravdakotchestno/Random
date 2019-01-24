import java.math.BigInteger;
import java.util.Scanner;

public class main {
    static Scanner scan=new Scanner(System.in);
    public static void main(String[] args){

        System.out.println("Enter your number:");
        BigInteger number=new BigInteger(scan.nextLine());

        if(number.compareTo(new BigInteger("0"))<=0){

            System.out.println("Number is negative or 0");

        }else{

            String str=decToBin(number);

            System.out.println(str);

        }

    }
    public static String decToBin(BigInteger num){

        if(!num.equals(new BigInteger("0"))){

            return decToBin(num.divide(new BigInteger("2")))+num.remainder(new BigInteger("2"));

        }else

            return "";

    }
}
