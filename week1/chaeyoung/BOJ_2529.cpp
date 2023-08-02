#include <iostream>
#include <string>
using namespace std;

int K;
char op[11];
bool visited[11];
string minvalue = "", maxvalue = "";


void dfs(int prev, char operation, int idx, string str){
    if(idx == K){
        maxvalue = str;
        if(minvalue == ""){
            minvalue = str;
        }
        return;
    }
    for(int i = 0; i < 10; i++){
        if(visited[i]) continue;
        visited[i] = true;
        //int -> char
        char next = i + '0';

        if(operation == '<' && prev < i){
            dfs(i, op[idx+1], idx+1, str + next);
        }
        if(operation == '>' && prev > i){
            dfs(i, op[idx+1], idx+1, str + next);
        }
        visited[i] = false;
    }
}

int main(){
    cin >> K;
    for(int i = 0; i < K; i++){
        cin >> op[i];
    }
    for(int i = 0; i < 10; i++){
        visited[i] = true;
        char now = i + '0';
        string st = "";
        st += now;
        dfs(i, op[0], 0, st);
        visited[i] = false;
    }

    cout << maxvalue << "\n" << minvalue << "\n";
    return 0;
}