

#include <iostream>
using namespace std ; 

int zlicz_dzielnik(int y)
{
    int dziel = 0;
    for(int i=1; i<=y;i++)
    {
        if(y%i == 0)
        {
            dziel++;
        }
    }
    return dziel;
}

int main(int argc, char **argv)
{
	int x = 0 ;
    cout << "Podaj liczbe : " ;
    cin >> x ;
    
    cout << "Ilość dzielników liczby " << x << " jest równa : " << zlicz_dzielnik(x) ;
    
    
    
	return 0;
}

