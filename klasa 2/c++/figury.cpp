/*
 * figury.cpp
 */


#include <iostream>
using namespace std;

void prostokat2(a, b, znak) {
        
        for (i = 0; i < a; i++) {
            for (j = 0; j < b; j++) {
                if (j == 0 || j == b)
                cout << znak << endl
                else
                cout << " " << endl
                
            
            }
        
        }
    return 0
}

int main(int argc, char **argv)
{
    int a; //deklaracja
    a = 0;
    int b;
    b = 0 //inicjacja
    // int a = 0 (definicja [deklaracja + inicjacja])
    
    cout << "Podaj zakres pierwszy: ";
    cin >> a;
    cout << "Podaj zakres drugi: ";
    cin >> b;
    
    char znak;
    cout << "Podaj znak: ";
    cin >> znak;
    
    prostokat2(a, b, znak);
	return 0;
}

