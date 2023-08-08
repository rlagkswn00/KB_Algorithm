#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int L, C;
char arr[16];

void solve(int idx, int mo, int ja, string str) {

    //str이 암호 길이면서 모음, 자음 개수 충족시 프린트
    if (str.size() == L) {
        if (mo < 1 || ja < 2) return;
        cout << str << "\n";
        return;
    }
    for (int i = idx; i < C; i++) {
        char temp = arr[i];

        if (temp == 'a' || temp == 'e' || temp == 'i' || temp == 'o' || temp == 'u') {
            solve(i + 1, mo+1, ja, str + temp);
        }
        else {
            solve(i + 1, mo, ja+1, str + temp);
        }

    }
}

int main() {
    cin >> L >> C;
    for (int i = 0; i < C; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + C);
    solve(0, 0, 0, "");
}