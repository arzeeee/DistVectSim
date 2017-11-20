### ----Routing Table----	###
### By Natus Vincere		###


nNode = input("Masukkan jumlah node: ")
NodeKe = {}                                 #Inisialisasi dictionary node
for i in range(nNode):						#Inisiasi list tetangga kosong
  NodeKe[i+1] = []

for i in range(nNode):						#Inisialisasi node bertetangga
  NodeT = input("Masukkan node yang bertetangga dengan node "+str(i+1)+" :")
  for j in range(len(NodeT)):
    NodeKe.setdefault(i+1,[]).append(NodeT[j])
  
print(NodeKe)

