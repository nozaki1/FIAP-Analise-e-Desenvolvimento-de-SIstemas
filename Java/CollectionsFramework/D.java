package CollectionsFramework;
import java.util.ArrayList;
import java.util.List;
//Escreva  uma  lista  para  o  armazenamento  de  Strings  e  exemplifique  a utilização dos métodos da interface Generic.

public class D {
    public static void main(String[] args) {
        List<String> lista = new ArrayList<String>();
        lista.add("BMW");
        lista.add("Audi");
        lista.add("Mercedes");

        // tentar inserir elementos não-String causam erro de compilação:
        lista.add(3);
        lista.add(5.4);
        lista.add(false);

        System.out.println(lista);

    }
}
