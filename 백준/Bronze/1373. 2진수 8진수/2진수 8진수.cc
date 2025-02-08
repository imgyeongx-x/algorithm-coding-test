
#include <iostream>
#include <string>
using namespace std;

int main() {

	string N;
	cin >> N;

	while (N.size() % 3 != 0) {
		N = "0" + N;
	}

	string M = "";

	for (int i = 0; i < N.size(); i += 3) {
		M.push_back((N[i] - '0') * 4 + (N[i + 1]-'0') * 2 + (N[i + 2]-'0') + '0');
	}

	cout << M;

	return 0;
}