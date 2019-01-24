import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import javax.imageio.ImageIO;
import javax.swing.JFrame;
import javax.swing.JPanel;


public class Zmeika {

    //переменная, содержащая в себе true, если игра еще идет
    static boolean isGameRunning=true;

    //главное игровое поле

    //0     ничего
    //2     snake
    //3     orange
    static int[][] GameMap=new int[50][50];
    
    //текущий счет
    static int score=0;
    
    //переменная с текущим направлением
    //1 left
    //2 right
    //3 up
    //4 down
    static int napr=2;

    //ArrayList, содержащий в себе предыдущие ходы (нужно для перезаписи tailX и tailY)
    //лучше заменить Queue или что-то в этом роде
    static ArrayList<int[]> moves=new ArrayList<>();

    //флаг, отвечающий за то, чтобы мы не смогли сменить значение napr больше, чем 1 раз за цикл
    static boolean areYouAbleToChangeNapr = true;
    
    //рандом генератор
    static Random rand;

    //координаты апельсинки
    static int orangeX=10;
    static int orangeY=10;
    

    //текущий цвет змеи (выбирается рандомно при каждом перезаходе в игру)
    static int colornum;
    
    //координаты головы змеи
    static int headX=3;
    static int headY=3;
    
    //координаты конца змеи 
    static int tailX=3;
    static int tailY=3;
    

    //метод main 
    public static void main(String[] args) {
        //создание окна
        GameFrame gameFrame = new GameFrame();

        //инициализация рандом генератора
        rand=new Random();

        //выбор текущего цвета змеи
        colornum=rand.nextInt(GamePanel.colors.length);
        
        //заполнение поля нулями (возможно это не нужно)
        fillMap();

        //добавление конца змеи в moves
        moves.add(new int[]{3,3});
        

        //добавление первого апельсина на поле
        GameMap[orangeY][orangeX]=3;

        //текущий ход
        int currentMove=0;

        //главный игровой цикл
        while(isGameRunning){
            
            //если змея съела апельсин
            if(headX==orangeX&&headY==orangeY){

                //прибавление очков
                score++;

                //поиск координат для нового апельсина
                do{
                    orangeX=rand.nextInt(50);
                    orangeY=rand.nextInt(50);

                }while(GameMap[orangeY][orangeX]!=0&&GameMap[orangeY+1][orangeX]!=2&&GameMap[orangeY-1][orangeX]!=2&&GameMap[orangeY][orangeX-1]!=2&&GameMap[orangeY][orangeX+1]!=2);


                //спавн нового апельсина
                GameMap[orangeY][orangeX]=3;

            }else{

                //если же змея не съела апельсин, то тогда перезаписываем координаты хвоста

                //currentMove прибавляется и координаты хвоста изменяются только в случае, если апельсин не был съеден
                //при съедании апельсина координаты хвоста не изменяются, а значит и хвост становится дальше от головы,
                // а значит змейка как бы растет
                tailY=moves.get(currentMove)[0];
                tailX=moves.get(currentMove)[1];
                currentMove++;
            }

            

            //штука, которая заставляет поток засыпать 10 раз в секунду (можно при повышении сложности уменьшать значение, передаваемое в .sleep() )
            try{
                Thread.sleep(100);
            }catch(Exception e){ }
            
            //перезапись headX и headY в зависимости от переменной napr
            try{

                //если координаты, на которые пытается переползти змея, равны 2 (тоесть хвосту змеи), то тогда вызывается gameOver()
                switch(napr){

                    case 1:{
                        if(GameMap[headY][headX-1]==2){
                            GameOver();
                        }else
                            headX--;
                        
                        break;
                    }
                    case 2:{
                        if(GameMap[headY][headX+1]==2){
                            GameOver();
                        }else
                            headX++;
                        
                        break;
                    }
                    case 3:{
                        if(GameMap[headY-1][headX]==2){
                            GameOver();
                        }else
                            headY--;
                        
                        break;
                    }
                    case 4:{
                        if(GameMap[headY+1][headX]==2){
                            GameOver();
                        }else
                            headY++;
                        
                        break;
                    }
                }
                //также gameOver вызывается при выходе за пределы экрана (тоесть при IndexOutOfBoundsException)
            }catch(IndexOutOfBoundsException e){

                GameOver();
                
            }
                
                
                    
                    
                
            //разрешение на смену направления во время следующего цикла
            areYouAbleToChangeNapr=true;

            //удаление двойки (значения, обозначающего клетку со змеей) из поля на месте хвоста
            GameMap[tailY][tailX]=0;

            //добавление двойки (клетки со змеей) по координатам головы змеи
            GameMap[headY][headX]=2;

            //перерисовка панели в соответствии с новым полем
            GameFrame.panel.Repaint(GameMap);

            //добавление текущей позиции головы в moves
            moves.add(new int[]{headY,headX});
            
            
        }
        
        
    }

