


#include <iostream>
using namespace std;

int iloczyn_it(int a , int iloczyn = 1)
{
    int n;
    cout << "Podaj ile liczb : " << endl ;
    cin >> n;
    
    for (int i=1 ; i < n + 1; i++)
    {
        cout<<"Podaj liczbę:  " <<endl ;
        cin >> a; 
        iloczyn *= a;
    }
    return iloczyn ;
}
int main(int argc, char **argv)
{
	
    int a = 0 ;
    int iloczyn = 1;
    
    cout << iloczyn_it(a, iloczyn);
    
	return 0;
}
