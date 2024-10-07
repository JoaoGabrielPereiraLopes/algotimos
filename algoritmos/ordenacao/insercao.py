conjunto=[int(x) for x in input().split(' ')]
ordenado=[]
index=0
for x in conjunto:
    fim=False
    for y in range(0,len(ordenado)):
        if ordenado[y]>=x:
            fim=not fim
            index=y
            break
    if fim:
        ordenado.insert(index,x)
    else:
        ordenado.append(x)
print(ordenado)