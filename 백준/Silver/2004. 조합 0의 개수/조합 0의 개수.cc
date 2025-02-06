
#include <iostream>

using namespace std;

long long findfive(long long n) {
	long long cnt = 0;
	for (long long i = 5; i <= n; i *= 5) {
		cnt += n / i;
	}
	return cnt;
}

long long findtwo(long long n) {
	long long cnt = 0;
	for (long long i = 2; i <= n; i *= 2) {
		cnt += n / i;
	}
	return cnt;
}

int main() {

	long long n, m;
	cin >> n >> m;

	long long five = findfive(n) - (findfive(m) + findfive(n - m));

	long long two = findtwo(n) - (findtwo(m) + findtwo(n - m));

	long long res = five < two ? five : two;
	//cout << five << two;

	if (res < 0)
		res = 0;
	cout << res;

	return 0;
}