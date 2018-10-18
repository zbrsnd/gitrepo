/*
 * tabliczka.cpp
 */ 



#include <iostream>
#include <iomanip> // <-- import bibloteki manipulation (manipulowanie wejsciem wyjsciem)


using namespace std;

void tabliczka(int x, int y) {// <-- void - funkcja, ktora niczego nie zwraca <zadnej wartosci etc.>   
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= y; j++) {
            cout << setw(4) << i*j << " "; //setw(4) <<- set width, ustaw szerokosc pola
        }
        cout << endl;
    }
    ;
}



int main(int argc, char **argv)
{
	int a, b; //deklaracja
    a = b = 0; //inicjacja
    // int a = 0 (definicja [deklaracja + inicjacja])
    
    cout << "Podaj zakres pierwszy: ";
    cin >> a;
    cout << "Podaj zakres drugi: ";
    cin >> b;
    tabliczka(a, b);
    
	return 0;
}

