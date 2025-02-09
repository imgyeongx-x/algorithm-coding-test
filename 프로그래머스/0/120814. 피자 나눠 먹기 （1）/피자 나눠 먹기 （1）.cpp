#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = n / 7 + 1;
    if (n % 7 == 0)
        answer--;   
    
    return answer;
}