#include <iostream>
#include <stdio.h>
#include <string>
#include <queue>
#include <algorithm>
using namespace std;

int N;
int safe_num;
queue<pair<int, int>> q;
int visited[101][101];
int map[101][101];

int dx[] = { 0, 0, -1, 1 };
int dy[] = { -1, 1, 0, 0 };

void bfs(int height){
    while (!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        visited[x][y] = 1;

        for (int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N)
                continue;

            if (map[nx][ny] <= height || visited[nx][ny] == 1)
                continue;

            visited[nx][ny] = 1;
            q.push(make_pair(nx, ny));
        }
    }
}

void reset(){
    safe_num = 0;
    for (int x = 0; x < N; x++){
        for (int y = 0; y < N; y++){
            visited[x][y] = 0;
        }
    }
}

int main()
{
    int height = 0, result = 0;
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;

    for (int x = 0; x < N; x++){
        for (int y = 0; y < N; y++){
            cin >> map[x][y];
            if (height < map[x][y]) height = map[x][y];
        }
    }

    while (height >= 0){
        for (int x = 0; x < N; x++){
            for (int y = 0; y < N; y++){
                if (map[x][y] > height && visited[x][y] == 0){
                    q.push(make_pair(x, y));
                    bfs(height);
                    safe_num++;
                }
            }
        }
        if (result < safe_num) result = safe_num;

        reset();
        height--;
    }

    cout << result;
    return 0;
}