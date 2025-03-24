import random

#roll
def roll(dice):
	hand=[]
	i=0
	while(dice>i):
		hand.append(random.randint(1,6));
		i=i+1
	return(hand)


#point counter
def point(hand,dicein,scoreinit):
	farkle=1
	score=scoreinit
	dice=dicein
	one=hand.count(1)
	two=hand.count(2)
	three=hand.count(3)
	four=hand.count(4)
	five=hand.count(5)
	six=hand.count(6)
	counts=[one,two,three,four,five,six]
	if (counts.count(3)==2):
		score=score+2500
		print("2 triples!")
		dice=dice-6
		farkle=0
		#3 pairs
	elif (counts.count(2)==3):
		score=score+1500
		print("3 pairs!")
		dice=dice-6
		farkle=0
		#"full house +1"
	elif(counts.count(4)==1 and counts.count(2)==1):
		score=score+1500
		print("full house!")
		dice=dice-6
		farkle=0
		#6 of a kind
	elif(counts.count(6)==1):
		score=score+3000
		dice=dice-6
		print("six of a kind!!!")		
		farkle=0
		#straight
	elif(counts.count(1)==6):
		score=score+1500
		dice=dice-6
		print("straight!")
		farkle=0
		#5 of a kind
	elif(counts.count(5)==1):
		score=score+2000
		print("5 of a kind!!")
		dice=dice-5
		farkle=0
		#4 of a kind
	elif(counts.count(4)==1):
		score=score+1000
		print("4 of a kind!")
		dice=dice-4
		farkle=0
		#3 of a kind
	elif(counts.count(3)==1):
		print("3 of a kind!")
		if (hand.count(1)==3):
			score = score + 300
		elif (hand.count(2)==3):
			score=score+200
		elif(hand.count(3)==3):
			score=score+300
		elif(hand.count(4)==3):
			score=score+400
		elif(hand.count(5)==3):
			score=score+500
		elif(hand.count(6)==3):
			score=score+600
		dice=dice-3
		farkle=0
		#finish up
		
		#1
	if(hand.count(1)>0 and hand.count(1)<3 and dice!=0):
		farkle=0
		score=score+100*hand.count(1)
		dice = dice - hand.count(1)	
				#5
	if(hand.count(5)>0 and hand.count(5)<3 and dice!=0):
		farkle=0
		score=score+50*hand.count(5)
		dice = dice - hand.count(5)
		#farkle
	if(farkle==1):
		print("farkle :p    score:0")
		return([0,1,1])
		
	return([score,dice,farkle])
		

#initialize turn
total=0
score=0
while(total<10000):
	print("")
	print("starting over")
	total=total + score
	print ("current total score:", end="")
	print(total)
	dice=6
	farkle=0
	choice="y"
	score=0
	while(farkle==0 and choice=="y"):
		hand=roll(dice)
		print(hand)
		result=point(hand,dice,score)
		if(result[2]==1):
			score=0
			break
		if(result[1]==0):
			dice=6
			print("new hand!")
		else:
			dice=result[1]
		score=result[0]
		print(dice,end="")
		print(" dice left. Current score:",end="")
		print(score)
#choice
		choice=input("Go again? (y/n)")

print(" you won")

	