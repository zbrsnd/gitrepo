/*
 * znaki.cpp
 * 
 * Copyright 2018  <>
 * 
*/

#include <iostream>
using namespace std;


void zamien_znaki(char tb[], int roz) {
    for (int i = 0; i < roz; i++) {
        //zamień małe znaki na duże
        kod ascii 'a' = 97
        kod ascii 'A' = 65
        97 - 65 = 32
        (char)(kod_ascii - 32)
        
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

int main(int argc, char **argv)
{
	
    const int rozmiar = 20;
    char znaki[rozmiar];
    cin.getline(znaki, rozmiar);
    licz_znaki(znaki, cin.gcount());
	return 0;
}

