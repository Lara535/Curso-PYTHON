# while
i = 1

while i <= 8:
    print(i)
    i += 1


# for
cores = ["azul", "verde", "preto"]

for cor in cores:
    print(cor)


# break
i = 0

while True:
    print(i)
    i += 1

    if i == 5:
        break

# continue
for i in range(10):

    if i %2 ==  0: # se ele for PAR, continue contando
        continue
    print(i)

# pass (nada acontece)
for i in range(5):
    pass