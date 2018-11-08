/*
 * znaki.cpp
 * 
 * Copyright 2018  <>
 * 
*/

#include <iostream>
using namespace std;
#include <string.h>


void zamien_znaki(char tb[], int roz) {
    int i=0;
    while(tb[i]!='\0') {
        
        tb[i++]=(char)((int)tb[i]-32);
    }

    i=0;
    while(tb[i]!='\0') {
        cout<<tb[i++];
    }

}

void ascii(char tb[], int roz) {
    int kod = 0;
    for(int i = 0; i < roz; i++) {
        kod = (int)tb[i];
        if (kod > 64 && kod < 96) 
            cout << (char)(kod + 32) << " ";
        else if (kod > 96 && kod < 123)
            cout << (char)(kod - 32) << " ";
        else cout << tb[i] << " ";
        
        }
    }

void licz_znaki(char tb[], int roz) 
{
    //~for(int i=0; i < roz; i++) {
            //~cout << tb[i];
    //~} 
    
    int znak_kod = 0; // kod ASCII badanego znaku
    int cyfry, literyD, literyM, reszta;
    int i = 0;
    cyfry = literyD = literyM = reszta = 0;
    
    while (tb[i] != '\0') {
        znak_kod = (int)tb[i];
        if (znak_kod > 64 && znak_kod < 91)
            literyD++;
        else if (znak_kod > 96 && znak_kod < 123)
            literyM++;
        else if (znak_kod > 47 && znak_kod < 58)
            cyfry++;
        else
            reszta++;
        
        i++;
    }
    cout << "Liter dużych" << literyD << endl;
    cout << "Liter małych:" << literyM << endl;
    cout << "Cyfr:" << cyfry << endl;
    cout << "Pozostałych:" << reszta << endl;
}
int zlicz(char tb[], int roz) {
    int i = 0;
    while (tb[i] != '\0') i++;
    return i;
    
    }

void odwroc(char tb[], int roz){
    
    for (int i = roz-1; i >= 0; i--){
        cout << tb[i] << " ";
        }
    
    }

int main(int argc, char **argv)
{
	
    const int rozmiar = 20;
    char znaki[rozmiar];
    cin.getline(znaki, rozmiar);
    //~ licz_znaki(znaki, cin.gcount());
    //~int ilosc = cin.gcount();
    //~ilosc = zlicz(znaki);
    //~int ilosc = strlen(znaki);
    //~cout << ilosc;
    //~zamien_znaki(znaki,rozmiar);
    //~ascii(znaki, ilosc);
    odwroc(znaki, rozmiar);
	return 0;
}

