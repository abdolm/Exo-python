# import turtle

# Ceci est un commentaire, les commentaires sont ignorés par l'ordinateur.
# Ils sont ici pour permettre aux développeur de garder leur code compréhensible 
# (pour eux même ou pour les autres)

# turtle.speed(8) # permet de régler la vitesse d'animation de la tortue (1 étant le plus lent, 10 le plus rapide)

# Début des instructions permettant de dessiner : insérer votre code ici !

# turtle.forward(100) # Ici une instruction permettant d'avancer de 200px
# turtle.left(90) # Ici une instruction permettant de dessiner un cercle de rayon 30px
# turtle.forward(100) # Ici une instruction permettant d'avancer de 200px
# turtle.right(90)
# turtle.forward(-100) # Ici une instruction permettant d'avancer de 200px
# turtle.left(90) # Ici une instruction permettant de dessiner un cercle de rayon 30px
# turtle.forward(-100) # Ici une instruction permettant d'avancer de 200px

# fin des instruction permettant de dessiner.

# turtle.done() # permet d'indiquer à la tortue que nous avons fini le dessin


# turtle.speed(8)

# turtle.forward(100) # Ici une instruction permettant d'avancer de 200px
# turtle.left(72) # Ici une instruction permettant de dessiner un cercle de rayon 30px
# turtle.forward(100) # Ici une instruction permettant d'avancer de 200px
# turtle.left(72)
# turtle.forward(100) # Ici une instruction permettant d'avancer de 200px
# turtle.forward(100)
# turtle.left(72)
# turtle.forward(100)



# turtle.done()

# turtle.speed(8)

# turtle.forward(100) # Ici une instruction permettant d'avancer de 200px
# turtle.left(90) # Ici une instruction permettant de dessiner un cercle de rayon 30px
# turtle.forward(100) # Ici une instruction permettant d'avancer de 200px
# turtle.left(135)
# turtle.forward(140) # Ici une instruction permettant d'avancer de 200px
# turtle.goto(100,0)
# turtle.left(135)
# turtle.forward(100) 
# turtle.left(-45)
# turtle.forward(-140) # Ici une instruction permettant d'avancer de 200px
# turtle.goto(100,-10)

# turtle.forward(100)



# turtle.done()



# ans = input("Type the miles disatnce you want to convert in km: ")
# miles = int(ans)
# km = miles * 1.6
# print(f"{miles} miles est équivalent à {km} km")

# number = int(input("Entrez un nombre "))

# if(number % 2 != 0):
#     # code qui s'exécute si nbUtilisateur est plus petit que 0
#     print("Votre nombre est IMPAIRE")
# else:
#     # sinon, c'est ce code qui s'exécute
#     print("Votre nombre est PAIRE !")


# nb1 = int(input("Entrez le premier nombre "))
# nb2 = int(input("Entrez le deuxieme nombre "))
# nb3 = int(input("Entrez le troixieme nombre "))
# if nb1 > nb2 and nb1 > nb3:
#     # si nb1 > nb2 et nb2 > nb3 alors on exécute ce code
#     print("nb1 est le nombre le plus grand !")
# elif nb2 > nb1 and nb2 > nb3:
#     # sinon, si nb1 < nb2 et nb2 < nb3 alors on exécute ce code
#     print("nb2 est le nombre le plus grand !")
# else:
#     # sinon, on exécute celui-ci
#     print("nb3 est le nombre le plus grand !")


# nb = int(input("Entrez un nombre entier : "))

# def my_function(nombre):
#     """fonction qui verifie si un nombre est paire ou impaire

#     Args:
#         nombre (int): le nombre que l'on souhaite verifier
#     """
#     if nombre % 2 == 0:
#         print("le nombre est pair")
#     else:
#         print("Le nombre est impair")


# my_function(nb)

# nb = int(input("Entrez un nombre entier : "))

# def est_pair(nombre:int)-> bool:
#     """fonction qui verifie si un nombre est paire ou impaire

#     Args:
#         nombre (int): le nombre que l'on souhaite verifier.

#     Returns:
#         The return value. True for success, False otherwise.

#     """
#     if nombre % 2 == 0:
#         return True
#     else:
#         return False


# est_pair(nb)

# nb1 = int(input("Entrez le premier nombre "))
# nb2 = int(input("Entrez le deuxieme nombre "))
# nb3 = int(input("Entrez le troixieme nombre "))
# def lepluspetit(nombre1:int, nombre2:int, nombre3:int)-> int:
#  """fonction qui trouve le petit nombre

# #     Args:
# #         nb1,nb2,nb3 (int): les nombre que l'on souhaite comparer.

# #     Returns:
# #         le plus petit nombre
# #     """
#  if nombre1 < nombre2 and nombre1 < nombre3:
#     # si nb1 < nb2 et nb2 < nb3 alors on exécute ce code
#     print(f"{nombre1} est le nombre le plus petit !")
#  elif nombre2 < nombre1 and nombre2 < nombre3:
#     # sinon, si nb2 < nb1 et nb2 < nb3 alors on exécute ce code
#     print(f"{nombre2} est le nombre le plus petit !")
#  else:
#     # sinon, on exécute celui-ci
#     print(f"{nombre3} est le nombre le plus petit !")

# lepluspetit(nb1,nb2,nb3)

# def absolu(number1, number2):
#      """fonction donne le nombre absolu de la multiplication

#     #     Args:
#     #         number1,number2: les nombres dont on souhaite obtenir la valeur absolu
#     #     Returns:
#     #         la valeur absolu de la multiplication
#     #     """
#      if number1 < 0:
#             number1 = -number1
#      if number2 < 0:
#             number2 = -number2
#      return number1 * number2      

# print(absolu(10,-5))

# def moyenne(nb1,nb2,nb3):
#     """fonction qui donne la moyenne des trois nombres

#         Args:
#             nb1,nb2,nb3: les nombres dont on souhaite obtenir la moyenne
#         Returns:
#             la moyenne
#     """
#     list = [nb1,nb2,nb3]
#     resultat = sum(list)
#     return resultat/3

# print(moyenne(20,10,15))
# def triangle_motif(n,motif) :   
#     for i in range (1,n+1):
#         s=''
#         for j in range(1,i+1):
#             s+=motif
#         print(s)
# triangle_motif(7,"#")

# def somme(nb1,nb2,nb3,nb4) :
#     list = [nb1,nb2,nb3,nb4]
#     resultat = sum(list)
#     print (resultat)


# somme(10 ,45, 20, 10)
# def boucle4():
#     for i in range(1,101):
#         if i % 3 == 0:
#             print("Fizz")

#         elif i % 5 == 0:
#             print("Fuzz")
        
#         else: 
#             print(i)

# boucle4()

def inverse(liste):
    # reverse the order of list elements
    liste.reverse()


    print('Reversed List:', liste)
prime_numbers = [2, 6, 5, 18]
inverse(prime_numbers)