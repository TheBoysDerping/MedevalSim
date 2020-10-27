#THIS IS COMPLETE. DO NOT CODE IN IT MORE!









# DONT DELETE THIS
import random, sys
if len(sys.argv) - 1:
    random.seed(int(sys.argv[1]))
#########################################################
restarttimes = 0

print("WELCOME!")
print("Please take a seat, we have much to discuss.")

print("What is your name stranger?")
name = (input())
print(f"So your name is {name} eh?")

print("We are going to do a simulation. Be ready.")

print("Hit Enter to Choose your Weapon, Armor, and Pet!")
input()
weapon = ("Sword", "Knife", "Bow", "Wizard Staff", "Spell Book", "Throwing Stars")
armor = ("Leather", "Steel", "Chainmail", "No")
pet = ("Wolf", "Cat", "Bird", "No", "Horse")
Chosenweapon = (random.choice(weapon))
Chosenarmor = (random.choice(armor))
Chosenpet = (random.choice(pet))
chosenpethp = (random.randrange(0,11))
chosenhp = (random.randrange(9, 21))
nopet=("No")

print(f"your weapon is a {Chosenweapon}")
print(f"Your armor is {Chosenarmor} armor")
print(f"you have {chosenhp} hp")
if Chosenpet not in nopet:
	print(f"your pet is a {Chosenpet} and has {chosenpethp} hp")
else:
	print("You have no pet")

if Chosenarmor == "Leather":
    print("Your armor gives you a 2 Hp Bonus")
    chosenhp += 2
    print(f"You have {chosenhp} total hp")
if Chosenarmor == "Chainmail":
    print("Your armor gives you a 4 Hp Bonus")
    chosenhp += 4
    print(f"You have {chosenhp} total hp")
if Chosenarmor == "Steel":
    print("Your armor gives you a 8 Hp Bonus")
    chosenhp += 8
    print(f"You have {chosenhp} total hp")
if Chosenarmor == "No":
    print("Your armor gives you no Hp Bonus")
    print(f"You have {chosenhp} total hp")
print("Hit enter to start the sim.")
input()
print()

enemy1 = ("Goblins", "Human Sized Chickens", "Vampires", "Random Villagers")
chosenenemy1 = (random.choice(enemy1))
print(
    f"As you are walking down a trail you encounter a group of {chosenenemy1}")
print(f"What do you do? You can attack, run like a coward, or Scream like a little girl and sacrafice yourself to the {chosenenemy1}. Say attack, run or scream based on what you want. NO CAPITALS.")
ifrepeat1 = 1
validresponses =('attack','run','scream')

while ifrepeat1 == 1 or ifrepeat1 == 2:
	decision1 = input()
	if decision1 not in validresponses:
		print("INVALID RESPONSE. PLEASE TRY AGAIN")
		ifrepeat1 = 2
	if decision1 == "run":
		ifrepeat1 = 0
		print( f"you ran like a coward and arrived at the nearest village where you spent the next few days until the {chosenenemy1} have left")
	elif decision1 == "attack":
		print("hit enter to roll a D10 to determine if you kill them without damage or of you kill them and get hit")
		input()
		killorno=random.randint(1,10)
		print(f"You attack the {chosenenemy1} with your {Chosenweapon}")
		if killorno >=5:
			print("You killed them and took no damage")
		else:
			print("You killed them and took 4 damage")
			chosenhp -= 4
		ifrepeat1 = 0
	elif decision1 == "scream":
		print(f"you run towards the {chosenenemy1} screaming and hand them your {Chosenweapon}, allowing them to kill you with it.")
		ifrepeat1 = 0
		afterlife2 = (random.randint(1, 2))
		if afterlife2 == 1:
			print(
      "you wake up in heaven, and you are treated to the smell of your mothers cookies and spend the rest of eternity happy"
      )
		if afterlife2 == 2:
			print(
        "You wake up in hell, are treated to the smell of crap, and are tortured and misrable for eternity")
			exit()
