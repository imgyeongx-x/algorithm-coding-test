
#include <iostream>
#include <string>
#include <stack>
#include <queue>
using namespace std;

int main() {

	string line;
	stack<char> st;
	queue<char> qu;

	getline(cin, line, '\n');
	bool isFlip = true;

	for (int i = 0; i < line.size(); i++) {

		//cout << line[i];

		if (isFlip == true) {
			if (line[i] == '<') {
				while (!st.empty()) {
					cout << st.top();
					st.pop();
				}
				isFlip = false;
				cout << '<';
			}

			else if ((line[i] >= 'a' && line[i] <= 'z') || (line[i] >= '0' && line[i] <= '9')) {
				st.push(line[i]);
				if (i == line.size() - 1) {
					while (!st.empty()) {
						cout << st.top();
						st.pop();
					}
				}
			}

			else if (line[i] == ' ') {
				while (!st.empty()) {
					cout << st.top();
					st.pop();
				}
				cout << ' ';
			}
		}

		else if (isFlip == false){

			//cout << "don't flip" << '\n';
			if (line[i] != '>') {
				qu.push(line[i]);
			}
			else {
				while (!qu.empty()) {
					cout << qu.front();
					qu.pop();
				}
				cout << '>';
				isFlip = true;
			}
		}
	}

	return 0;
}