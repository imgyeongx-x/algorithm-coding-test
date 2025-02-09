#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    
    int i = 1;
    while (i * i <= n) {
        if (i * i == n)
            answer = 1;
        i++;
    }
    if (answer == 0)
        answer = 2;
    
    return answer;
}