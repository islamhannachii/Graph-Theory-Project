import math
from .Graphee import Graphee
 
# Test
# les sommets sont numérotés à partir de 1
# matriceAdj = [[0, 7, 0, 5, 0, 0, 0,0],
#               [0, 0, 0, -3, 4, 2, 0,0],
#               [0, 5, 0, 7, 0, 4, 0,0],
#               [0, 0, 0, 0, 5, 3, 0,0],
#               [0, 0, 0, 0, 0, 0, 4,0],
#               [0, 0, 0, 0, 0, 0, 7,0],
#               [0, 0, 0, 0, 0, 0, 0,1],
#               [0, 0, 0, 0, 0, 0, 1,0],
#               ]
# ordre = [(1, 2), (1, 3), (1, 4), (3, 2), (2, 5),
#          (3, 5), (4, 3), (4, 6), (6, 7), (5, 7)]
# ordre = []
# for i in range(len(matriceAdj)):
#     for j in range(len(matriceAdj) - 1):
#         if (matriceAdj[i][j]):
#             ordre.append((i+1,j+1))
# print(ordre)
# g = Graphebell(matriceAdj)
# g.bellmanFord(1)                    