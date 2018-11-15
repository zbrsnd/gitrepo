/*
 * palindromy.cpp
 */


#include <iostream>
#include <string.h>

using namespace std;

//~bool - funcja logiczna - prwdal lub fałsz
bool palindrom(char wyraz[], int ilosc) {
    bool zLogiczna = true;
    for(int i = 0; i < (ilosc / 2); i++) {
            if(wyraz[i] != wyraz[ilosc - (i+1)]){
                    zLogiczna = false;
                }
        }
    return zLogiczna;
    }

int main(int argc, char **argv)
{
    int rozmiar = 20;
    char wyraz[rozmiar];
    cout << "Podaj wyraz: ";
    cin.getline(wyraz, rozmiar);
    //~cout << cin.gcount() << endl;
    int ilosc = strlen(wyraz);
    cout << palindrom(wyraz, ilosc) << endl;
    return 0;
}

