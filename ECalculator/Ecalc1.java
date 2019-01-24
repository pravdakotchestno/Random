import java.math.BigDecimal;
import java.math.MathContext;

public class Main {
    //simple e number calculator
    static BigDecimal bd=new BigDecimal("1");
    public static final int accuracy = 200000;
    public static void main(String[] args) {
        bd=(bd.add(bd.divide(BigDecimal.valueOf(accuracy),MathContext.DECIMAL128))).pow(accuracy);

        System.out.println(bd.round(MathContext.DECIMAL128));
    }
}
