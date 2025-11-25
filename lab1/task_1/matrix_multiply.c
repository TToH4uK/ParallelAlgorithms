#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <omp.h>

void naive_matrix_multiply(double *A, double *B, double *C, int n) {
    // #pragma omp parallel for collapse(2)
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            double sum = 0.0;
            for (int k = 0; k < n; k++) {
                sum += A[i * n + k] * B[k * n + j];
            }
            C[i * n + j] = sum;
        }
    }
}

void block_matrix_multiply(double *A, double *B, double *C, int n, int r) {
    // #pragma omp parallel for collapse(2)
    for (int ii = 0; ii < n; ii += r) {
        for (int jj = 0; jj < n; jj += r) {
            int i_end = (ii + r < n) ? (ii + r) : n;
            int j_end = (jj + r < n) ? (jj + r) : n;
            
            for (int kk = 0; kk < n; kk += r) {
                int k_end = (kk + r < n) ? (kk + r) : n;
                
                for (int i = ii; i < i_end; i++) {
                    for (int j = jj; j < j_end; j++) {
                        double sum = 0.0;
                        for (int k = kk; k < k_end; k++) {
                            sum += A[i * n + k] * B[k * n + j];
                        }
                        C[i * n + j] += sum;
                    }
                }
            }
        }
    }
}

void init_matrix(double *matrix, int n) {
    for (int i = 0; i < n * n; i++) {
        matrix[i] = (rand() % 20001) / 100.0 - 100.0;
    }
}

int check_correctness(double *C1, double *C2, int n, double epsilon) {
    for (int i = 0; i < n * n; i++) {
        if (fabs(C1[i] - C2[i]) > epsilon) {
            return 0;
        }
    }
    return 1;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        printf("Usage: %s <matrix_size> <block_size>\n", argv[0]);
        return 1;
    }
    
    int n = atoi(argv[1]);
    int r = atoi(argv[2]);
    
    srand(time(NULL));
    
    double *A = (double *)malloc(n * n * sizeof(double));
    double *B = (double *)malloc(n * n * sizeof(double));
    double *C_naive = (double *)calloc(n * n, sizeof(double));
    double *C_block = (double *)calloc(n * n, sizeof(double));
    
    init_matrix(A, n);
    init_matrix(B, n);
    
    double start = omp_get_wtime();
    naive_matrix_multiply(A, B, C_naive, n);
    double naive_time = omp_get_wtime() - start;
    
    start = omp_get_wtime();
    block_matrix_multiply(A, B, C_block, n, r);
    double block_time = omp_get_wtime() - start;
    
    int correct = check_correctness(C_naive, C_block, n, 1e-5);
    
    printf("%d,%d,%.6f,%.6f,%s\n", n, r, naive_time, block_time, correct ? "OK" : "FAIL");
    
    free(A);
    free(B);
    free(C_naive);
    free(C_block);
    
    return 0;
}
