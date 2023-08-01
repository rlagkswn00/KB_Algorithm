#include <iostream>
#include <algorithm>
#define MAX 51
using namespace std;

int N, M, min_val = 100;
char arr[MAX][MAX];

string WB[8] = {
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
};

string BW[8] = {
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
};

int start_W(int x, int y){
    int cnt = 0;
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            if(arr[x+i][y+j] == WB[i][j]){
                cnt++;
            }
        }
    }
    return cnt;
}

int start_B(int x, int y){
    int cnt = 0;
    for(int i = 0; i < 8; i++){
        for(int j = 0; j < 8; j++){
            if(arr[x+i][y+j] == BW[i][j]){
                cnt++;
            }
        }
    }
    return cnt;
}

int main()
{
    cin >> N >> M;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin >> arr[i][j];
        }
    }
    for(int i = 0; i+8 <= N; i++){
        for(int j = 0; j+8 <= M; j++){
            int tmp;
            tmp = min(start_B(i,j),start_W(i,j));
            if(tmp < min_val) {
                min_val = tmp;
            }
        }
    }
    cout << min_val;
    return 0;
}