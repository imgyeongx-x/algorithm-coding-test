
#include <iostream>
using namespace std;

int main() {

	int N;
	cin >> N;
	
	int fibo[1001];
	fibo[0] = 1;
	fibo[1] = 1;

	for (int i = 2; i <= N; i++) {
		fibo[i] = (fibo[i - 1] + fibo[i - 2])%10007;
	}

	cout << fibo[N];

	return 0;
}