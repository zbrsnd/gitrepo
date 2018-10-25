#include <iostream>
#include <cstdlib>
using namespace std;



void minmax1() {
    char dalej = 't';
    int liczba = 0;
    int min, max;
    cout << "Podaj liczbę: ";
    cin >> liczba;
    min = max = liczba;
    while(dalej == 't') {
        cout << "Podaj liczbę: ";
        cin >> liczba;
        if (liczba < min)
            min = liczba;
        if (liczba > max)
            max = liczba;
        cout << "Następna? (t/n) ";
        cin >> dalej;
    }
    cout << "Najmniejsza: " << min << endl;
    cout << "Największa: " << max << endl;
}

void wypelnij(int tab[], int roz) {

    cout << "Podaj " << roz << " liczb: " << endl;
    for(int i = 0; i < roz; i++) {
        cin >> tab[i];
    }
}

void drukuj(int tab[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout << tab[i] << " ";
    }
}

void wypelnij_los(int tab[], int roz) {
    srand(time(NULL)); //inicjacja generatora liczb pseudolosowych

    for(int i = 0; i < roz; i++) {
        tab[i] = rand() % 101;
    }
}


int main()
{
    int rozmiar = 50;
    int tab[rozmiar];
    wypelnij(tab, rozmiar);
    drukuj(tab, rozmiar);
    wypelnij_los(tab, rozmiar);

    //minmax1();
    return 0;
}
