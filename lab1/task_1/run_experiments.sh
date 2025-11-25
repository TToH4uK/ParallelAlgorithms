#!/bin/bash

echo "Matrix Size,Block Size,Naive Time,Block Time,Correct"

for n in 100 200 300 400 500; do
    for r in 1 2 5 10 15 20 30 50 100 200 $n; do
        ./matrix_multiply $n $r
    done
done

for n in 500 1000 1500 2000 5000 10000; do
    for r in 1 2 5 10 15 20 30 50 100 200 500; do
        ./matrix_multiply $n $r
    done    
done

for n in 128 256 512 1024 2048; do
    for r in 1 2 5 10 15 20 30 50 100 200; do
        ./matrix_multiply $n $r
    done
done
