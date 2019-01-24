import javax.swing.*;
import java.awt.*;

public class Main {

    public static final int X = 751;

    public static void main(String[] args) {
        int[] primes = generatePrimes(X);
        new Frame(X, primes);

    }
    private static int[] generatePrimes(int x){
        int[] primes = new int[x * x + 1];

        for(int i = 0; i < primes.length; i++){
            primes[i] = i;
        }
        for(int i = 2; i < primes.length; i++){
            if(primes[i] != 0){
                for(int j = 2; j * i < primes.length; j++){
                    primes[j * i] = 0;
                }
            }
        }
        return primes;
    }
}



class Frame extends JFrame{

    class Panel extends JPanel{
        private int primes[];
        private int X;
        public Panel(int primes[], int x){
            this.primes = primes;
            this.X = x;
        }
        public void paintComponent(Graphics g){

            g.setColor(Color.black);

            int x = X / 2;
            int y = x;
            int dir = 0;
            // 0 - right
            // 1 - up
            // 2 - left
            // 3 - down

            int stage = 1;
            int curstage = 1;
            int c = 0;

            for(int i = 0; i < X * X; i++){
                switch(dir){
                    case 0:{
                        x++;
                        break;
                    }
                    case 1: {
                        y--;
                        break;
                    }
                    case 2:{
                        x--;
                        break;
                    }
                    case 3:{
                        y++;
                        break;
                    }
                }
                if(--curstage == 0){
                    dir = (dir + 1) % 4;
                    if(c == 1){
                        c = 0;
                        stage++;
                    }else{
                        c = 1;
                    }

                    curstage = stage;
                }
                if(primes[i] != 0){
                    g.fillRect(x, y, 1, 1);
                }
            }
        }
    }
    public Frame(int x, int primes[]){


        getContentPane().add(new Panel(primes, x));
        setTitle("Ulam spiral");
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(x, x + 20);
        setLocationRelativeTo(null);
        setVisible(true);

    }

}