    //метод, заполняющий карту нулями (я его возможно теперь удалю, т.к. он, возможно, не нужен)
    public static void fillMap(){
        for(int[] array:GameMap){
            for(int cell:array){
                cell=0;
            }
        }
    }

    //метод gameOver(), просто присваивающий isGameRunning false
    public static void GameOver(){
        isGameRunning=false;
        
    }
        
}
    

//класс окна
class GameFrame extends JFrame{

    //панель, на которой будет отрисовываться поле

    public static GamePanel panel;
    GameFrame(){

        //инициализация панели
        panel=new GamePanel();



        //унастройка отображения окна

        this.setSize(500,522);
        this.setLocationRelativeTo(null);
        this.add(panel);
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setVisible(true);
        panel.setFocusable(true);

        //добавление слушателя кнопок на панель
        panel.addKeyListener(new KeyListener() {
                
            public void keyPressed(KeyEvent e) {
                //если вы можете сменить направление
                if(Zmeika.areYouAbleToChangeNapr){
                    //изменение направления в зависимости от нажатой кнопки
                    switch(e.getKeyCode()){
                    
                        case(KeyEvent.VK_LEFT):{
                            if(Zmeika.napr!=2){
                                Zmeika.napr=1;
                            }
                            break;
                        }
                        case(KeyEvent.VK_RIGHT):{
                            if(Zmeika.napr!=1){
                                Zmeika.napr=2;
                            }
                            break;
                        }
                        case(KeyEvent.VK_UP):{
                            if(Zmeika.napr!=4){
                                Zmeika.napr=3;
                            }
                            break;
                        }
                        case(KeyEvent.VK_DOWN):{
                            if(Zmeika.napr!=3){
                                Zmeika.napr=4;
                            }
                            break;
                        }
                    
                    }

                }
                //теперь мы больше не можем сменить направление
                Zmeika.areYouAbleToChangeNapr=false;
            }
            
            //методы слушателя, которые нам переопределять незачем
            public void keyReleased(KeyEvent e) {
                 
            }
 
            public void keyTyped(KeyEvent e) {
                
            }
     
        });
        
    }
   
}

//класс GamePanel
class GamePanel extends JPanel{
    //картинка с надписью GameOver
    public Image img;

    //поле, которое отрисовывается на экране
    int[][] GameMap=new int[50][50];

    //все возможные цвета змеи
    public static Color colors[]={Color.BLUE,Color.CYAN,Color.GREEN,Color.LIGHT_GRAY,Color.MAGENTA,Color.ORANGE,Color.RED};
    

    //метод, нужный для перерисовки новоро поля на экране
    public void Repaint(int[][] Gamemap){
        GameMap=Gamemap;
        repaint();
    }

    //конструктор класса GamePanel
    GamePanel(){
        
        //попытка загрузить картинку с надписью GameOver
        try {
            img=ImageIO.read(new File("src/gameover.png"));
        } catch (IOException ex) {
           System.out.println("IOException");
        }
        //расположение окна на координатах 0 0 с размерами 500 на 500
        this.setBounds(0,0,500,500);
    }
    


    //перерисовка панели
    public void paintComponent(Graphics gr){
        
        //координаты отрисовываемого прямоугольника (квадрата)
        int x=0;
        int y=0;
        
        if(Zmeika.isGameRunning){
            //отрисовка поля в случае если игра еще не закончена

            for(int[] array:GameMap){
            
                for(int cell:array){

                    //выбор текущего цвета в зависимости от значения ячейки в GameMap
                    switch(cell){
                        //отрисовка пустого места белым цветом
                        case 0:{
                            gr.setColor(Color.WHITE);
                            break;
                        }
                        //отрисовка змеи
                        case 2:{
                            //отрисовка происходит в зависимости от значения colornum, который выбирается рандомно каждый раз при запуске
                            // (типо змея при каждой игре своего цвета)
                            gr.setColor(colors[Zmeika.colornum]);
                            break;
                        }
                        //отрисовка апельсинки желтым цветом
                        case 3:{
                            gr.setColor(Color.YELLOW);
                            break;
                        }
                    
                    }
                    //отрисовка квадрата с выбраным цветом и 
                    gr.fillRect(x,y,10,10);


                    x+=10;
                }

                x=0;
                y+=10;
            }

            //отрисовка текущего счета на экран
            gr.setColor(Color.BLACK);
            gr.drawString("Score: "+Zmeika.score, 10, 20);
        }else{
            //в случае, если игра закончена, будет отрисовываться картинка с надписью GameOver
            gr.drawImage(img,0,0, this);
        }

    }
}
