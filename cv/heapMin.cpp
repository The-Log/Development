int main(){
  return 0;
}
struct minHeap{
  int size;
  int miniHeap[size];
  int pos = 0;
  void makeHeap(int listA[]){
    if(listA.size() > 0){
        for (i = 0; i < listA.size(); i++) {
          insert(listA[i]);
        }
    }
  }
  void insert(int x){
    if(pos == 0){
      miniHeap[pos + 1] = x;
      pos = 2;
    }
    else{
      miniHeap[pos] = x;
      pos = pos + 1;
      bubleUp();
    }
  }
  void bubleUp(){
    p1 = pos;
    while(p1 > 0 && miniHeap[p1/2] > miniHeap[p1]){
      y = miniHeap[p1];
      miniHeap[p1] = miniHeap[p1/2];
      miniHeap[p1/2] = y;
    }
  }
  void sinkDown(int x){
    int a = miniHeap[k];
    smallest = k;
    if(2*k < pos && miniHeap[smallest] > miniHeap[2*k]){
    }
    if(2*k+1 < pos && miniHeap[smallest] > miniHeap[2*k+1]){
    }
    if(smallest != k)
      swap(k,smallest);
      sinkDown(smallest);
  }
  void swap(int x, int y){
    temp = miniHeap[x];
    miniHeap[x] = miniHeap[y];
    miniHeap[y] = temp;
  }
  int extractMin(){
    int minimum = miniHeap[1];
    miniHeap[1] = miniHeap[pos-1];
    miniHeap[pos-1]= 0;
    pos = pos - 1;
    sinkDown(1);
    return minimum;
  }
}
