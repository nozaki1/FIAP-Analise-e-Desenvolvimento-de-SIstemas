package Arrays;
import java.util.Scanner;

//Escreva  um  programa  para  armazenar  em  uma  matriz  as  notas  das  5 disciplinas dos 20 alunos de uma turma.

public class D {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float notas[][] = new float[5][20];

        for (int disciplina = 0; disciplina < notas.length; disciplina++){
            for (int aluno = 0; aluno < notas[disciplina].length; aluno++){
                System.out.println("Digite a nota do aluno " + (aluno+1) + " na disciplina " + (disciplina+1) + ":");
                notas[disciplina][aluno] = sc.nextFloat();
            }
        }sc.close();
    }
}
