/*
 * cezar.cpp
 */


#include <iostream>
#include <string.h>
using namespace std;

#define MAKS 100



void szyfruj(int klucz, char tekst[], int ilosc, int kod) {
    klucz = klucz % 26;
    for(int i = 0; i < ilosc ; i++) {
        cout << tekst[i];
        tekst[i] = tekst[i+1];
        kod = (int)tekst[i];
        cout << kod;
        
        }
    
}


int main(int argc, char **argv)
{
    char tekst[MAKS];
    cout << "Podaj tekst ułożony z małych liter:\n" << endl;
    cin.getline(tekst, MAKS);
    int ilosc = strlen(tekst);                                                                    
	int klucz;
    int kod;
    cout << "Podaj klucz" << endl;
    cin >> klucz;
    szyfruj(klucz, tekst, ilosc, kod);
	return 0;
}

