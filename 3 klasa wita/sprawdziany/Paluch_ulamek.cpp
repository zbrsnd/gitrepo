

#include <iostream>
using namespace std;


int NWD(int x, int y)
{
    while (x>0)
    {
        x = x % y ;
        y = y - x ;
    }
    return y;
}



int main(int argc, char **argv)
{
	int licznik = 0 ;
    int mianownik = 0 ;
    
    cout << "Podaj pierwszą liczbe :" ;
    cin >> licznik ;
    cout << "Podaj drugą liczbe : " ;
    cin >> mianownik ;
    
    cout<<"Ułamek wynosi: "<<licznik/(NWD(licznik,mianownik)) << '/' <<mianownik/(NWD(licznik,mianownik))<<endl;
    
    
	return 0;
}

