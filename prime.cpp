#include <cstring>
#include<iostream>
using namespace std;

int main(){
    int testCase, lower_limit, upper_limit;
    bool flag = true;
    cin >> testCase;

    for (int i = 0; i < testCase; i++)
    {

        cin >> lower_limit;
        cin >> upper_limit;
        cout << endl;

        isPrime(lower_limit, upper_limit);
    }
    return 0;
}

void isPrime(int lowerLimit, int upperLimit)
{
    bool primeNo[upperLimit + 1];
    memset(primeNo, true, sizeof(primeNo));
    primeNo[1] = false;
    for (int i = 2; i * i < upperLimit; i++)
    {
        if (primeNo[i] == true)
        {
            for (int j = i * i; j <= upperLimit; j = j + i)
            {
                primeNo[j] = false;
            }
        }
    }
    for (int k = lowerLimit; k < sizeof(primeNo); k++)
    {
        if (primeNo[k] == 1)
        {
            cout << k << endl;
        }
    }
}