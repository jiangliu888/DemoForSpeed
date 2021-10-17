#include <iostream>
#include <thread>
using namespace std;

int cnt = 0;

void producer(){
    while (true){
        cnt += 1;
    }
}

void consumer(){
    while(true){
        cnt -= 1;
    }
}

int main(){
    std::thread t1(producer);
    std::thread t2(consumer);
    t1.join();
    t2.join();
    std::cout << cnt << std::endl;
}


// compile
// g++ -Wl,--no-as-needed --std=c++11 -pthread producer-consumer-model.cpp -o main