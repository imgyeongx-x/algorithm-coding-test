#include <iostream>
#include <string>
using namespace std;

int main()
{
    int N;

    cin >> N;
    cin.clear();

    int deq[20000];
    string order;

    int head = 10000;
    int tail = 10000;

    while (N--) {
        cin >> order;
        if (order == "push_front") {
            int num;
            cin >> num;
            head--;
            deq[head] = num;
        }
        else if (order == "push_back") {
            int num;
            cin >> num;
            deq[tail] = num;
            tail++;
        }
        else if (order == "pop_front") {
            if (head == tail)
                cout << "-1\n";
            else {
                cout << deq[head] << "\n";
                head++;
            }
        }
        else if (order == "pop_back") {
            if (head == tail)
                cout << "-1\n";
            else {
                tail--;
                cout << deq[tail] << "\n";
            }
        }
        else if (order == "size") {
            cout << tail - head << "\n";
        }
        else if (order == "empty") {
            if (head == tail)
                cout << "1\n";
            else
                cout << "0\n";
        }
        else if (order == "front") {
            if (head == tail)
                cout << "-1\n";
            else
                cout << deq[head] << "\n";
        }
        else if (order == "back") {
            if (head == tail)
                cout << "-1\n";
            else
                cout << deq[tail-1] << "\n";
        }
    }

    return 0;
}