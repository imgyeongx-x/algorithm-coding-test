
#include <iostream>
#include <string>
#include <stack>
using namespace std;


int main() {

	string str;
	cin >> str;
	string str_a;

	int raser = 0;
	
	int stickN = 0;
	int cutN = 0;

	for (int i = 0; i < str.size(); i++) {
		if (str[i] == '(' && str[i + 1] == ')') {
			cutN += stickN;
			i++;
		}
		else {
			if (str[i] == '(') {
				stickN++;
			}
			else if (str[i] == ')') {
				stickN--;
				cutN++;
			}
		}
		/*cout << "stick is " << stickN;
		cout << " cut is " << cutN << '\n';*/
	}
	cout << cutN;

	return 0;
}