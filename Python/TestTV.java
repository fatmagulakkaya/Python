/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Hafta4;

/**
 *
 * @author ceyda
 */
public class TestTV {
    public static void main(String[] args) {
        TV tv1=new TV();
        tv1.ac();
        tv1.kanaliAyarla(30);
        tv1.sesiAyarla(4);
        
        
        TV tv2=new TV();
        tv2.ac();
        tv2.kanaliAyarla(15);
        tv2.sesiAyarla(7);
        
        //tv2.kapat();
        tv2.kanalYukari();
        tv2.kanalYukari();
        tv2.sesYukari();
        
        System.out.println("1. TV'nin kanali: "+tv1.kanal+" sesi: "+tv1.sesSeviyesi);
        System.out.println("2. TV'nin kanali: "+tv2.kanal+" sesi: "+tv2.sesSeviyesi);
    }
}
