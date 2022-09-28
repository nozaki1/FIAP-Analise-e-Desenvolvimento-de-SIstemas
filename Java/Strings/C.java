package Strings;
import java.util.Scanner;

//Dado um texto contendo somente palavras separadas por caracteres em branco, terminando em ponto final, escreva apenas as palavras distintas existentes no texto.

public class C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String fraseFinal = "";
        System.out.print("Digite uma frase: ");
        String frase = sc.nextLine();
        sc.close();

        String palavras [] = frase.split(" ");
        for (String palavra: palavras){
            if (!fraseFinal.contains(palavra)){
                fraseFinal += palavra + " ";
            }
        }
        System.out.println(fraseFinal);
    }
}
