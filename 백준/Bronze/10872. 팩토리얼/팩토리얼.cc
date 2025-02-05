
#include<iostream>
using namespace std;

int main() {

	int N;
	cin >> N;

	int res = 1;

	for (int i = 1; i <= N; i++) {
		res *= i;
	}
	cout << res;

	return 0;
}