print("")
print("The next morning...")
print()
print(f"you wake up and get ready for the day and head out on a shopping run. As you approach the store you see a man dressed in all black robbing the shopkeeper. He sees you as you pull out your {Chosenweapon} and tries to attack you. You dodge his first attack. Roll a D10 to determine how much damage you do.")
input("Hit Enter to roll")
robberhp=10
while robberhp != 0 and robberhp >= 0:
	if robberhp != 0:

		robberattackroll = random.randint(1,10)
		robberhp-=robberattackroll
		if robberhp <=0:
			robberhp=0
		print(f"You did {robberattackroll} damage to the robber he now has {robberhp} health left")
		input()
		print ("the robber attacks and does 2 damage to you")
		chosenhp -= 2
	if robberhp == 0:
		print ("You have knocked out the robber, You take him to the Sherrif and turn him in")
print()

print("You buy your groceries and head home and fall asleep on your bed")

print()
print ("you awake in bed, having slept good that night you felt refreshed and ready for anything. When all of a sudden you hear a loud ROAR from inside the neaby cave.")
print("...")
print()
print(
    f"you walk towards the cave when you see flames erupting from it. As you get closer you see more of those pesky {chosenenemy1} gaurding the enterance. Do you attack them or run like a coward. say attack or run based on your decision.")
ifrepeat2=1

attk_run = input()

while ifrepeat2 ==1 or ifrepeat2 == 2:
	if attk_run not in validresponses:
		print("INVALID RESPONSE. PLEASE TRY AGAIN")
		attk_run = input()
		ifrepeat2 = 2

	if attk_run == "run":
		ifrepeat2 = 0
		print(f"You get shot by one of the {chosenenemy1} by a bow and die")
		chosenhp = 0
	if chosenhp <= 0:
			print("You died")
			print()
			afterlife = (random.randint(1, 2))
			if afterlife == 1:
				print("you wake up in heaven, and you are treated to the smell of your mothers cookies and 	spend the rest of eternity happy")
				exit()
			if afterlife == 2:
				print("You wake up in hell, are treated to the smell 	of crap, and are tortured and misrable for eternity")
				exit()
	if attk_run == "attack":
		ifrepeat2 = 0
		print(f"You charge the {chosenenemy1}. Roll a D10 to see if you kill all of them, if you get five or above  you kill them, if you dont you get hit and then kill them. Press enter to roll the D10")
		input()
		hitorkill = 0
		while hitorkill <= 0:
			hitorkill = (random.randint(1, 10))
			print(f" you rolled a {hitorkill}")
			if hitorkill <= 4:
				hitcounter = (random.randrange(0, 5))
				chosenhp - hitcounter
				print(f"you have {chosenhp} health left.")
			else:
				print(f"you killed the {chosenenemy1}")
print()
print(
    'you have successfully killed all of them. As you enter the cave you see it, A dragon... You try to stealthily approach it as it is sleeping. As you go to attack it wakes up and smackes you with its tail. Then you get back up. "Whats the worst that could happen." You say to yourself as you go to fight the dragon.'
)
dragonhp = int(100)
print()
print(
    "You Need to roll a D10 to determine how much damage you do to the dragon. It has 100 hp so whatever you roll will be doubled"
)
while dragonhp >= 0 and dragonhp != 0:
	input()
	damagetodragon = random.randint(10, 20)
	damagetodragon *= 2
	print(f"you rolled a {damagetodragon}")
	print(f"You did {damagetodragon} to the dragon")
	dragonhp -= damagetodragon
	print(f"The dragon now has {dragonhp} health")
	print("You took 3 damage from the dragon")
	chosenhp -= 3
	if Chosenpet not in nopet:
		print(f"Your pet {Chosenpet} did 10 damage to the dragon")
		dragonhp -= 10
	print(f"you have {chosenhp} left")
	if chosenhp <= 0:
		print("You died")
		print(f"The dragon killed you with {dragonhp} left")
		print()
		afterlife = (random.randint(1, 2))
		if afterlife == 1:
			print("you wake up in heaven, and you are treated to the smell of your mothers cookies and spend the rest of eternity happy")
			exit()
		if afterlife == 2:
			print("You wake up in hell, and you are imeadiatly greeted by demons and are tortured and misrable for eternity")
			exit()
if dragonhp <= 0:
	print("You killed the dragon! It landed on top of you. You died because of being crushed along with your pet")
	print()
	afterlife = random.randint(1, 2)
	if afterlife == 1:
		print(f"you wake up in heaven, and you are treated to the smell of your mothers cookies and spend the rest of eternity happy. Your pet {Chosenpet} is there too!")
	if afterlife == 2:
		print("You wake up in hell, and you are imeadiatly greeted by demons and are tortured and misrable for eternity")
print()
print("THE END")