/*
 * silnia.cpp
 */


#include <iostream>
using namespace std;


int silnia_it(int a) {
    
    int wynik = 1;
    for (int i = 1; i < a+1; i++) {
        wynik = a * (a-1);
        }
    return wynik;
    }

int silnia_rek(int a){
    
    if (a == 1)
        return 1;
    return a * silnia_rek(a-1);
    }

int main(int argc, char **argv)
{
	int a;
    cout << "Podaj liczbę: " << endl;
    cin >> a;
    cout << "Silnia dla: " << a << " wynosi: " << silnia_it(a) << endl;
    cout << "Silnia dla: " << a << " wynosi: " << silnia_rek(a) << endl;
	return 0;
}

