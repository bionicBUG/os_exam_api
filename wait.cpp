#include <iostream>
#include <unistd.h>
#include <sys/wait.h>

using namespace std;

int main(void) {
    pid_t id1=fork();
    pid_t id2 =  fork();
    if (id1 > 0 && id2 > 0) {
        cout<<"child: "<<getpid()<<endl;
    }
    if (id1 > 0 && id2 > 0) {
        wait(NULL);
        wait(NULL);
        cout<<"parent terminated";
    } else if (id2==0 && id1==0) {
        sleep(2);
        wait(NULL);
        cout<<"1st child terminated";
    } else if (id2==0 && id1>0) {
        sleep(1);
        cout<<"second child terminated";
    } else {
        cout<<"grand child terminated";
    }

    
}