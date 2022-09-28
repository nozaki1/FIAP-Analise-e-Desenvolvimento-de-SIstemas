package LacoRepeticao;

//Elabore  um  programa para  fazer  a tabuada  de  um  número  fornecido pelo usuário,variando de 0 a 12,emostre o resultado a cada iteração.

public class C {
    public static void main(String[] args) {
        int anterior = 0;
        int atual = 1;
        int proximo;
        System.out.println(atual);
        for (int i = 0; i < 30; i++){
            proximo = atual + anterior;
            System.out.println(proximo);
            anterior = atual;
            atual = proximo;
        }
    }
}
