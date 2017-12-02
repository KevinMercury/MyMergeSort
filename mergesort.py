def mergeSort(lst):
  if(len(lst) <= 1): return lst
  mid = int(len(lst) / 2)
  lstLeft = mergeSort(lst[:mid])
  #print("LEFT ",lstLeft)
  lstRight = mergeSort(lst[mid:])
  #print("RIGHT ",lstRight)
  return merge(lstLeft + lstRight, mid)
  
def merge(lst,mid):
  #print(mid)
  newLst = []
  i = 0
  j = mid
  while(i < mid and j <= len(lst) - 1):
    if(lst[i] < lst[j]):
      newLst.append(lst[i])
      i = i + 1
    else:
      newLst.append(lst[j])
      j = j + 1
  
  while(i < mid):
    newLst.append(lst[i])
    i = i + 1
    
  while(j <= len(lst) - 1):
    newLst.append(lst[j])
    j = j + 1
    
  #print("MERGE ",newLst)
  return newLst


lst = [8,3,4,9,2,6,1,5,0]
newLst = mergeSort(lst)
print(newLst)
