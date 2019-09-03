

#include <iostream>
using namespace std;

int wartosc_rek(int k)
{
    if (k==1)
    
        return 1;
        
    else
    
    return wartosc_rek(k-1)+(2*k)+(k-2);

}

int main(int argc, char **argv)
{
    
    int z;
    
    cout << "Podaj numer wyrazu ciągu: ";
    
    cin >> z;
    
    cout << "Wartość tego wyrazu: " << wartosc_rek(z);

    return 0;

}
