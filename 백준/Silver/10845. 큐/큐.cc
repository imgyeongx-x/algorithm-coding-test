
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int N;
    cin >> N;
    cin.clear();
    
    int arr[10000];
    int prev = 0;
    int next = 0;
    
    
    for (int i = 0; i < N; i++) {
        string order;
        cin >> order;
        
        if (order == "push") {
            int num;
            cin >> num;
            arr[next] = num;
            next++;
        }
        else if (order == "pop") {
            if (prev == next) {
                cout << "-1" << "\n";
            }
            else {
                cout << arr[prev] <<"\n";
                prev++;
            }
        }
        else if (order == "size") {
            cout << next-prev <<"\n";
        }
        else if (order == "empty") {
            if (next == prev)
                cout << 1 << "\n";
            else
                cout << 0 << "\n";
        }
        else if (order == "front") {
            if (next == prev) {
                cout << -1 << "\n";
            }
            else {
                cout << arr[prev] << "\n";
            }
        }
        else if (order == "back") {
            if (next == prev) {
                cout << -1 << "\n";
            }
            else {
                cout << arr[next-1] << "\n";
            }
        }
    }
    return 0;
}