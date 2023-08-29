#include <iostream>
#include <stdio.h>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

int a1, a2, b1, b2, c1, c2, d1, d2;
int N = 4;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    while (N > 0) {
        cin >> a1 >> b1 >> c1 >> d1 >> a2 >> b2 >> c2 >> d2;
        if (a1 < a2) {
            if (a2 == c1 || d1 == b2) {
                if (a2 == c1 && d1 == b2)
                    cout << "c" << "\n";
                else
                    cout << "b" << "\n";
            }
            else if (a2 - c1 < 0 && b2 - d1 < 0) {
                if (d2 < b1) cout << "d" << "\n";
                else if (d2 == b1) {
                    if (a2 == c1) cout << "c" << "\n";
                    else cout << "b" << "\n";
                }
                else cout << "a" << "\n";
            }
            else
                cout << "d" << "\n";
        }
        else {
            if (a1 == c2 || d2 == b1) {
                if (a1 == c2 && d2 == b1)
                    cout << "c" << "\n";
                else
                    cout << "b" << "\n";
            }
            else if (a1 - c2 < 0 && b1 - d2 < 0) {
                if (d1 < b2) cout << "a" << "\n";
                else if (d1 == b2) {
                    if (a1 == c2) cout << "c" << "\n";
                    else cout << "b" << "\n";
                }
                else cout << "a" << "\n";
            }
            else
                cout << "d" << "\n";
        }
        N--;
    }
    return 0;
}
