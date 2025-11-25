import matplotlib.pyplot as plt
import pandas as pd
import os

# Загружаем данные
df = pd.read_csv('results.csv')

# Создаём директорию для графиков
os.makedirs("graphics", exist_ok=True)

# Среднее время для последовательного алгоритма
naive_time = df.groupby('Matrix Size', as_index=False)['Naive Time'].mean().rename(columns={'Naive Time': 'Time'})

def plot_comparison(block_size):
    # Среднее время для выбранного блока
    block_time = df[df['Block Size'] == block_size].groupby('Matrix Size', as_index=False)['Block Time'].mean()
    
    plt.figure(figsize=(8,5))
    plt.plot(naive_time['Matrix Size'], naive_time['Time'], label='Sequential', linewidth=2, color='black')
    plt.plot(block_time['Matrix Size'], block_time['Block Time'], label=f'Block {block_size}', linewidth=2, color='blue')
    
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
