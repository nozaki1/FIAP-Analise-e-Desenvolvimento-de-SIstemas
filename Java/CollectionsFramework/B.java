package CollectionsFramework;
import java.util.HashSet;
import java.util.Set;
// Escreva  uma  lista  para  o  armazenamento  de  Strings  e  exemplifique a utilização dos métodos da interfaceSet

public class B {
    public static void main(String[] args) {
        Set<String> set = new HashSet<String>();
        set.add("Ferrari");
        set.add("Aston Martin");
        set.add("Porsche");
        set.add("Mercedes");
        set.add("Porsche");
        set.add("Aston Martin");
        System.out.println(set);
        System.out.println(set.isEmpty());
    }
}
