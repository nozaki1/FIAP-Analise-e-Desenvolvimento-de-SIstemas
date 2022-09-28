package CollectionsFramework;
import java.util.HashMap;
import java.util.Map;
//Escreva  uma  lista  para  o  armazenamento  de  Strings  e  exemplifique a utilização dos métodos da interface Map

public class C {
    public static void main(String[] args) {
        Map<String, String> mapa = new HashMap<String, String>();
        mapa.put("SF90","Scuderia Ferrari");
        mapa.put("M3", "BMW");
        mapa.put("Aventador", "Lamborghini");

        //só pode existir uma chave "SF90"
        mapa.put("SF90", "Ferrari");
        //podem existir infinitos valores "Ferrari" desde que a chave seja diferente
        mapa.put("296 GTB", "Ferrari");

        System.out.println(mapa);
    }
}
