#include <iostream>
using namespace std;

int main()
{    
    int row, col;

    cin >> row;
    cin >> col;
    int my_arr[row][col];

    for (int i = 0; i < row; i++)
    {  
        for (int j = 0; j < col; j++)
        {
            cin >> my_arr[i][j];            
        }        

    }
    for (int i = 0; i < col; i++)
    {
        for (int j = 0; j < row; j++)
        {
            cout << my_arr[j][i];
            cout << " ";
        }
        cout << endl;
    }
    
}