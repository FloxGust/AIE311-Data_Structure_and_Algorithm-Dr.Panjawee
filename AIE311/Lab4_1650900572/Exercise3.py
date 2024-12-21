class Graph:
    def __init__(self, num_edges):
        self.num_edges = num_edges + 1
        self.adj_matrix = [[""] * self.num_edges for _ in range(self.num_edges)]
        self.vertices = []

    def create_Adjmat(self, edge):
        self.vertices.append(edge)
        for row in range(len(self.adj_matrix)):
            for col in range(1, len(self.adj_matrix)):
                if row == 0 and self.adj_matrix[row][col] == "":
                    self.adj_matrix[row][col] = edge
                    self.adj_matrix[col][row] = edge
                    break
                elif row > 0 and self.adj_matrix[row][col] == "":
                    self.adj_matrix[row][col] = "0"

    def connect(self, vert1, vert2):
        idx1, idx2 = self.get_indices(vert1, vert2)
        if idx1 is not None and idx2 is not None:
            self.adj_matrix[idx1][idx2] = "1"
            self.adj_matrix[idx2][idx1] = "1"

    def disconnect(self, vert1, vert2):
        idx1, idx2 = self.get_indices(vert1, vert2)
        if idx1 is not None and idx2 is not None:
            self.adj_matrix[idx1][idx2] = "0"
            self.adj_matrix[idx2][idx1] = "0"

    def get_indices(self, vert1, vert2):
        idx1, idx2 = None, None
        for i in range(1, len(self.adj_matrix)):
            if self.adj_matrix[i][0] == vert1:
                idx1 = i
            if self.adj_matrix[0][i] == vert2:
                idx2 = i
        return idx1, idx2

    def print_mat(self):
        for row in self.adj_matrix:
            print(row)

    def print_edge_list(self):
        print("\nEdge List:")
        for i in range(1, len(self.adj_matrix)):
            for j in range(i + 1, len(self.adj_matrix)):
                if self.adj_matrix[i][j] == "1":
                    print(f"{self.adj_matrix[i][0]} - {self.adj_matrix[0][j]}")

    def print_adj_list(self):
        print("\nAdjacency List:")
        adj_list = {vert: [] for vert in self.vertices}
        for i in range(1, len(self.adj_matrix)):
            for j in range(1, len(self.adj_matrix)):
                if self.adj_matrix[i][j] == "1":
                    adj_list[self.adj_matrix[i][0]].append(self.adj_matrix[0][j])
        for vert, neighbors in adj_list.items():
            print(f"{vert}: {' '.join(neighbors)}")

graph1 = Graph(6)
for node in ["A", "B", "C", "D", "E", "F"]:
    graph1.create_Adjmat(node)

graph1.connect("A", "B")
graph1.connect("A", "C")
graph1.connect("C", "D")
graph1.connect("C", "F")
graph1.connect("E", "F")

print("\nAdjacency Matrix:")
graph1.print_mat()
graph1.print_edge_list()
graph1.print_adj_list()


graph1.disconnect("C", "F")
graph1.disconnect("A", "B")
graph1.disconnect("C", "D")



print("\n\nUpdated Adjacency Matrix:")
graph1.print_mat()
graph1.print_edge_list()
graph1.print_adj_list()



graph1.connect("A", "E")
graph1.connect("B", "C")
graph1.connect("D", "F")



print("\n\nFinal Adjacency Matrix:")
graph1.print_mat()
graph1.print_edge_list()
graph1.print_adj_list()
