
#include <iostream>
using namespace std;

int main() {

	int T;
	cin >> T;

	int n;
	int add[12];
	int ott[4];

	add[0] = 0;
	add[1] = 1;
	add[2] = 2;
	add[3] = 4;

	for (int i = 4; i < 12; i++) {
		add[i] = add[i - 3] + add[i - 2] + add[i - 1];
	}

	for (int i = 0; i < T; i++) {
		cin >> n;
		cout << add[n] << "\n";
	}


	return 0;
}