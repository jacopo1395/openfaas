#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <pthread.h>


void* work(void* vargp){
    int* lvl = (int *)vargp;
    // printf("%d\n", *lvl);
    char cmd [100];
    // char file [100];
    strcpy(cmd, "python3 client.py ");
    if (*lvl==1){
        strcat(cmd,"1");
        // strcat(file,"result_1.txt");
    }
    if (*lvl==2){
        strcat(cmd,"2");
        // strcat(file,"result_2.txt");
    }
    if (*lvl==3){
        strcat(cmd,"3");
        // strcat(file,"result_3.txt");
    }
    // strcat(cmd," > ");
    // strcat(cmd,file);

    // strcat(cmd," &");
    // printf("%s\n",cmd );
    system(cmd);
}


int main(int argc, char const* argv[]) {
    int max,step,lvl;
    if( argc != 4 ) {
        printf("Required 3 parameters <max_threads> <step_range> <max_difficulty>\n");
        exit(-1);
    }
    max = atoi(argv[1]);
    step = atoi(argv[2]);
    lvl = atoi(argv[3]);

    FILE *f = fopen("result.txt", "w+");
    if (f == NULL){
        printf("Error opening file!\n");
        exit(1);
    }
    fprintf(f, "difficulty,threads,millisecond,latency\n");
    fclose(f);

    for (int i=1; i<lvl+1; i++){
        // printf("lvl\n");
        for (int j = 0; j <= max; j=j+step) {
            int j1 = j;
            if (j==0) j1=1;
            // printf("threads\n");
            pthread_t threads[max];
            clock_t begin = clock();
            for (int k = 1; k < j1; k++) {
                int ret = pthread_create (&threads[k], NULL, work, (void *)&i);
                if (ret){
                    printf("ERROR; return code from pthread_create() is %d\n",ret);
                    exit(-1);
                }
            }
            for (int k = 1; k < j1; k++) {
                pthread_join(threads[k], NULL);
            }
            clock_t end = clock();
            double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
            time_spent*=1000;
            FILE *f = fopen("result.txt", "a");
            if (f == NULL){
                printf("Error opening file!\n");
                exit(1);
            }
            fprintf(f, "%d,%d,%lf,%lf\n", i,j1,time_spent,time_spent/j1);
            printf("%d,%d,%lf,%lf\n", i,j1,time_spent,time_spent/j1);
            fclose(f);
        }
    }
    return 0;
}
