class Dinic:
    def __init__(self, graph):
        self.graph = graph  # Граф в виде словаря
        self.capacity = {}  # Ёмкости рёбер
        self.level = {}  # Уровни вершин

    def add_edge(self, u, v, cap):
        self.capacity[(u, v)] = cap
        self.capacity[(v, u)] = 0  # Обратное ребро с ёмкостью 0

    def bfs(self, source, sink):
        self.level = {u: -1 for u in self.graph}  # Инициализация уровней
        self.level[source] = 0
        queue = [source]

        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if self.level[v] < 0 and self.capacity[(u, v)] > 0:  # Если не посещена и есть остаточная ёмкость
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
                    if v == sink:
                        return True
        return False

    def dfs(self, u, sink, flow):
        if u == sink:
            return flow
        for v in self.graph[u]:
            if self.level[v] == self.level[u] + 1 and self.capacity[(u, v)] > 0:
                current_flow = min(flow, self.capacity[(u, v)])
                temp_flow = self.dfs(v, sink, current_flow)
                if temp_flow > 0:
                    self.capacity[(u, v)] -= temp_flow
                    self.capacity[(v, u)] += temp_flow
                    return temp_flow
        return 0

    def max_flow(self, source, sink):
        total_flow = 0
        while self.bfs(source, sink):
            while True:
                flow = self.dfs(source, sink, float('Inf'))
                if flow == 0:
                    break
                total_flow += flow
        return total_flow


# Пример использования
if __name__ == "__main__":
    # Граф в виде словаря
    graph = {
        0:[1,2],
        1:[2,3],
        2:[1,4],
        3:[2,5],
        4:[3,5],
        5:[]
    }

    dinic = Dinic(graph)

    # Добавление рёбер (u, v, capacity)
    dinic.add_edge(0, 1, 16)
    dinic.add_edge(0, 2, 13)
    dinic.add_edge(1, 2, 10)
    dinic.add_edge(1, 3, 12)
    dinic.add_edge(2, 1, 4)
    dinic.add_edge(2, 4, 14)
    dinic.add_edge(3, 2, 9)
    dinic.add_edge(3, 5, 20)
    dinic.add_edge(4, 3, 7)
    dinic.add_edge(4, 5, 4)


    source = 0  # Источник
    sink = 5  # Сток
    print("Максимальный поток:", dinic.max_flow(source, sink))