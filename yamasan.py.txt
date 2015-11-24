someFruits=["banana","blue berry","kiwi","pineapple", "apple"]
print( type(someFruits) )
print(someFruits[2])   # indexing
print(someFruits[-1])  # indexing
print(someFruits[:3])  # slicing
print(someFruits[1:3]) # slicing
thaiFruits=["mangosteen","mango","rose apple","rambutan"]
allFruits = someFruits + thaiFruits
print(allFruits)

japaneseFruits=["Kaki","Ume"]
japaneseFruits.append("Fuji apple")
print ( japaneseFruits )

for x in allFruits :
    print( x )