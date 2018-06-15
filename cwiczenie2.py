from collections import defaultdict
import os
import os.path
import sys

bridgesList = []
class Graph:
    
    def __init__(self,vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
        
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def findAndPrintBridge(self,u, been, father, low, time):
        son = 0
        been[u] = True
        time[u] = self.Time
        low[u] = self.Time
        self.Time += 1
 
        for v in self.graph[u]:
            if been[v] == False :
                father[v] = u
                son += 1
                self.findAndPrintBridge(v, been, father, low, time)
                low[u] = min(low[u], low[v])
                if low[v] > time[u]:
                    print ("%s %s" %(u+1,v+1))
                    bridgesList.append([u+1,v+1])
     
            elif v != father[u]: 
                low[u] = min(low[u], time[v])
                
    def bridge(self):
        been = [False] * (self.V)
        time = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        father = [-1] * (self.V)
 
        for i in range(self.V):
            if been[i] == False:
                self.findAndPrintBridge(i, been, father, low, time)

    def findArticulationPoints(self,u, been, ap, father, low, time):
        son = 0
        been[u] = True
        time[u] = self.Time
        low[u] = self.Time
        self.Time += 1
 
        for v in self.graph[u]:
            if been[v] == False :
                father[v] = u
                son += 1
                self.findArticulationPoints(v, been, ap, father, low, time)
                low[u] = min(low[u], low[v])
                if father[u] == -1 and son > 1:
                    ap[u] = True
                if father[u] != -1 and low[v] >= time[u]:
                    ap[u] = True   
                    
            elif v != father[u]: 
                low[u] = min(low[u], time[v])
 
    def AP(self, apVertices):
        been = [False] * (self.V)
        time = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        father = [-1] * (self.V)
        ap = [False] * (self.V) 
        
        for i in range(self.V):
            if been[i] == False:
                self.findArticulationPoints(i, been, ap, father, low, time)
 
        for index, value in enumerate (ap):
            if value == True: apVertices.append(index+1),
            
def program():     
    apVertices = []
    option = input("Wpisz opcję(1 - Znajdowanie mostów lub 2 - Znajdowanie punktów artykulacji lub 3 - Wyjście): ")
    if option == "1":
        while True:
            fileWithInputData = input("Plik z tekstem wejściowym: ") 
            if os.path.exists(fileWithInputData):   
                break
            else:
                print ("Plik nie istnieje, podaj inną scieżkę!")
                continue              
        with open(fileWithInputData) as fp:  
            for cnt, line in enumerate(fp):
                if cnt == 0:
                    #create Graph
                    g1 = Graph(int(line))
                else:
                    edges = line.split(" ")
                    edges = [e.replace('\n', '') for e in edges]
                    for z in edges:     
                        try:
                            i = int(z)
                            g1.addEdge(i-1, cnt-1)
                        except ValueError:
                            #Handle the exception
                            pass   
            g1.bridge()
            
            nameOfFile = input("Ścieżka do pliku wyjsciowego: ")
            file = open(nameOfFile, "w")
            first = ""
            for x in bridgesList:
                first = first + str(x[0]) + " " + str(x[1]) + "\n"
            lines = [first]    
            file.writelines(lines)
            file.close()
            os.system(nameOfFile)
            program()
    elif option == "2":
        
        while True:
            fileWithInputData = input("Plik z tekstem wejściowym: ") 
            if os.path.exists(fileWithInputData):   
                break
            else:
                print ("Plik nie istnieje, podaj inną scieżkę!")
                continue              
        with open(fileWithInputData) as fp:  
            for cnt, line in enumerate(fp):
                #print("Line {}: {}".format(cnt, line))
                if cnt == 0:
                    #create Graph
                    g2 = Graph(int(line))
                else:
                    edges = line.split(" ")
                    edges = [e.replace('\n', '') for e in edges]
                    for z in edges:     
                        try:
                            i = int(z)
                            g2.addEdge(i-1, cnt-1)
                        except ValueError:
                            #Handle the exception
                            pass   
            g2.AP(apVertices)
            print(*apVertices, sep=' ')
            nameOfFile = input("Ścieżka do pliku wyjsciowego: ")
            file = open(nameOfFile, "w")
            first = ""
            for x in apVertices:
                first = first + str(x) + " "
            lines = [first]    
            file.writelines(lines)
            file.close()
            os.system(nameOfFile)
            program()
    elif option == "3":
        sys.exit()
    else:
        print("Coś poszło nie tak, proszę wybrać 1 lub 2")
        program()      
program()
