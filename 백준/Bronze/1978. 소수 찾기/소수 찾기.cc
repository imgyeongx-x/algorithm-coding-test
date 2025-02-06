
#include <iostream>
#include <numeric>
using namespace std;

int main() {

	int N;
	cin >> N;
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		int j;
		for (j = num - 1; j >= 1; j--) {
			if (num % j == 0)
				break;
		}
		if (j == 1)
			cnt++;
	}
	cout << cnt;
	
	return 0;
}