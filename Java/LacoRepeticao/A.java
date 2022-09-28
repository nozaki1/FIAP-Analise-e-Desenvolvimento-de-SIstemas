package LacoRepeticao;
import java.util.Scanner;

//Elabore um programa para ler 20 valores inteiros fornecidos pelo usuário e calcular a soma deles. Apresente o resultado ao final.

public class A {

    public static void main(String[] args) throws Exception {
     Scanner sc = new Scanner(System.in);
    int soma = 0;

    for (int i = 0; i < 20; i++) {
        System.out.print("Digite um número: ");
        soma += sc.nextInt();
    }
       sc.close();
    System.out.println("A soma total é " + soma);
  }

}
