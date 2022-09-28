package Strings;

public class A {
    public static void main(String[] args) {
        String bananada = "BANANADA";

        //Imprimir ANA
        System.out.println(bananada.substring(1, 4));

        //Imprimir BANDA
        String ban = bananada.substring(0, 3);
        String da = bananada.substring(6);
        System.out.println(ban + da);

        //Indicar as posições de todos os 'A's existentes na palavra BANANADA
        int index = bananada.indexOf("A");
        while (index >= 0){
            System.out.println(index);
            index = bananada.indexOf("A", index + 1);
        }
    }
}
