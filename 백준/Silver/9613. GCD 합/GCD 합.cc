
#include <iostream>
using namespace std;

int __gcd(int a, int b) {
	if (b > a) {
		int tmp = b;
		b = a;
		a = tmp;
	}
	while (a % b != 0) {
		int tmp = a % b;
		a = b;
		b = tmp;
	}
	return b;
}

int main() {
	
	int t;
	cin >> t;

	while (t--) {
		int n;
		cin >> n;

		int arr[101];

		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		long long g = 0;

		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				g += __gcd(arr[i], arr[j]);
			}
		}

		cout << g << "\n";
	}

	return 0;
}