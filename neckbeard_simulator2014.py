#Neckbeard Simulator 2014 v1.0
#For LPTHW ex36
#started 3.07.2014
#finished 5.07.2014

from sys import exit

inventory = []

print ""
print "_____________________"
print "|NECKBEARD SIMULATOR|"
print "--------2014---------"

print """
You are a 20-something year old washed out high school graduate who still lives in his
parents' basement. Your piss bottles are all filled up and you ran out of gaming fuel,
plus your old school Xbox decided to break. It's time for the monthly upstairs visit.
You gently stroke your neckbeard and get up from your dusty sofa. 

Once you have all the things you need, return to the basement to win the game.

The things you need: empty bottles, mountain dew, doritos, funds. You also need to have no
xbox on you.

NOTE: You can check your inventory at any time by writing 'inventory'
NOTE2: In order to interact with the game just type out the name of the thing you want to interact
with. No need for verbs.
NOTE3: Type exit to leave at any time.
"""

print "You're standing up near your old trusty sofa."
print "The LCD TV your parents bought you a few years ago is on the 'Failed to add funds' screen" 
print "on the Xbox Marketplace. You should ask your mom for some money."
print "Your piss bottles are all filled up, so you should drain them in the upstairs toilet." 
print "You also notice your old Xbox in the corner, near your empty Doritos bags and Mountain Dew bottles."
print "Something in it broke and it refuses to load games."
print "You should hand it over to your dad, he could fix it." 
print "The flight of stairs leading to the groundfloor is in the upper righthand corner of the basement."
print "What do you do?"



def basement():	
		
	bsnext = raw_input("> ")
	
	if bsnext == "xbox":
		print "It's your old broken xbox! You pick it up and add it to your inventory."
		inventory.append("xbox")
		basement()
	elif bsnext == "doritos":
		print "Seems like your gamer fuel ran out. Better restock!"
		basement()
	elif bsnext == "piss bottles":
		print "Your 5 piss bottles. Seems like they're all full."
		print "You pick them up and add them to your inventory."
		inventory.append("piss bottles")
		basement()
	elif bsnext == "tv":
		print "Your LCD TV. Pretty much the only light you see on a daily basis."
		basement()
	elif bsnext == "stairs" or bsnext == "upstairs":
		print "You slowly inch over to the stairs and begin The Climb."
		print "Once upstairs, you find yourself in the hallway."
		print "You see the door to the Outside World and a window. The sun is shining way too bright."
		print "The doors to the living room and the kitchen are also here, as well as the stairs going to "
		print "the first and only floor of the house."
		print "What do you do?"
		hallway()
	elif bsnext == "inventory":
		inventory_show()
		basement()
	elif bsnext == "exit":
		exit(0)
	else:
		print "Sorry friend, try again."
		basement()
		
def hallway():
    
	hnext = raw_input('> ')
	
	if hnext == "outside":
		print "'Outside? I could never leave this house!'"
		hallway()
	elif hnext == "window":
		print "'The glow of the sun.. absolutely disgusting.'"
		hallway()
	elif hnext == "upstairs":
		print "'My parents' dwelling place. I better not invade their privacy.'"
		hallway()
	elif hnext == "downstairs":
		print "You retreat back into your basement."  
		if 'piss bottles' in inventory and 'xbox' in inventory:
			print "You got your bottles and your xbox, not much else to do here."
			print "You head back upstairs."
			hallway()
		elif 'piss bottles' in inventory and 'xbox' not in inventory:
			print "You have your  bottles but you should also grab your xbox."
			basement()
		elif 'piss bottles' not in inventory and 'xbox' not in inventory and 'empty bottles' in inventory and 'funds' in inventory and 'doritos' in inventory and 'mountain dew' in inventory:
			endgame()
		elif 'piss bottles' not in inventory and 'xbox' in inventory:
			print "You have your xbox but your smelly piss bottles are still here."
			basement()
		elif 'piss bottles' not in inventory and 'xbox' not in inventory:
			print "Did you really just forget both your piss bottles and your xbox? Step it up, neckbeard!~"
			basement()
		else:
			exit(0)
	elif hnext == "kitchen":
		print "You slowly open the kitchen door and enter."
		print "Your mom is washing the dishes from what was presumably breakfast."
		print "The drawer where the Doritos are is opened and you can see the bags inside."
		print "The fridge is right next to your mom, the Mountain Dew is probably there."
		print "The door to the bathroom is the corner of the room."
		print "What do you do?"
		kitchen()
	elif hnext == "living room":
		print "You make your way into the living room."
		print "Inside, your father is sitting in his armchair watching Friends reruns on the family TV."
		print "There's not much else of interest in this room."
		print "What do you do?"
		living_room()
	elif hnext == "inventory":
		inventory_show()
		hallway()
	elif hnext == "exit":
		exit(0)
	else:
		print "I don't understand you."
		hallway()
	
