#Algoritma Dijkstra
#Kota Bandung graph simulation for shortest path
#Lukas Kurnia Jonathan / 13517006 
#Institute of Technology Bandung

class Kota():
    #Constructor kota
    def __init__(self, jumlahPersimpangan):
        self.node =jumlahPersimpangan
        # self.graph = [[0 for column in range(jumlahPersimpangan)] for row in range(5)]
        self.graph =[]
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
            print((i+1),self.getPersimpangan(i) , '=' , listDistance[i] , 'dengan rute : ' )
            for indeks in range (len(listRute[i])):
                print('-', self.getPersimpangan(listRute[i][indeks]))
           
          
    def printPath(self,start, end, listDistance,listRute):
        print('Jarak optimum dari {} ke {} = {} ' .format(self.getPersimpangan(start),self.getPersimpangan(end), listDistance[end]))
        print('Dengan rute: ')
        for indeks in range (len(listRute[end])):
            print('-', self.getPersimpangan(listRute[end][indeks]))

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

bandung = Kota(16)
bandung.namaPersimpangan[0]='Rumah Penulis'
bandung.namaPersimpangan[1]='Alun-alun kota Bandung'
bandung.namaPersimpangan[2]='Perempatan Cibaduyut – Leuwi Panjang'
bandung.namaPersimpangan[3]='Perempatan Moh. Toha – Soekarno-Hatta'
bandung.namaPersimpangan[4]='Pertigaan Leuwi Panjang - Peta'
bandung.namaPersimpangan[5]='Perempatan Kopo – Soekarno-Hatta'
bandung.namaPersimpangan[6]='Perempatan Peta – Kopo'
bandung.namaPersimpangan[7]='Pertigaan Pasir Koja – Kopo'
bandung.namaPersimpangan[8]='Pertigaan Pasir Koja – Astana Anyar'
bandung.namaPersimpangan[9]='Perempatan Pungkur – Otista'
bandung.namaPersimpangan[10]='Perempatan Peta – Inhoftank'
bandung.namaPersimpangan[11]='Perempatan BKR – Moh. Toha'
bandung.namaPersimpangan[12]='Pertigaan Moh. Toha – Pungkur'
bandung.namaPersimpangan[13]='Pertigaan Dewi Sartika – Pungkur'
bandung.namaPersimpangan[14]='Perempatan Asia Afrika – Otista'
bandung.namaPersimpangan[15]='Perempatan Sudirman – Astana Anyar'


bandung.graph = [
                [0, 0, 1700, 1800, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 500, 0],
                [1700, 0, 0, 1700, 1000, 650, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1800, 0, 1700, 0, 0, 0, 0, 0, 0, 0, 0, 1200, 0, 0, 0, 0], 
                [0, 0, 1000, 0, 0, 0, 200, 0, 0, 0, 700, 0, 0, 0, 0, 0],
                [0, 0, 650, 0, 0, 0, 1200, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 200, 0, 0, 1200, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 180, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 450, 0, 0, 0, 0, 0, 750],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1100, 0, 350, 250, 0, 0],
                [0, 0, 0, 0, 700, 0, 0, 0, 0, 0, 0, 300, 0, 0, 0, 0],
                [0, 0, 0, 1200, 0, 0, 0, 0, 0, 0, 300, 0, 1100, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 350, 0, 0, 0, 120, 0, 0],
                [0, 750, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 700, 0, 0, 0, 0, 0, 650],
                [0, 0, 0, 0, 0, 0, 0, 0, 750, 0, 0, 0, 0, 0, 0, 0]
                ]

distance,rute = bandung.Dijkstra(0)
bandung.printAllPath(0,distance,rute)
# bandung.printPath(0,1,distance,rute)