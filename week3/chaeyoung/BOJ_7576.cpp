#include <iostream>
#include <stdio.h>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int N, M, result = 0;
int arr[1001][1001];
queue<pair<int, int>> q;

int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };

void bfs() {
    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
                if (arr[nx][ny] == 0) {
                    arr[nx][ny] = arr[x][y] + 1;
                    q.push(make_pair(nx, ny));
                }
            }
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> M >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 1) q.push(make_pair(i, j));
        }
    }
    bfs();
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (arr[i][j] == 0) {
                cout << -1 << "\n";
                return 0;
            }

            if (result < arr[i][j]) {
                result = arr[i][j];
            }
        }
    }
    cout << result-1;
    return 0;
}