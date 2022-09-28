package LacoRepeticao;
import java.util.Scanner;

// Elabore um programa que leia o nome e o salário de n pessoas, o usuário deverá informar se deseja continuar a iteração. Ao final,apresente a quantidade de pessoas informadas e a média entre os salários.

public class D {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int qtd_pessoas = 0;
        double total_salario = 0;
        String resposta;


        do{
            System.out.print("Digite o nome de um funcionário: ");
            sc.nextLine();
            qtd_pessoas++;
            System.out.print("Informe o salário desse funcionário(use vírgula para decimais): ");
            total_salario += sc.nextDouble();
            System.out.println("Deseja inserir mais um funcionário? (S/N)");
            resposta = sc.next();
            //consumir a "sujeira" no input
            sc.nextLine();
        }while(resposta.equals("S"));

        sc.close();
        System.out.println("Você inseriu " + qtd_pessoas + " funcionários.");
        System.out.println("A média dos salários inseridos é R$" + total_salario / qtd_pessoas);
    }
}
