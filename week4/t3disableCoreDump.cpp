#include <iostream>
#include <csignal>

void handleSegmentationFault(int signal) {
    std::cerr << "Segmentation fault (signal " << signal << "). Exiting.\n";
    exit(EXIT_FAILURE);
}

int main() {
    // Custom signal handler for Segmentation fault (Most common reason for Core dump)
    // prevents core dump file from appearing
    signal(SIGSEGV, handleSegmentationFault);

    // Triggering a segmentation fault
    int* nullPointer = nullptr;
    *nullPointer = 32;

    return 0;
}