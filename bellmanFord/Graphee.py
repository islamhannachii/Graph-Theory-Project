import math
class Graphee():
 
    def __init__(self, noeuds):
        self.matriceAdj = noeuds.copy()
 
    def Afficher(self, src, dist):
        mat = []
        for noeud in range(len(self.matriceAdj)):
                mat.append([(noeud+1), dist[noeud]])
        return mat
    def bellmanFord(self, src, ordre=False):
        ordre = self.ordre_cal()
        dist = [math.inf] * len(self.matriceAdj)
        precedence = [-1] * len(self.matriceAdj)
        dist[src-1] = 0
        precedence[src-1] = src-1
        relax = True
        iteration = 0
        while (iteration < len(self.matriceAdj)-1) and relax == True:
            relax = False
            for elm in ordre:
                if (dist[elm[1]-1] > dist[elm[0]-1]+self.matriceAdj[elm[0]-1][elm[1]-1]):
                    dist[elm[1]-1] = dist[elm[0]-1]+self.matriceAdj[elm[0]-1][elm[1]-1]
                    precedence[elm[1]-1] = elm[0]-1
                    relax = True
            iteration += 1
        
        return self.Afficher(src, dist)
    def ordre_cal (self):
        ordre = []
        for i in range(len(self.matriceAdj)):
            for j in range(len(self.matriceAdj)):
                if (self.matriceAdj[i][j]):
                    ordre.append((i+1,j+1,self.matriceAdj[i][j]))
        return ordre
    