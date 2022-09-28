package Arrays;

import java.util.Scanner;

// Altere  o  programa  anterior  para  registrar  as  temperaturas  de  cada  dia  do mês, neste caso,utilize uma matriz com 30 linhas e 24 colunas. Ao final,verifique qual foi a maior temperatura, a menor temperatura e a temperatura média.

public class C {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float temperaturas[][] = new float[30][24];
        float temperaturaMediaTotal = 0;
        float temperaturaMediaDia = 0;
        float temperaturaTotalDia = 0;

        for (int dia = 0; dia < temperaturas.length; dia++) {
            for (int hora = 0; hora < temperaturas[dia].length; hora++){
                System.out.print("Digite a temperatura da hora atual no dia " + (dia+1) + ": ");
                temperaturas[dia][hora] = sc.nextFloat();
                temperaturaTotalDia += temperaturas[dia][hora];
            }
            temperaturaMediaDia = temperaturaTotalDia / 24;
            temperaturaMediaTotal += temperaturaMediaDia;
            temperaturaMediaDia = 0;
            temperaturaTotalDia = 0;
        }
        sc.close();
        float temperaturaMediaMes = temperaturaMediaTotal / 30;
        System.out.println("A temperatura média no mês foi de: " + temperaturaMediaMes + " graus.");
    }
}
