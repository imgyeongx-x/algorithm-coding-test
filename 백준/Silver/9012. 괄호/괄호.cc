#include <iostream>
#include <stack>

using namespace std;

int main() {

	stack<char> PS;
	int T;
	cin >> T;
	cin.ignore();

	bool isVPS = true;

	for (int i = 0; i < T; i++) {
		isVPS = true;
		PS = {};

		char ch;
		ch = cin.get();

		while (ch != '\n') {
			if (ch == '(') {
				PS.push(ch);
			}
			else if (ch == ')') {
				if (PS.empty()) {
					isVPS = false;
				}
				else
					PS.pop();
			}
			ch = cin.get();
		}

		if (PS.size() != 0 || isVPS == false)
			cout << "NO" << endl;

		else
			cout << "YES" << endl;
	}

	return 0;
}