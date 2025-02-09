#include <string>
#include <vector>
#include <math.h>

using namespace std;

int solution(int n) {
    int answer = 0;
    
    for (int i = 1; i <= sqrt(n); i++){
        if (n % i == 0){
            if (i == sqrt(n))
                answer++;
            else
                answer+=2;
        }
    }
    
    return answer;
}