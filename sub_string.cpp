#include <iostream>
using namespace std;

int main(){
    int t;
    long int x, m ;    
    cin >>t;    
    while (t--)        
    {
        long long max_count = 0;
        x=0;
        string my_string;
        cin >> my_string;
        m = my_string.length();
        for (int i = 0; i < m; i++)
        {  
            if (my_string[i] == 'a' || my_string[i] ==  'e' || my_string[i] ==  'i' || my_string[i] ==  'o' || my_string[i] ==  'u' || my_string[i] ==  'A' || my_string[i] ==  'E' || my_string[i] ==  'I' || my_string[i] ==  'O' || my_string[i] ==  'U')
            {  
                x = (i+1)*(m-i);
                max_count += x;
            }                    
                   
        }
        cout << max_count << endl;
        max_count = 0;
    }    
}