/*
 * potega_rek.cpp
 */


#include <iostream>
using namespace std;


int potega_it(int a, int n) {
    
    int wynik = 1;
    
    for (int i = 0; i < n; i++) {
        wynik = wynik * a;
        }
    return wynik;
    }
    
int potega_rek(int a, int n) {
    
    if(n == 0) 
        return 1;
    return a * potega_rek(a, n-1);
    }
    


int main(int argc, char **argv)
{
	int a, n;
    cout << "Podaj podstawę i wykładnik potęgi: " << endl;
    cin >> a >> n;
    cout << "Potęga: " << potega_it(a,n) << endl;
    cout << "Potęga: " << potega_rek(a,n) << endl;
	return 0;
}

