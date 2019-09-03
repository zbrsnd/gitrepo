


#include <iostream>
using namespace std ; 

void kwota(int x)
{
    int bank = 0 ;
    int wplata = 0 ;
    
    for( int i = 0 ; i <= x ; i++ )
    {
        bank = bank + wplata ;
        wplata += 10 ;
    }
        cout << "Stan konta po  " << x << " miesiącach: " << bank << endl ;
        cout <<"Kwota ostatniej wpłaty : " << 100 + (x*10);
}

int main(int argc, char **argv)
{
    int x = 0 ;
	
    do
    {
        cout <<"Podaj ilość miesięcy : " ;
        cin >> x ;
    }
    while (x < 0) ;
    
    kwota(x) ;
    
	return 0;
}

