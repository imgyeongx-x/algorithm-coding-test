#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    int answer = schedules.size(); 
    for (int i = 0; i < schedules.size(); i++){
        schedules[i] += 10;
        if (schedules[i] % 100 >= 60)
            schedules[i] += 100 - 60;
        
        bool late = false;
        for (auto t : timelogs[i]){
            if (startday == 6 || startday == 7) {
                startday++;
                if (startday == 8)
                    startday -= 7;
                continue;
            }
            else {
                if (t > schedules[i]){
                    late = true;
                }
                startday++;
            }
        }
        
        if (late == true)
        {
            answer--;
        }
        late = false;
    }
    
    return answer;
}