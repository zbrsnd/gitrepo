#include <cstdlib>
#include <iostream>

using namespace std;

int ciag_rek(int i)
{
        if(i==0)
        
            return 0;
            
        else
        
        return ciag_rek(i-1)+1+(i-1)*2;
}
int main(int argc, char **argv)
{
        int h;
        
        cout << "Który wyraz ciagu ? : ";
        
        cin >> h;
        
        cout << ciag_rek(h);
        
        return 0;
}

