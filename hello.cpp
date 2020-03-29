// Thanxxx P1
#include <iostream>
using namespace std;
int main() {
      bool notfound = true;
      int number;
      while (notfound)
      {         
         cin >> number;
         if (number != 42 && notfound == true) 
         {
            cout << number << endl;
         } else
         {
            notfound = false;
         }                  
      }      
   return 0;
}