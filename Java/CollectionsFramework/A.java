package CollectionsFramework;

import java.util.ArrayList;
import java.util.List;
//Escreva uma lista para o armazenamento de Strings e exemplifique a utilização dos métodos da interface List

public class A {
    public static void main(String[] args) {
        List<String> lista = new ArrayList<String>();
        lista.add("Ferrari");
        lista.add("Mercedes");
        lista.add("Porsche");
        lista.add("Aston Martin");
        lista.set(3, "McLaren");
        lista.remove(1);
        lista.add("Porsche");
        System.out.println(lista);
    }
}
