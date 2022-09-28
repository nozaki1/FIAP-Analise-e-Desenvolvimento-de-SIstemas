package Strings;
import java.util.Scanner;

//Indique se uma expressão é palíndroma.

public class B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite a expressão a ser verificada: ");
        String palavra = sc.nextLine();
        String palavraReversa = "";

        for (int i = palavra.length() - 1; i >= 0 ; i-- ){
            palavraReversa += palavra.charAt(i);
        }
        sc.close();
        if (palavraReversa.equals(palavra)){
            System.out.println("É um palíndromo!");
        }else{
            System.out.println("Não é um palíndromo.");
        }
    }
}
