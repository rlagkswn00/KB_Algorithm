#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int T, n, sum = 0;
int arr[12];

int solve(int num){
    if(num == 1){
        return 1;
    }
    if(num == 2){
        return 2;
    }
    if(num == 3){
        return 4;
    }
    if(arr[num]!= -1){
        return arr[num];
    }
    return arr[num] = solve(num-1) + solve(num-2) + solve(num-3);
}

int main(){
    cin >> T;
    while(T--){
        cin >> n;
        memset(arr, -1, sizeof(arr));
        cout << solve(n) << endl;
    }
}