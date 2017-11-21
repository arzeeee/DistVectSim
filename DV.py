### ----Routing Table----	###
### By Natus Vincere		###



def InputNodeNeighbor():
  NodeT = input("Masukkan node yang bertetangga dengan node "+str(i+1)+" :")
  for j in range(len(NodeT)):
    if (NodeT[j]==nNode):
  	  print("Tidak bisa bertetangga dengan node sendiri")
  return NodeT


nNode = input("Masukkan jumlah node: ")
Node = {}                                 #Inisialisasi dictionary node
for i in range(nNode):						#Inisiasi list tetangga kosong
  Node[i+1] = []


for i in range(nNode):						#Inisialisasi node bertetangga
  NodeT = input("Masukkan node yang bertetangga dengan node "+str(i+1)+" :")
  # for j in range(len(NodeT)):
  #   if (NodeT[j]==nNode):
  # 	  print("Tidak bisa bertetangga dengan node sendiri")
  for j in range(len(NodeT)):
    Node.setdefault(i+1,[]).append(NodeT[j])

nSkenario = input("Masukkan jumlah skenario: ")
Skenario
for i in range(nSkenario):

  
print(Node)

