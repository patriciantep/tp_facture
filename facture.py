import copy
myProduit = {
    "name" : "aucun",
    "price" : 0.0 ,
    "quantity" : 0
}
priceTotal=0
listProduit = [] #on met hors de la boucle for afin d'avoir la liste complet des produits or si on met
#dans la boucle ça va montrer jusqu'à la dernière itération le dernier produit et non la liste entière
nbreProduit= int(input("combien de produit voulez-vous facturer? :"))
for i in range(0, nbreProduit):
   produitEnCours = copy.deepcopy(myProduit)
   produitEnCours["name"] = input("entrer le nom du produit : ")
   produitEnCours["price"] = float(input("entrer le prix du produit : "))
   produitEnCours["quantity"] = int(input("entrer la quantité de produit : "))
   listProduit.append(produitEnCours)
#append rajoute des elements dans un tableau
   priceTotal += produitEnCours["price"] * produitEnCours["quantity"]
   print(listProduit)
print(f'priceTotal = {priceTotal}')
















    
#TODO

#L'objectif de ce mini TP consite en la génération d'une facture. 