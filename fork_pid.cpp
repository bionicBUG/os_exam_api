#include <iostream>
#include <unistd.h>
using namespace std;

int main(void) {
        pid_t pid =  fork();
        if (pid ==0) {
            cout<<"child: "<<getpid()<<endl;
            cout<<"parent: "<<getpid()<<endl;
        }
    
}
