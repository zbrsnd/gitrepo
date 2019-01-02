/*
 * sortowanie.cpp
 */


#include <iostream>
using namespace std;

void wypelnij(int tab[], int roz) {
    srand(time(NULL)); //inicjacja generatora liczb pseudolosowych
    for(int i=0; i < roz; i++) {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int roz) {
    for(int i=0; i < roz; i++) {
        cout << tab[i] << " ";
        
    }
}


void zamien1(int &a, int &b) {
    
    cout << a << " " << b << endl;
    int tmp = a;
    a = b;
    b = tmp;
    cout << a << " " << b << endl;
    
    }

//~void bubble_sort_asc(int tab[], int n) { // n - rozmiar tablicy
    //~int i,j;
    //~for(i = 0; i < n-1; i++) {
        //~for(j = 0; j < n-1-i; j++) {
               //~if(tab[j] > tab[j+1])
                //~zamien1(&tab[j], &[tab j+1])
                
            //~}
        //~}
    //~} 


void sort_selection(int tab[], int n) {
    
    int i,k,j;
    for(i = 0; i < n-1; i++) {
        k = i; //indeks najmniejszego elementu
        for (j = k+1; j < n; j++) {
            if (tab[j] > tab[k]) 
                k = j;
            }
        zamien1(tab[i], tab[k]);
        }
    }


int main(int argc, char **argv)
{
	int roz = 20;
    int tab[roz];
    wypelnij(tab,roz);
    //~drukuj(tab,roz);
    tab[0] = 7;
    tab[1] = 5;
    zamien1(tab[0], tab[1]);
    cout << tab[0] << " " << tab[1] << endl;
    sort_selection(tab,roz);
    drukuj(tab,roz);
	return 0;
}

