package LacoRepeticao;
import java.util.Scanner;

//Elabore  um  programa para  fazer  a tabuada  de  um  número  fornecido pelo usuário,variando de 0 a 12,emostre o resultado a cada iteração.

public class B {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int numero;
        System.out.print("Digite um número inteiro para descobrir sua tabuada: ");
        numero = sc.nextInt();

        for (int i = 0; i <= 12; i++){
            System.out.println(numero + " X " + i + " = " + numero * i);
        }
        sc.close();
    }
}
