import pandas

df = pandas.read_csv("1/matrix.csv", sep=",")

primeDiagonalSum = 0
for ind in df.index:
    primeDiagonalSum+=df[str(ind)][ind]
print(primeDiagonalSum)

secondaryDiagonalSum = 0
for ind in df.index:
    reverseInd = len(df.index) - ind - 1
    secondaryDiagonalSum+=df[str(ind)][reverseInd]
print(secondaryDiagonalSum)
