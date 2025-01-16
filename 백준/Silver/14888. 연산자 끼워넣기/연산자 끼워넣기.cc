#include <iostream>
#include <stdlib.h>

using namespace std;

int N;
int num[11];
int op[4];

long long minV = 1000000000;
long long maxV = -1000000000;

long long findV(long long res, int index)
{
	if (index == N)
	{
		if (minV > res)
			minV = res;

		if (maxV < res)
			maxV = res;
	}

	for (int i = 0; i < 4; i++)
	{
		if (op[i] > 0)
		{
			op[i]--;
			if (i == 0)
			{
				findV(res + num[index], index + 1);
			}
			else if (i == 1)
			{
				findV(res - num[index], index + 1);
			}
			else if (i == 2)
			{
				findV(res * num[index], index + 1);
			}
			else
			{
				findV(res / num[index], index + 1);
			}
			op[i]++;
		}
	}
	
	return res;
}


int main()
{

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> num[i];
	}

	for (int i = 0; i < 4; i++)
	{
		cin >> op[i];
	}

	findV(num[0], 1);

	cout << maxV << "\n" << minV;


	return 0;
}
