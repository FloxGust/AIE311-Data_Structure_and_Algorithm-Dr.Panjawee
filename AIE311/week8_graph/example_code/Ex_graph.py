class Graph:
    def __init__(self, num_edges):
        self.num_edges = num_edges + 1
        self.adj_matrix = [[""] * self.num_edges for _ in range(self.num_edges)]

    def create_Adjmat(self, edge):

        for row in range (0, len(self.adj_matrix)):
            for col in range (1, len(self.adj_matrix)):
                if  row == 0 and self.adj_matrix[row][col] == "" :
                    self.adj_matrix[row][col] = edge
                    self.adj_matrix[col][row] = edge
                    break
                elif row > 0 and self.adj_matrix[row][col] == "":
                     self.adj_matrix[row][col] = "0"

    def print_mat(self):
        for row in self.adj_matrix:
            print(row)
       
    
    
    def connect(self, vert1,vert2):
        idx1,idx2 =None ,None
       
        
        print()
        for i in range (1, len(self.adj_matrix)):
        
            if self.adj_matrix[i][0] == vert1 :
                idx1 = i
            elif self.adj_matrix[0][i] == vert2 :
                idx2 = i
        if idx1 != "" and idx2 != "":
            self.adj_matrix[idx1][idx2] = "1"
            self.adj_matrix[idx2][idx1] = "1"
                
    
    
    
    
    
    
    
graph1 = Graph(3)

graph1.create_Adjmat("A")
graph1.create_Adjmat("B")
graph1.create_Adjmat("C")

graph1.connect("A","C")
graph1.connect("A","B")
graph1.connect("B","C")
graph1.connect("A","A")
graph1.connect("B","B")
graph1.connect("C","C")
graph1.print_mat()


