#include <iostream>
#include <cstdlib>
#include <time.h>

using namespace std;


void wypelnij_los(int tab[], int n) {
    srand(time(NULL));//inicjacja generatora liczb pseudolosowych
    for(int i = 0; i < n; i++) {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int n) {
    for(int i = 0; i < n; i++) {
        cout << tab[i] << " ";
    }
}

void zamien(int &a, int &b){
    int tmp = a;
    a = b;
    b = tmp;
}

void zamien2(int tab[], int i){
    int tmp = tab[i];
    tab[i] = tab[i+1];
    tab[i+1] = tmp;
    }
    
void sort_bubble(int tab[], int n){
    cout << "\nSortowanie bąbelkowe\n";
    int licznik = 0;
    for (int j = n - 1; j > 0; j--) {
        for(int i = 0; i < j; i++) {
            licznik++;
            if (tab[i] < tab[i+1])
                zamien(tab[i], tab[i+1]);
        }
        cout << tab[j] << " ";
    }
    cout << "\nPowtórzeń: " << licznik << endl;
}

void sort_insert(int tab[], int n) {
    cout << "\nSortowanie przez wstawianie\n";
    int i, j, tmp;
    int licznik = 0;
    for (i = 1; i < n; i++) {
        tmp = tab[i];
        j = i - 1;
        licznik++;
        while (j >= 0 && tab[j] > tmp) {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
    cout << "\nPowtórzeń: " << licznik << endl;
}


void sort_selection(int tab[], int n){
    int i, j, k;
    for(i = 0; i < n - 1; i++){
        k = i; // indeks najmniejszego elementu
        for(j = k + 1; j < n; j++){
                if(tab[j] < tab[k]){
                    k = j;
                }
            }
        zamien(tab[i], tab[k]);
        }
    }

int main(int argc, char **argv)
{
	int n = 20;
    int tab[n];
    wypelnij_los(tab, n);
    drukuj(tab, n);
    //int a = 10;
    //int b = 20;
    //zamien(a, b);
    //cout << a << " "<< b;
    cout << endl;
    //~sort_bubble(tab, n);
    sort_insert(tab, n);
    //~sort_selection(tab, n);
    cout << endl;
    drukuj(tab, n);
    
	return 0;
}
