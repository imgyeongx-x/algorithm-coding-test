
#include <iostream>
using namespace std;

int main() {

	int a, b;

	cin >> a >> b;

	int N = a;
	if (a > b)
		N = b;

	for (int i = b; i >= 1; i--) {
		if (a % i == 0 && b % i == 0) {
			N = i;
			break;
		}
	}

	int M = N;

	while (true) {
		if (M % a == 0 && M % b == 0) {
			break;
		}
		M += N;
	}

	cout << N << "\n" << M;


	return 0;
}