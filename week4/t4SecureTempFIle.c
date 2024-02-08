#define _CRT_RAND_S

#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

// creates temporary file following guidelines from https://wiki.sei.cmu.edu/confluence/display/c/FIO21-C.+Do+not+create+temporary+files+in+shared+directories

int main(void) {
    FILE* file;
    errno_t err;

    // Generate a unique file name based on 16 cryptographically secure random numbers
    char filename[33];  
    for (int i = 0; i < 16; i++) {
        unsigned int number;
        err = rand_s(&number);
        if (err != 0) {
            printf("The rand_s function failed!\n");
            return 1;
        }

        // Concatenate the entire number in hexadecimal format
        sprintf(filename + i * 2, "%02x", number);
    }

    // Open the file for writing with atomic open and exclusive access
    err = fopen_s(&file, filename, "wx");
    if (err != 0) {
        printf("Failed to open the file for writing!\n");
        return 1;
    }

    fprintf(file, "%s", "some temporary data");

    // Close the file after use
    fclose(file);

    // Remove the file before program exit
    if (remove(filename) != 0) {
        printf("Failed to remove the file!\n");
        return 1;
    }

    return 0;
}