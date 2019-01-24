import java.math.BigDecimal;
import java.math.MathContext;

public class Main {
    //simple pi number calculator using Wallis product
    static BigDecimal bd=new BigDecimal("1");
    public static final int accuracy = 200000;
    public static void main(String[] args) {
        for(int i=2;i<accuracy;i+=2){
            bd=bd.multiply(BigDecimal.valueOf(i).divide(BigDecimal.valueOf(i-1),MathContext.DECIMAL64));
            bd=bd.multiply(BigDecimal.valueOf(i).divide(BigDecimal.valueOf(i+1),MathContext.DECIMAL64));
            System.out.printf("%3.2f %%\n",((float)i)/accuracy*100);
        }
        bd=bd.multiply(BigDecimal.valueOf(2));
        System.out.println(bd.round(MathContext.DECIMAL64));
    }
}
