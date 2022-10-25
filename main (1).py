from random import randint
import time

vertices = 100
arestasMin = 0
arestasMax = 3

repetições = 1

randintMin = 1
randintMax = 1000

arr=[]
arrClone=[]

print('Devito a alguma limitação, quando usado mais de 100 vertices o .txt não é preenchido com os dados calculados')
for repet in range(repetições):
  
  start_time = time.time()
  
  for y in range(vertices):
    
    arrTemp=[]
    arrTemp.append(randint(randintMin,randintMax))
    for x in range(randint(arestasMin,arestasMax)):
      arrTemp.append(randint(randintMin,randintMax))
    arr.append(arrTemp)


  
  #print(arr)
  

  arrVertices=[]
  teste=[]
  arrClone=arr
  for x in range(len(arr)):
    arrVertices.append(arr[x][0])

    
  for x in range(len(arr)): # 0 a 9
    for y in range(1,len(arr[x])):
      if arr[x][y] in arrVertices:
        index_pos_list = [ i for i in range(len(arrVertices)) if arrVertices[i] == arr[x][y] ]
      else:
        index_pos_list=[]
      newarr=[]
      teste.append(index_pos_list)
      for z in range(len(index_pos_list)):
        newarr=arr[index_pos_list[z]]+newarr
        arr[x][y]=newarr
      index_pos_list=[]

  teste2=[]
  teste = [x for x in teste if x]

  
  for x in range(len(teste)):
      for y in range(len(teste[x])):
        teste2.append(teste[x][y])
  teste2=list(set(teste2))
  teste2.sort()
  
  index=0
  varr2=0
  while index < (len(teste2)):
    arr.pop(teste2[index]+varr2)
    index=index+1
    varr2=varr2-1
  #print('')
  print(arr)

  print("--- %s seconds ---" % (time.time() - start_time)) 
  with open('lista_adjacencias.txt', 'w') as f:
    f.write('O primeiro elemento de cada lista (incluindo uma dentro da outra) representa um vertice, e os elementos seguintes, representam suas arestas')
    f.write('')
    f.write(str(arr))
  
  
