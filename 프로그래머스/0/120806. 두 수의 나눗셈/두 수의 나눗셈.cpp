#include <string>
#include <vector>

using namespace std;

int solution(int num1, int num2) {
    double dd = (double) num1 / (double) num2;
    int answer = dd * 1000;
    return answer;
}