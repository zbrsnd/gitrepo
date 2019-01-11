#include <iostream>
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


void sort_insert(int tab[], int n) {
    int i, j, tmp;
    for (i = 1; i < n; i++) {
        tmp = tab[i];
        j = i - 1;
        while (j >= 0 && tab[j] > tmp) {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
}


int szukaj_lin(int tab[], int n, int el_szuk){

    for (int i = 0; i < n; i++)
        if (tab[i] == el_szuk)
            return i;
    return -1;
}
 // dziel i zwyciężaj

int szukaj_bin_lin(int tab[], int n, int el_szuk){
    int poczatek, koniec, srodek;
    poczatek = 0;
    koniec = n - 1;

    while(poczatek <= koniec){
        srodek = (poczatek + koniec) / 2;
        if (tab[srodek] == el_szuk){
            return srodek;
        } 

        else if(el_szuk < tab[srodek])
            koniec = srodek - 1;
        else poczatek = srodek + 1;
    }
    return -1;

}

int szukaj_bin_rek(int tab[], int el_szuk, int poczatek, int koniec) {
    
    if (poczatek <= koniec) {
        int srodek = (poczatek + koniec) / 2;
        if (tab[srodek] == el_szuk) return srodek;
        if (el_szuk < tab[srodek]) 
            return szukaj_bin_rek(tab, el_szuk, poczatek, srodek-1);
        else 
            return szukaj_bin_rek(tab, el_szuk, srodek+1, koniec);
    
        
        }
    return -1;
    }
    


int main(int argc, char **argv)
{
    int n = 20;
    int tab[n];
    wypelnij_los(tab, n);
    sort_insert(tab, n);
    drukuj(tab, n);
    int el_szuk = 0;
    cout << "Podaj liczbę: ";
    cin >> el_szuk;
	int index = 0;
    //~index = szukaj_bin_rek(tab, el_szuk, 0, n-1);
    index = szukaj_bin_lin(tab, n, el_szuk);
    if(index >= 0)cout<<"Znaleziono: " << index << endl;
    else 
        cout << "Nie znaleziono";

    //~if (index != -1)
        //~cout << "Znaleziono";
    //~else     
        //~cout << "Nie znaleziono";

    sort_insert(tab, n);
    szukaj_bin_lin(tab, n, el_szuk);

    return 0;
}

