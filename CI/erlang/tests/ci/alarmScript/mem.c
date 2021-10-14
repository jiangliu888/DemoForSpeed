/*usage: cc mem.c -o mem.out 后 使用./mem.out 100 & 消耗对应数字MB单位的内存，释放时杀掉对应进程即可*/
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
 
#define UNIT (1024*1024)
 
int main(int argc, char *argv[])
{
        long long i = 0;
        int size = 0;
 
        if (argc != 2) {
                printf(" === argc must 2\n");
                return 1;
        }
        size = strtoull(argv[1], NULL, 10);
        if (size == 0) {
                printf(" argv[1]=%s not good\n", argv[1]);
                return 1;
        }
 
        char *buff = (char *) malloc(size * UNIT);
        if (buff)
                printf(" we malloced %d Mb\n", size);
        buff[0] = 1;
 
        for (i = 1; i < (size * UNIT); i++) {
                if (i%1024 == 0)
                        buff[i] = buff[i-1]/8;
                else
                        buff[i] = i/2;
        }
        pause();
}
