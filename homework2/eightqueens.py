def queen(n):
    q = []
    return queens(n, q)

def queens(n, q):
    if len(q) == n:
        print (q)
        return
    for Nexty in range(n):
        if not check(Nexty, q): #判斷是否衝突
            q.append(Nexty) #將其放上棋盤
            queens(n, q) #尋找下一個皇后的擺放位置
            q.pop() #將其移出，以尋找該行的其他可能擺放位置
        
#因各皇后所在位置之x值已固定為0-7，故不需考慮直線衝突狀況
def check(Nexty, q):
    NextX = len(q)
    for x in range(len(q)):
        if q[x] == Nexty: return True  #判斷橫線是否衝突
        if abs(x - NextX) == abs(q[x] - Nexty): return True  #判斷斜線是否衝突
    return False

queen(8)