def kitchen():
	
	knext = raw_input('> ')
	
	if knext == "mom" and 'funds' not in inventory:
		inventory.append('funds')
		print "You: Hello mother. I would like to inquire about adding more funds to my credit card."
		print "Mom: S-sure son, what for?"
		print "You: Oh, you ignorant woman. The new Call of Duty DLC, obviously!"
		print "Mom: O-oh right. Well, you'll have the money in a few hours."
		print "You: Thank you, life-giver."
		print "Mom: L-love you.\n"
		print "Well, that's taken care of. You add 'funds' to your inventory. What do I do now?"		
		kitchen()
	elif knext == "mom" and 'funds' in inventory:
		print "You: Hello again, life-giver."
		print "Mom: H-hi son.."
		print "'Nothing else to discuss with her.'"
		kitchen()
	elif knext == 'drawer':
		print "You peek inside the drawer. Apart from Doritos, it's chock full of 'healthy' stuff, "
		print "like Fitness cereal or apples. 'Plebian food', you think to yourself."
		print "What do you get?"
		drawer()
	elif knext == 'bathroom':
		print "You walk over to the bathroom's door."
		print "You find the same old blue tiled bathroom."
		print "The toilet, the sink, the drawers, the shower. Your old razor is resting on the sink."
		if 'piss bottles' in inventory:
			print "You should empty those piss bottles in the toilet."
		else:
			print "This is probably where you would have emptied your piss bottles, if you had them."
		print "What do you do?"
		bathroom()
	elif knext == 'fridge':
		print "You don't even bother looking at all the useless food your parents buy."
		print "You clearly see your target: the three 2 liter Mountain Dew bottles."
		print "The fruits, cream, ham, not even the chocolate; none of them seem interesting to you."
		print "I think you know what you must do."
		fridge()
	elif knext == 'hallway':
		print "You head back into the hallway."
		hallway()
	elif knext == "inventory":
		inventory_show()
		kitchen()
	elif knext == "exit":
		exit(0)
	else:
		print "Can't understand you."
		kitchen()
	

def living_room():
	
	lvnext = raw_input('> ')
	
	if lvnext == 'tv':
		print ">2014"
		print ">friends reruns"
		print "shiggy, life-gifter."
		living_room()
	elif lvnext == 'dad' and 'xbox' in inventory:
		print "You: Hello, life-gifter."
		print "Dad: Wow, you actually came out of the basement. Why?"
		print "You: Very funny, father. I would like to ask you if you could fix my old xbox."
		print "Dad: Your old xbox? Did you break it or what?"
		print "You: I have absolutely no idea, it just decided to stop functioning."
		print "Dad: Sure, I'll try to fix it."
		print "You: Thank you, life-gifter. Here is-"
		print "Dad: Son, you haven't said the magic word :-)."
		print "You: 'You cannot be serious..."
		father()
	elif lvnext == 'dad' and 'xbox' not in inventory:
		print "You: Hello, life-gifter."
		print "Dad: Hey son. Out to get some air?"
		print "You: [mumbling in neckbeard] Very funny.."
		living_room()
	elif lvnext == "inventory":
		inventory_show()
		living_room()
	elif lvnext == 'exit':
		exit(0)
	elif lvnext == 'hallway':
		print "You head back into the hallway."
		print "And obviously, you find yourself in the hallway. What do you do?"
		hallway()
	else:
		print "Didn't quite catch that."
		living_room()
		
	
