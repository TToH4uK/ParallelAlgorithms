import sys

try:
    import matplotlib.pyplot as plt
    import networkx as nx
    VISUALIZATION_AVAILABLE = True
except ImportError:
    VISUALIZATION_AVAILABLE = False
    print("Внимание: matplotlib или networkx не найдены. Визуализация будет пропущена, только текстовый вывод.")

class DependencyAnalyzer:
    def __init__(self, M, N):
        self.M = M
        self.N = N
        self.writes = {} 
        self.reads = []  
        self.dependencies = []

    def run_simulation(self):
        """Симулирует выполнение цикла для записи доступов."""
        print(f"Симуляция циклов для M={self.M}, N={self.N}...")
        for m in range(1, self.M + 1):
            for i in range(1, self.N): #
                current_iter = (m, i)
                
                # S1: u(m,i) = u(m,i-1) + u(m-1,i) + u(m-1,i+1)
                
                self.record_read(current_iter, (m, i-1))
                self.record_read(current_iter, (m-1, i))
                self.record_read(current_iter, (m-1, i+1))
                
                self.record_write(current_iter, (m, i))

    def record_read(self, iteration, access_coords):
        self.reads.append({'iter': iteration, 'access': access_coords})

    def record_write(self, iteration, access_coords):
        self.writes[access_coords] = iteration

    def find_dependencies(self):
        """Находит потоковые зависимости (Чтение после Записи)."""
        print("Анализ зависимостей...")
        for read in self.reads:
            access = read['access']
            reader_iter = read['iter']
            
            if access in self.writes:
                writer_iter = self.writes[access]
                
                if writer_iter != reader_iter:
                    dist_m = reader_iter[0] - writer_iter[0]
                    dist_i = reader_iter[1] - writer_iter[1]
                    dist_vector = (dist_m, dist_i)
                    
                    dep = {
                        'source': writer_iter,
                        'dest': reader_iter,
                        'vector': dist_vector,
                        'type': 'Flow'
                    }
                    self.dependencies.append(dep)

    def print_dependencies(self):
        print("\nОбнаруженные зависимости:")
        unique_vectors = set()
        for dep in self.dependencies:
            unique_vectors.add(dep['vector'])
        
        print("\nНайденные уникальные векторы расстояний:")
        for v in sorted(list(unique_vectors)):
            print(f"  d = {v}")

    def generate_expanded_graph(self, filename="expanded_graph.png"):
        print(f"\n--- Развернутый граф зависимостей (Текстовое представление) ---")
        print(f"Узлы: (m, i) для m в 1..{self.M}, i в 1..{self.N-1}")
        print("Ребра (пример):")
        count = 0
        for dep in self.dependencies:
            if count < 10: 
                print(f"  {dep['source']} -> {dep['dest']}")
            count += 1
        if count > 10:
            print(f"  ... и еще {count - 10} ребер.")

        if VISUALIZATION_AVAILABLE:
            G = nx.DiGraph()
            for m in range(1, self.M + 1):
                for i in range(1, self.N):
                    G.add_node((m, i), pos=(i, -m)) 
            for dep in self.dependencies:
                G.add_edge(dep['source'], dep['dest'])

            pos = nx.get_node_attributes(G, 'pos')
            
            plt.figure(figsize=(8, 6))
            nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', arrowsize=20)
            plt.title(f"Развернутый граф зависимостей (M={self.M}, N={self.N})")
            plt.grid(True)
            plt.savefig(filename)
            print(f"Развернутый граф сохранен в {filename}")

    def generate_reduced_graph(self, filename="reduced_graph.png"):
        unique_vectors = set()
        for dep in self.dependencies:
            unique_vectors.add(dep['vector'])
            
        print("\n--- Редуцированный граф зависимостей (Текстовое представление) ---")
        print("Узел: S1")
        print("Ребра (Петли на S1):")
        for v in sorted(list(unique_vectors)):
            print(f"  S1 -> S1 : d={v}")

        if VISUALIZATION_AVAILABLE:
            G = nx.MultiDiGraph()
            G.add_node("S1")
            
            for v in unique_vectors:
                label = f"({v[0]}, {v[1]})"
                G.add_edge("S1", "S1", label=label)

            plt.figure(figsize=(4, 4))
            pos = {"S1": (0, 0)}
            nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightgreen')
            
            plt.title("Редуцированный граф зависимостей")
            plt.axis('off')
            plt.savefig(filename)
            print(f"Редуцированный граф сохранен в {filename}")

if __name__ == "__main__":

    M_val = 3
    N_val = 3 # i идет от 1 до 5
    
    analyzer = DependencyAnalyzer(M_val, N_val)
    analyzer.run_simulation()
    analyzer.find_dependencies()
    analyzer.print_dependencies()
    analyzer.generate_expanded_graph("graphics/expanded_graph.png")
    analyzer.generate_reduced_graph("graphics/reduced_graph.png")
