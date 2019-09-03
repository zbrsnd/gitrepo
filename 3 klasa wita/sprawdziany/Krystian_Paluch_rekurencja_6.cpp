#include <iostream>
#include <cstdlib>

using namespace std;

int NWD_rek(int a, int b)
{
   if(a!=b)
   
     return NWD_rek(a>b?a-b:a,b>a?b-a:b);
     
   return a; 
}
 
int main(int argc, char **argv)
{
    int x, y;
 
    cout<<"Podaj dwie liczby: ";
    
    cin>>x>>y;
 
    cout<<"Największy wspólny dzielnik ("<<x<<","<<y<<") = "<<NWD_rek(x,y)<<endl;
    
    return 0;
}

