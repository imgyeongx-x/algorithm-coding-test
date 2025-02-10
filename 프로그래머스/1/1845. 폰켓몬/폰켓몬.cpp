#include <vector>
using namespace std;

int solution(vector<int> nums)
{
    vector<int> pType(200000, 0);
    
    int get = nums.size() / 2;
    int diff = 0;
    for(int e: nums){
        pType[e]++;
        if (pType[e] == 1)
            diff++;
    }
    
    int answer = diff < get ? diff : get;
    return answer;
}