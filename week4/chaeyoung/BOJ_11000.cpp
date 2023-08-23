#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

vector<pair<int, int>> v;
priority_queue<int,vector<int>,greater<int>> pq;
int N;
int ans;

int main(){

    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    int s, t;
    for(int i = 0; i < N; i++){
        cin >> s >> t;
        v.push_back(pair<int,int>(s,t));
    }
    sort(v.begin(),v.end());

    //가장 첫 수업의 끝나는 시간 먼저 추가
    pq.push(v[0].second);

    for(int j = 1; j < N; j++){
        if(pq.top() <= v[j].first){
            pq.pop();
        }
        pq.push(v[j].second);
    }
    ans = pq.size();

    cout << ans;
}