def drawer():
	
	dnext = raw_input('> ')
	
	if dnext == 'doritos':
		inventory.append('doritos')
		print "You grab 3 bags of plain Doritos and 5 bags of the spicy ones. Tasty!"
		print "All done with the drawer! What do you do next?"
		kitchen()
	elif dnext == 'cereal':
		print "'Cereal? FOR WHAT PURPOSE??'"
		drawer()
	elif dnext == 'apples':
		print "'Who the hell eats fruit, shiggy.'"
		drawer()
	elif dnext == "inventory":
		inventory_show()
		drawer()
	elif dnext == "exit":
		exit(0)
	else:
		print 'What are you even saying.'
		drawer()
		
def fridge():
	
	fnext = raw_input('> ')
	
	if fnext == "mountain dew":
		print "'YES!! I have acquired the Dew."
		inventory.append('mountain dew')
		print "'What else is there to do in this kitchen.."
		kitchen()
	elif fnext == "inventory":
		inventory()
		fridge()
	elif fnext == "exit":
		exit(0)
	else:
		print "'M-muh Dew!"
		fridge()
	
def bathroom():

	btnext = raw_input('> ')
	
	if btnext == "toilet" and "piss bottles" in inventory:
		print "You empty all 5 bottles into the toilet. Good job! Now you have five empty bottles, "
		print "ready to be used."
		inventory.remove('piss bottles')
		inventory.append('empty bottles')
		print "You should probably leave the bathroom now. (Type it yourself, I'm not kicking you out)"
		bathroom()
	elif btnext == "toilet" and "piss bottles" not in inventory:
		print "Seeing as you pee in bottles and shit in the corner, there's no need to use that."
		bathroom()
	elif btnext == "sink":
		print "'My mother keeps a pretty clean sink.'"
		bathroom()
	elif btnext == 'razor':
		print "'My neckbeard is part of who I am. Shaving it off would make me less euphoric.'"
		bathroom()
	elif btnext == 'drawer' or btnext == "drawers":
		print "Nothing really interesting here, same old bathroom-y stuff."
		bathroom()
	elif btnext == 'kitchen':
		print "Time to leave this place."
		kitchen()
	elif btnext == 'inventory':
		inventory_show()
		bathroom()
	elif btnext == 'exit':
		exit(0)
	else:
		print "Did not catch that."
		bathroom()
		
def father():
	
	magic = raw_input("What's the magic word?\n> ")
	
	if magic == 'please':
		print "Dad: Sure son, you got it."
		print "You: I have no time for these infancies!"
		print "Dad: Sure, whatever you say. Hand me the xbox."
		print "Xbox removed!"
		inventory.remove('xbox')
		print "I should leave the living room now, I guess."
		living_room()
	elif magic == "inventory":
		inventory_show()
		father()
	elif magic == 'exit':
		exit(0)
	else:
		print "That's not the magic word!"
		father()
		
def endgame():
	print "Ripping open a Doritos bag and opening one of the Mountain Dew bottles, you try once again to add funds to your Microsoft account."
	print "'Funds added'"
	print "You smirk jewishly and stroke your neckbeard."
	print "Time to play the new Call of Duty DLC."
	print "Such is life for the basement dweller."
	print "The end."
	exit(0)
	
def inventory_show():	
	print inventory
	

basement()