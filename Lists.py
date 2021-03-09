def list_fun(X):
    
    if 'insert' in X:
        msg = X.split()
        lst.insert(int(msg[1]), int(msg[2]))
        #print(lst)
    
    elif 'append' in X:
        msg = X.split()
        lst.append(int(msg[1]))
    
    elif 'remove' in X:
        msg = X.split()
        lst.remove(int(msg[1]))
    
    elif 'pop' in X:
        lst.pop()
    
    elif 'print' in X:
        print(lst)
    
    elif 'sort' in X:
        lst.sort()
    
    elif 'reverse' in X:
        lst.reverse()
        
if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        X = input()
        list_fun(X)
