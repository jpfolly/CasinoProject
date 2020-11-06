import pandas as pda
import random

def premier_tirage(deck):
	tirage = random.sample(deck, 5)
	for i in tirage:
		deck.remove(i)
	return tirage, deck

def choix_cartes(tirage):
	jeu = []
	for i in tirage:
		print(i)
		choix = input('Voulez vous gardez vous cette carte ?  Sensible a la casse Oui/Non: ')
		if choix == "Oui":
			jeu.append(i)
	return jeu

def deuxieme_tirage(deck, main):
	nb_cartes = len(main)
	nb_cartes_a_prendre = 5 - nb_cartes
	new_cartes = random.sample(deck, nb_cartes_a_prendre)
	for i in new_cartes:
		main.append(i)
	return main
 
def machine():
	deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s'] 
	pt_jeu, new_deck = premier_tirage(deck)
	print(pt_jeu)
	main = choix_cartes(pt_jeu)
	tirage_final = deuxieme_tirage(new_deck, main)
	print(tirage_final)
	return tirage_final

def test_tirage(tirage):
	dic = {}
	keys = [1,2,3,4,5]
	value = []
	color = []
	for i,k in zip(tirage, keys):
		dic[k] = i.split('-')
	for key in dic.keys():
		value.append(dic[key][0])
		color.append(dic[key][1])
	return value, color
	
def convert_carte(liste):
	for e,i in zip(liste, range (0,5)):
		try:
			liste[i] = int(e)
		except:
			if e == 'J':
				liste[i] = 11
			elif e == 'Q':
				liste[i] = 12
			elif e == 'K':
				liste[i] = 13
			elif e == 'A':
				liste[i] = 1
			else:
				continue
	return liste

def quinte_flush_royale(tirage):
	valeur_gagnante = ['10' , 'J', 'Q' , 'K' , 'A']
	value, color = test_tirage(tirage)
	if sorted(valeur_gagnante) == sorted(value) and color.count(color[0]) == 5:
		return True
	else:
		return False
	
def quinte_flush(tirage):
	value, color = test_tirage(tirage)
	value = convert_carte(value)
	value = sorted(value)
	suite = []
	for e, i in zip(value[0:-1], range(len(value)-1)):
		if e+1 == value[i+1]:
			suite.append('True')
	if suite.count('True') == 4 and color.count(color[0]) == 5:
		return True
	else:
		return False

def carre(tirage):
	value, color = test_tirage(tirage)
	value1 = pda.Series(value)
	uniques = value1.unique()
	count = []
	for i in uniques:
		count.append(value.count(i))
	if len(uniques) == 2 and sorted(count) == [1, 4]:
		return True
	else:
		return False
		
def full(tirage):
	value, color = test_tirage(tirage)
	value1 = pda.Series(value)
	uniques = value1.unique()
	count = []
	for i in uniques:
		count.append(value.count(i))
	if len(uniques) == 2 and sorted(count) == [2, 3]:
		return True
	else:
		return False

def flush(tirage):
	value, color = test_tirage(tirage)
	if color.count(color[0]) == 5:
		return True
	else:
		return False

def quinte(tirage):
	value, color = test_tirage(tirage)
	value = convert_carte(value)
	value = sorted(value)
	suite = []
	for e, i in zip(value[0:-1], range(len(value)-1)):
		if e+1 == value[i+1]:
			suite.append('True')
		if suite.count('True') == 4 or value == [1, 10, 11, 12, 13]:
			return True
		else:
			return False

def brelan(tirage):
	value, color = test_tirage(tirage)
	value1 = pda.Series(value)
	uniques = value1.unique()
	count = []
	for i in uniques:
		count.append(value.count(i))
	if len(uniques) == 3 and sorted(count) ==  [1, 1, 3]:
		return True
	else:
		return False

def double_paire(tirage):
	value, color = test_tirage(tirage)
	value1 = pda.Series(value)
	uniques = value1.unique()
	count = []
	for i in uniques:
		count.append(value.count(i))
	if len(uniques) == 3 and sorted(count) == [1, 2, 2]:
		return True
	else:
		return False

def paire(tirage):
	value, color = test_tirage(tirage)
	value1 = pda.Series(value)
	uniques = value1.unique()
	count = []
	for i in uniques:
		count.append(value.count(i))
	if len(uniques) == 4 and sorted(count) == [1, 1, 1, 2]:
		return True
	else:
		return False
		

def gain(tirage_final, mise):
	if quinte_flush_royale(tirage_final) == True:  
		g = mise*250
		resultat = "Quinte Flush Royal ! Vous gagnez " +str(g) +" euros"
		return g, resultat
	elif quinte_flush(tirage_final) == True:
		g = mise*50
		resultat = "Quinte Flush ! Vous gagnez " +str(g) +" euros"
		return g, resultat
	elif carre(tirage_final) == True:
		g = mise*25
		resultat = "Carré ! Vous gagnez " +str(g) +" euros"
		return g, resultat
	elif full(tirage_final) == True:
		g = mise*9
		resultat = "Full ! Vous gagnez " +str(g) +" euros"
		return g, resultat
	elif flush(tirage_final) == True:
		g = mise*6
		resultat = "Flush ! Vous gagnez " +str(g) +" euros"
		return g, resultat
	elif quinte(tirage_final) == True:
		g = mise*4
		resultat = "Quinte ! Vous gagnez " +str(g) +" euros"
		return g, resultat
	elif brelan(tirage_final) == True:
		g = mise*3
		resultat = "Brelan ! Vous gagnez " +str(g) +" euros"
		return g, resultat
	elif double_paire(tirage_final) == True:
		g = mise*2
		resultat = "Double Paire ! Vous gagnez " +str(g) +" euros"
		return g, resultat
	elif paire(tirage_final) == True:
		g = mise*1
		resultat = "Paire ! Vous gagnez " +str(g) +" euros"
		return g, resultat
	else:
		g = 0
		resultat = "Vous avez perdu !"
		return g, resultat


def partie(mise, bankroll):
	main = machine()
	g, resultat = gain(main, mise)
	bankroll = bankroll - mise
	bankroll += g
	return resultat, bankroll

def video_poker():
	bankroll = int(input("Veuillez aprovisionner votre compte: "))
	mise_joueur = int(input("Votre mise est: "))
	test = 
	while bankroll - mise_joueur >= 0:
		resultat, bankroll = partie(mise_joueur, bankroll)
		print(resultat)
		print("Bank: " + str(bankroll))
		if bankroll == 0:
			print("Game Over")
			break
		else:
			mise_joueur = int(input("Votre mise: "))
			if bankroll - mise_joueur <0:
				print("Vous n'avez pas assez d'argent")
				mise_joueur = int(input("Votre mise: "))
	
video_poker()
