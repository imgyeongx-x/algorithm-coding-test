#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<string> babbling) {
    int answer = babbling.size();
    vector<string> word = {"aya", "ye", "woo", "ma"};
    
    for (int i = 0; i < babbling.size(); i++) {
        for (int j = 0; j < 4; j++){
            if (babbling[i].find(word[j]) != string::npos){
                babbling[i].replace(babbling[i].find(word[j]), word[j].size(), "0");
            }
        }
    }
    
    for (int i = 0; i < babbling.size(); i++) {
        for (int j = 0; j < babbling[i].size(); j++){
            
            if (babbling[i][j] != '0'){
                answer--;
                break;
            }
        }
    }
    
    return answer;
}