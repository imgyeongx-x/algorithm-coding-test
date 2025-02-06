
#include <iostream>
#include <time.h>
using namespace std;

int main() {

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {

		int a, b;
		cin >> a >> b;
		
		int x = a > b ? a : b;
		int y = a > b ? b : a;

		while (x % y != 0) {
			int tmp = x % y;
			x = y;
			y = tmp;
		}

		int lcd = (a * b) / y;

		cout << lcd << "\n";
	}	

	return 0;
}