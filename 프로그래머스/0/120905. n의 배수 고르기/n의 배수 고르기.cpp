#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, vector<int> numlist) {
    vector<int> answer;
    
    for (int i = 0; i < numlist.size(); i++){
        if (numlist[i] % n != 0){
            numlist.erase(numlist.begin()+i);
            i--;
        }
    }
    
    answer = numlist;
    
    return answer;
}