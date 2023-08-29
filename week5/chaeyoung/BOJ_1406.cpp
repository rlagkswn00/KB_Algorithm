#include <iostream>
#include <stdio.h>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    list<char> v;
    int N;
    auto current = v.end();
    char com;

    string s;
    cin >> s;
    for (int i = 0; i < s.size(); i++) {
        v.push_back(s[i]);
    }
    cin >> N;

    while (N > 0) {

        cin >> com;
        if (com == 'L') {
            if(current != v.begin())
                current--;
        }
        else if (com == 'D') {
            if (current != v.end())
                current++;
        }
        else if (com == 'B') {
            if(current != v.begin())
                current = v.erase(--current);
        }
        else if (com == 'P') {

            char extra;
            cin >> extra;
            v.insert(current, extra);
        }

        N--;
    }
    int k = v.size();
    for (auto it = v.begin(); it != v.end(); it++) {
        cout << *it;
    }

}
