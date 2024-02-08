#define _CRT_RAND_S

#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

// cryptographically secure random number generation using rand_s

int main(void) {
    FILE* file;
    errno_t err;

    err = fopen_s(&file, "t3.txt", "w");
    if (err != 0) {
        printf("Failed to open the file for writing!\n");
        return 1;
    }

    // Generate and write 64 cryptographically secure random numbers to the file
    for (int i = 0; i < 64; i++) {
        unsigned int number;
        err = rand_s(&number);
        if (err != 0) {
            printf("The rand_s function failed!\n");
            fclose(file);
            return 1;
        }
        fprintf(file, "%u", (unsigned int)(((double)number / ((double)UINT_MAX + 1)) * 10.0) + 1);
    }
    fclose(file);
    return 0;
}