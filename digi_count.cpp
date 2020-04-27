#include <iostream>
using namespace std;

int main(){
    int my_arr[10]={0,1,2,3,4,5,6,7,8,9};
    int count, my_var;
    string s;
    cin >> s;
    for (int i = 0; i < 10; i++)
    {
        count = 0;
        my_var = 0;
        for (int j = 0; j < s.length(); j++)
        {
            my_var = s[j];
            if (i == my_var-48)
            {
                count++;
            }
            
        }
        cout << i << "  " << count << endl;        
    }
    
}