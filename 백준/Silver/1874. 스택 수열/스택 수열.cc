#include <iostream>
#include <stack>
using namespace std;

int main() {
    int N;
    cin >> N;

    stack<int> st;
    bool possible = true;
    char pp[500000];
    int num = 1;
    int index = 0;
    
    for (int i = 0; i < N; i++){
        int req;
        cin >> req;
        if (possible == false)
            continue;
        if (st.empty() == true)
        {
            st.push(num);
            num++;
            pp[index] = '+';
            index++;
        }
        while (req > st.top()){
            st.push(num);
            num++;
            pp[index] = '+';
            index++;
        }
        if (req == st.top())
        {
            st.pop();
            pp[index] = '-';
            index++;
        }
        else {
            possible = false;
        }
    }

    if (possible == true){
       for (int i = 0; i < index; i++)
           {
               cout << pp[i] << '\n';
           }
    }
    else
        cout << "NO" << endl;
    
    return 0;
}