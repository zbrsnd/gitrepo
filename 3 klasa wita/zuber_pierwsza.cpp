/*
 * zuber_pierwsza.cpp
 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    int n;
    cout << "Podaj liczbę: ";
    cin >> n;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            cout << "Liczba złożona" << endl;
            return 0;
            }
    cout << "Liczba pierwsza" << endl;
        }   
	
	return 0;
}

