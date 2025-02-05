
#include <iostream>
using namespace std;

int main() {

	int n;
	cin >> n;

	int nx2[1001];

	nx2[1] = 1;
	nx2[2] = 3;

	for (int i = 3; i <= n; i++) {
		nx2[i] = (nx2[i - 2] * 2 + nx2[i - 1]) % 10007;
	}

	cout << nx2[n];


	return 0;
}