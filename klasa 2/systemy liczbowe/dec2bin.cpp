/*
 * dec2bin.cpp
 */


#include <iostream>
#include <cmath>
using namespace std;


// 127/podstawa wynik reszta r


int dec2any(int liczba, int podstawa, int tab[]) {
    int i = 0;
    do {
        tab[i] = liczba % podstawa;
        liczba = liczba / podstawa;
        i++;
        
        } while (liczba != 0);
        return i-1;
}



void any2dec(int tab[]) {
    
    int podstawa = 0;
    do {
        cout << "Podstawa <2;9>" << endl;
        cin >> podstawa;
        } while (podstawa < 2 || podstawa > 9);
        
    int ile = 0;
    cout << "Ile cyfr? "; cin >> ile >> endl;
    for (int i = 0; i < ile; i++)
        do {
            cout << "Podaj cyfrę (0-" << podstawa-1 << "): ";
            cin >> tab[i]
            } while (tab[i] < 0 || tab[i] > podstawa;
            
    //konwersja na sytem dziesiętny
    liczba10 = 0;
    for(int i = 0;; i < ile; i++) {
        tab[i] * liczba
        i++;
        liczba10++;
        }
    
    
    }
    
int main(int argc, char **argv)
{
	int tab[8];
    int liczba, podstawa;
    cout << "Podaj liczbę i podstawę systemu docelowego: " << endl;
    cin >> liczba >> podstawa;
    int i = dec2any(liczba, podstawa, tab);
    cout << "Wynik: ";
    while (i >= 0) {
        cout << tab[i];
        i--;
        }
    
    
	return 0;
}

