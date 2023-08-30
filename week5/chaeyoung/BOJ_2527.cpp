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

        int minX = min(a1, a2);
        int maxX = max(c1, c2);
        int minY = min(b1, b2);
        int maxY = max(d1, d2);

        int A = maxX-minX;
        int B = (c1-a1) + (c2-a2);
        int C = maxY-minY;
        int D = (d1-b1) + (d2-b2);

        if(A==B && C==D){
            cout << "c\n";
        }else if((A==B && C<D) || (C==D && A<B)){
            cout << "b\n";
        }else if(B < A || D < C){
            cout << "d\n";
        }else{
            cout << "a\n";
        }

        N--;
    }
    return 0;
}
