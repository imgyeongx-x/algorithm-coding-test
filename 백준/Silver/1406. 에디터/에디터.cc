#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
	cin.tie(NULL);


    string input;
    cin >> input;
    
    stack<char> left;
    stack<char> right;
    
    for (int i = 0; i < input.size(); i++){
        left.push(input[i]);
    }
    
    int cursor = input.size();
    cin.clear();

    int N;
    cin >> N;

    for (int i = 0; i < N; i++){
        char order;
        cin >> order;
        if (order == 'L'){
            if (!left.empty()){
                right.push(left.top());
                left.pop();
            }
        }
        else if (order == 'D'){
            if (!right.empty()){
                left.push(right.top());
                right.pop();
            }
        }
        else if (order == 'B'){
            if (!left.empty()){
                left.pop();
                cursor--;
            }
        }
        else if (order == 'P') {
            char newch;
            cin >> newch;

            left.push(newch);
            cursor++;
        }
    }
    
    string result = "";
    while (!left.empty()){
        right.push(left.top());
        left.pop();
    }
    
    while (!right.empty()){
        cout << right.top();
        right.pop();
    }

    cout << result;
    
    return 0;
}