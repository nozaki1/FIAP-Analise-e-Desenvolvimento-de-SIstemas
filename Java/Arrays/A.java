package Arrays;
import java.util.Scanner;

//Escreva  um  programa  para  preencher  uma  matriz  unidimensional  (vetor) com 15 posições de números inteirose, em seguida,apresente os elementos.

public class A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numeros = new int[15];
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Digite um número:");
            numeros[i] = sc.nextInt();
        }
        sc.close();
        System.out.println("Os números digitados foram:");
        for (int num : numeros) {
            System.out.println(num);
        }
    }
}