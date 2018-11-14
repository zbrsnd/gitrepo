/*
 * palindromy.cpp
 */


#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(char w[], int ilosc) {
    
    bool pal = true;
    
    
    for (int i = 0; i <= ilosc/2; i++){
        
        if (w[i] == w[ilosc-(i+1)]); //instrukcja pusta
        else {
            
            pal = false;
            break;
        }
        
    }

return pal;

}

int main(int argc, char **argv)
{
	int roz = 20;
    char wyraz[20];
    cout << "Podaj wyraz:";
    cin.getline(wyraz,roz);
    //~cout << cin.gcount() << endl;
    int ilosc = strlen(wyraz);
    if (palindrom(wyraz, ilosc))
        cout << "Palindrom";
    else {
        cout << "To nie palindrom";
    }
    
	return 0;
}

