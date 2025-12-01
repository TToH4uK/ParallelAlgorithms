import matplotlib.pyplot as plt
import pandas as pd
import os

# Загружаем данные
df_parr = pd.read_csv('results.csv')
df_seq = pd.read_csv('seq_results.csv')

# Создаём директорию для графиков
os.makedirs("graphics", exist_ok=True)

# Среднее время для последовательного алгоритма
parr_naive_time = df_parr.groupby('Matrix Size', as_index=False)['Naive Time'].mean().rename(columns={'Naive Time': 'Time'})
seq_naive_time = df_seq.groupby('Matrix Size', as_index=False)['Naive Time'].mean().rename(columns={'Naive Time': 'Time'})


def plot_comparison(block_size):
    # Среднее время для выбранного блока
    parr_block_time = df_parr[df_parr['Block Size'] == block_size].groupby('Matrix Size', as_index=False)['Block Time'].mean()
    seq_block_time = df_seq[df_seq['Block Size'] == block_size].groupby('Matrix Size', as_index=False)['Block Time'].mean()
    
    plt.figure(figsize=(8,5))
    plt.plot(parr_naive_time['Matrix Size'], parr_naive_time['Time'], label='Parallel', linewidth=2, color='black')
    plt.plot(seq_naive_time['Matrix Size'], seq_naive_time['Time'], label='Sequential', linewidth=2, color='blue')
    plt.plot(parr_block_time['Matrix Size'], parr_block_time['Block Time'], label=f'Parallel Block {block_size}', linewidth=2, color='red')
    plt.plot(seq_block_time['Matrix Size'], seq_block_time['Block Time'], label=f'Sequential Block {block_size}', linewidth=2, color='green')
    
    plt.xlabel('Matrix Size')
    plt.ylabel('Average Time (s)')
    plt.title(f'Matrix Multiplication: Sequential vs Block {block_size}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'graphics/comprasion_{block_size}.png')
    plt.close()

# Строим два графика: для блока 1 и блока 500
plot_comparison(1)
plot_comparison(500)
