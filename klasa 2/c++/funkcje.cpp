#include <iostream>

using namespace std;

int dodaj(int a, int b)
{
    return a + b;   
}

int odejmij(int a, int b)
{
    return a - b;   
}

int pomnoz(int a, int b)
{
    return a * b;   
}

float podziel(float a, float b)
{
    return a / b;   
}




int main(int argc, char **argv)
{
	
    float a, b; //deklaracja zmiennej
    a = b = 0; //inicjacja zmiennej
    
    
    cout << "Podaj 1. liczbę: ";
    cin >> a; //std:: <- standardowa biblioteka
    cout << a << endl;
    
    cout << "Podaj 2. liczbę: ";
    cin >> b; 
    cout << b << endl;
    
    
    
    cout << "Suma: " << dodaj(a, b) << endl;
    cout << "Różnica: " << odejmij(a, b) << endl;
    cout << "Iloczyn: " << pomnoz(a, b) << endl;
    cout << "Iloraz: " << podziel(a, b) << endl;
        
	return 0;
}

