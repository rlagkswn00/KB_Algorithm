#include <iostream>
#include <algorithm>
using namespace std;

int arr1[51];
int arr2[51];
int N, M;
int sum = 0;

void solve(){
    for(int i = 0; i < N; i++){
        sum += arr1[i]*arr2[N-i-1];
    }
    cout << sum;
}

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    for(int i = 0; i < N; i++){
        cin >> arr1[i];
    }

    for(int j = 0; j < N; j++){
        cin >> arr2[j];
    }

    sort(arr1, arr1+N);
    sort(arr2, arr2+N);

    solve();
}