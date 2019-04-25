#Algoritma Dijkstra
#Kota Bandung graph simulation for shortest path
#Lukas Kurnia Jonathan / 13517006 
#Institute of Technology Bandung

class Kota():
    #Constructor kota
    def __init__(self, jumlahPersimpangan):
        self.node =jumlahPersimpangan
        self.graph = [[0 for column in range(jumlahPersimpangan)] for row in range(5)]
        self.namaPersimpangan = {}

    def getPersimpangan(self,idx):
        return self.namaPersimpangan[idx]

    def printGraph(self):
        for column in self.graph:
            print(column)

    def getJarakMinimum(self, listDistance, listVisited):
        min = 9999
        for i in range(self.node):
            if(listDistance[i]< min and listVisited[i]==False):
                min = listDistance[i]
                min_indeks = i

        return min_indeks

    def printAllPath(self,start,listDistance,listRute):
        print('Jarak optimum dari {} ke seluruh tempat lain: ' .format(self.getPersimpangan(start)))
        for i in range(len(listDistance)):
            print(self.getPersimpangan(i) , '=' , listDistance[i] , 'dengan rute : ' , end ='')
            for indeks in range (len(listRute[i])):
                print(self.getPersimpangan(listRute[i][indeks]), end=' ')
            print()
          
    def printPath(self,start, end, listDistance,listRute):
        print('Jarak optimum dari {} ke {} = {} ' .format(self.getPersimpangan(start),self.getPersimpangan(end), listDistance[start]))
        print('Dengan rute: ',end ='')
        for indeks in range (len(listRute[end])):
            print(self.getPersimpangan(listRute[end][indeks]), end=' ')
        print()

    def Dijkstra(self,start):
        listDistance = [99999] * self.node
        listDistance[start] = 0
        
        listRute=[]
        for i in range(self.node):
            listRute.append([])
        listVisited = [False]*self.node

        for persimpangan in range(self.node):
            u = self.getJarakMinimum(listDistance,listVisited)
            listVisited[u] = True
            listRute[u].append(u)

            for v in range(self.node):
                if self.graph[u][v] >0 and  listVisited[v] == False and listDistance[v]>listDistance[u]+self.graph[u][v]:
                    listDistance[v] = listDistance[u] + self.graph[u][v]
                    listRute[v] = listRute[u].copy()

        return listDistance,listRute



bandung = Kota(7)

bandung.namaPersimpangan[0]='Bandung'
bandung.namaPersimpangan[1]='Jakarta'
bandung.namaPersimpangan[2]='Makassar'
bandung.namaPersimpangan[3]='Semarang'
bandung.namaPersimpangan[4]='Surabaya'
bandung.namaPersimpangan[5]='Malang'
bandung.namaPersimpangan[6]='Cianjur'

# print(bandung.namaPersimpangan[5])

# bandung.graph = [[0, 4, 2, 0, 0, 0], 
#                 [4, 0, 1, 5, 0, 0], 
#                 [2, 1, 0, 8, 10, 0], 
#                 [0, 5, 8, 0, 2, 6], 
#                 [0, 0, 10, 2, 0, 3],
#                 [0, 0, 0, 6, 3, 0]
#                 ]
            
bandung.graph = [[0, 0, 5, 6, 0, 0, 0], 
                [0, 0, 0, 0, 1, 3, 0], 
                [5, 0, 0, 2, 9, 0, 3], 
                [6, 0, 2, 0, 0, 7, 7], 
                [0, 1, 9, 0, 0, 2, 9],
                [0, 3, 0, 7, 2, 0, 8],
                [0, 0, 3, 7, 9, 8, 0]
                ]

distance,rute = bandung.Dijkstra(0)
bandung.printAllPath(0,distance,rute)
bandung.printPath(0,1,distance,rute)