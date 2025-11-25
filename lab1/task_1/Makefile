CC=gcc
CFLAGS=-fopenmp -O3 -Wall -std=c99
TARGET=matrix_multiply

all: $(TARGET)

$(TARGET): matrix_multiply.c
	$(CC) $(CFLAGS) -o $(TARGET) matrix_multiply.c -lm

clean:
	rm -f $(TARGET)

run: $(TARGET)
	chmod +x run_experiments.sh
	./run_experiments.sh > seq_results.csv

.PHONY: all clean run
