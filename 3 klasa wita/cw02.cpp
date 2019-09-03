/*
 * cw02.cpp
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int a,b,c;
    cin >> b >> c;
    do
    {
        a = b;
        b = c;
        cin >> c;
    }
    while (c != a + b);
    cout << c;6
    return 0;

}

