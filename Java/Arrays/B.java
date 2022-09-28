package Arrays;
import java.util.Scanner;

// Escreva umprograma para preencher uma matriz unidimensional (vetor) que deverá receber as temperaturas ao longo do dia. A medição precisa ser registrada a cada uma hora. Ao final,exiba a temperatura média do dia.

public class B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float temperaturas[] = new float[24];
        float temperaturaTotal = 0;
        for (int i = 0; i < temperaturas.length; i++){
            System.out.print("Digite a temperatura da hora atual: ");
            temperaturas[i] = sc.nextFloat();
            temperaturaTotal += temperaturas[i];
        }
        sc.close();
        float temperaturaMedia = temperaturaTotal / 24;
        System.out.println("A temperatura média do dia foi de " + temperaturaMedia + " graus.");
    }
}
