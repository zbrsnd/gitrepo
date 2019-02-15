/*
 * cezar.cpp
 */


#include <iostream>
#include <string.h>
using namespace std;

#define MAKS 100



void szyfruj(int klucz, char tekst[]) {
    klucz = klucz % 26;
    int kod = 0;
    int i = 0;
    while (tekst[i] != '\0') {
        kod = (int)tekst[i] + klucz;
        if (tekst[i] == ' ') {
            kod -= klucz;
        }
        else if (kod > 122) {
            kod  =- 26;
        }
        cout << (char)(kod);
        tekst[i] = (char)(kod);
        i++;
    }
                
      
     //~for(int i = 0; i < ilosc ; i++) {
        //~cout << tekst[i];
        //~kod = (int)tekst[i+klucz];
        //~cout << kod;
        //~}
                
}
    



int main(int argc, char **argv)
{
    char tekst[MAKS];
    cout << "Podaj tekst ułożony z małych liter:\n" << endl;
    cin.getline(tekst, MAKS);
    //~int ilosc = strlen(tekst);                                                                    
	int klucz;
    cout << "Podaj klucz" << endl;
    cin >> klucz;
    szyfruj(klucz, tekst);
	return 0;
}

