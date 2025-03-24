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

		dice=dice-6
		farkle=0
		#3 pairs
	elif (counts.count(2)==3):
		score=score+1500
	
		dice=dice-6
		farkle=0
		#"full house +1"
	elif(counts.count(4)==1 and counts.count(2)==1):
		score=score+1500

		dice=dice-6
		farkle=0
		#6 of a kind
	elif(counts.count(6)==1):
		score=score+3000
		dice=dice-6
		
		farkle=0
		#straight
	elif(counts.count(1)==6):
		score=score+1500
		dice=dice-6
		
		farkle=0
		#5 of a kind
	elif(counts.count(5)==1):
		score=score+2000

		dice=dice-5
		farkle=0
		#4 of a kind
	elif(counts.count(4)==1):
		score=score+1000
		dice=dice-4
		farkle=0
		#3 of a kind
	elif(counts.count(3)==1):

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
		return([0,1,1])
		
	return([score,dice,farkle])
		

#initialize auto
goal=50
current=0
goals=[]
scores=[]
while(goal<2000):
	total=0
	score=0
	turns=0
	while(turns<2000):
		total=total + score
		dice=6
		farkle=0
		choice="y"
		score=0
		turns=turns+1
		while(farkle==0 and choice=="y"):
			hand=roll(dice)
			result=point(hand,dice,score)
			if(result[2]==1):
				score=0
				break
			if(result[1]==0):
				dice=6
			else:
				dice=result[1]
			score=result[0]
			if (score<goal):
				choice="y"
			else:
				choice="n"
	total=total+score
	goals.append(goal)
	scores.append(total)
	if (total>current):
		winner=goal
		current=total
	goal=goal+50
print(winner, end="")
print(" won with a 2000 turn score of ", end="")
print (current)
i=0
while (50*i<goal-50):
	print(goals[i], end=",")
	print(scores[i])
	i=i+1
	