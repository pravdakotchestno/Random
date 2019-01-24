import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;

public class Main {
    //simple e number calculator
    static BigDecimal bd=new BigDecimal("1");
    public static final int accuracy = 6000;
    public static void main(String[] args) {
        for(long i=1;i<accuracy;i++){

            bd=bd.add(BigDecimal.ONE.divide(new BigDecimal(fact(BigInteger.valueOf(i))), new MathContext(1280)));

        }

        String result=bd.round(new MathContext(1280)).toString();
        int i=0;//73
        for(char ch: result.toCharArray()){
            System.out.print(ch);
            i++;
            if(i==73) {
                System.out.print('\n');
                i=0;
            }
        }
    }

    static BigInteger fact(BigInteger bi){
        return(bi.toString().compareTo("1")<=0)?BigInteger.ONE:bi.multiply(fact(bi.subtract(BigInteger.ONE)));
    }
}

