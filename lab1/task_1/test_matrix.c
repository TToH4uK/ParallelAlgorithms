#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "matrix_multiply.c"

// Простой тест для проверки корректности
void test_small_matrix() {
    int n = 3;
    double *A = (double *)malloc(n * n * sizeof(double));
    double *B = (double *)malloc(n * n * sizeof(double));
    double *C_naive = (double *)calloc(n * n, sizeof(double));
    double *C_block = (double *)calloc(n * n, sizeof(double));
    
    // Простая матрица для теста
    for (int i = 0; i < n * n; i++) {
        A[i] = i + 1;
        B[i] = 1;
    }
    
    naive_matrix_multiply(A, B, C_naive, n);
    block_matrix_multiply(A, B, C_block, n, 2);
    
    assert(check_correctness(C_naive, C_block, n, 1e-5));
    printf("Test passed!\n");
    
    free(A);
    free(B);
    free(C_naive);
    free(C_block);
}

int main() {
    test_small_matrix();
    return 0;
}
