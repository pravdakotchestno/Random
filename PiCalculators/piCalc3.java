import java.math.BigDecimal;
import java.math.MathContext;

public class Main {
    //simple pi number calculator using Nilakantha formula
    static BigDecimal bd=new BigDecimal("3");
    public static final int accuracy = 20000000;
    public static void main(String[] args) {
        for(long i=2;i<accuracy;i+=4){

            bd=bd.add(BigDecimal.valueOf(4).divide(BigDecimal.valueOf(i*(i+1)*(i+2)),MathContext.DECIMAL64));
            bd=bd.subtract(BigDecimal.valueOf(4).divide(BigDecimal.valueOf((i+2)*(i+3)*(i+4)),MathContext.DECIMAL64));
            System.out.printf("%3.2f %%\n",((float)i)/accuracy*100);

        }
        System.out.println(bd.round(MathContext.DECIMAL64));
    }
}
