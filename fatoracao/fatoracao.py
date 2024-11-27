def fatores(n):
    fatores={}
    for x in range(2,n+1):
        contagem=0
        while n%x==0:
            contagem+=1
            n=n//x
        if contagem:
            fatores[x]=contagem
    return fatores