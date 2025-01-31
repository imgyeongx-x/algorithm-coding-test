#include <iostream>
#include <string>
#include <queue>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
    int N;
    int K;
    
    cin >> N >> K;
    
    queue<int> q;
    
    for (int i = 0; i < N; i++) {
        q.push(i+1);
    }
    
    int k = 0;
    
    int result[500000];
    int rIndex = 0;
    
    while (!q.empty()) {
        if (k == K - 1) {
            result[rIndex] = q.front();
            q.pop();
            rIndex++;
            
            k = 0;
        }
        else {
            k++;
            int tmp = q.front();
            q.push(tmp);
            q.pop();
        }
    }
    
    cout<<"<";
    for (int i = 0; i < rIndex; i++) {
        cout << result[i];
        if (i != rIndex - 1)
            cout << ", ";
    }
    cout << ">";
    
    return 0;
}