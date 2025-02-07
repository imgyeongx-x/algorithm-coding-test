
#include <iostream>
using namespace std;

long long _gcd(long long a, long long b) {
	if (a < b) {
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

	long long N; // 동생 수
	long long S; // 수빈 위치
	cin >> N >> S;

	long long *arr = new long long[N];

	for (int i = 0; i < N; i++) {
		long long tmp;
		cin >> tmp;

		arr[i] = S - tmp >= 0 ? S - tmp : tmp - S;
	}
	
	if (N == 1)
		cout << arr[0];

	else {
		long long gcd = _gcd(arr[0], arr[1]);
		for (int i = 2; i < N; i++) {
			gcd = _gcd(gcd, arr[i]);
		}
		cout << gcd;
	}

	return 0;
}