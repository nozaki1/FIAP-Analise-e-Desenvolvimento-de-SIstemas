package Strings;
import java.util.Scanner;
//Algoritmo de cálculo dos dígitos de controle do CPF (últimos 2 digitos)

public class D {
    public static void main(String[] args) {
        int cpf[] = new int[11];
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 9; i++){
            System.out.print("Digite um número inteiro: ");
            cpf[i] += sc.nextInt();
        }
        sc.close();

        // cálculo do 11 número do CPF
        int soma = 0;
        int multiplicador = 10;
        for (int i = 0; i < 9; i++){
            soma += cpf[i]*multiplicador;
            multiplicador--;
        }

        int resto = soma % 11;
        if (resto <=1){
            cpf[9] = 0;
        }else{
            cpf[9] = 11 - resto;
        }

        //cálculo do 12 número do CPF
        soma = 0;
        multiplicador = 11;
        for (int i = 0; i < 10; i++) {
            soma += cpf[i] * multiplicador;
            multiplicador--;
        }

        resto = soma % 11;
        if(resto <= 1){
            cpf[10] = 0;
        }else{
            cpf[10] = 11 - resto;
        }

        System.out.println("O número do CPF completo é:");
        for (int num: cpf){
            System.out.print(num);
        }
    }
}

