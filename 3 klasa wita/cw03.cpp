/*
 * cw03.cpp
 */


#include <iostream>
using namespace std;


void wypelnij(int a[], int n) {
    srand(time(NULL)); //inicjacja generatora liczb pseudolosowych
    for(int i=0; i < n; i++) {
        a[i] = rand() % 101;
    }
}

int main(int argc, char **argv)
{
	
    int n,x;
    cout << "Podaj liczbę elementów tablicy: " << endl;
    cin >> n;
    int a[n];
     wypelnij(a,n);
    
    int i = 0;
    if (i > n) return -1;
    for (i = 0; i < n; i++){
        if (a[i] = {x}) 
            return i;
    i += 1;
    }
    
    
	return 0;
}

