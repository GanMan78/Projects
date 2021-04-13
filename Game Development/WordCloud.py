
import pygame
import sys
import random
import time
import Words

pygame.init()

def NewWord():
	global word_x, word_y,text,choosen_word,press_word,word_caption
	word_x=random.randint(150,600)
	word_y=0
	press_word=''
	choosen_word=random.choice(Words.list)
	text=font.render(choosen_word,True,black)
	
#variables
x=900
y=600
speed=0.5
score=0
lcnt=0
print("1st lcnt")

#colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

#words
font=pygame.font.SysFont("ComicSansMs",45)
wfont=pygame.font.SysFont("Cambria",45)
text1=font.render("Hit SPACE To Try Again..",True,red)
text2=wfont.render("Press 'y' to continue..",True,blue)
text3=wfont.render("Continue limit exceeded..starting again",True,black)
award=wfont.render("You crossed the level..",True,blue)
#screen
win=pygame.display.set_mode((x,y))
pygame.display.set_caption("Burst the word cloud")

#Logo
logo=pygame.image.load("ic.png")
bg1=pygame.image.load("bg1.png")
bg2=pygame.image.load("bg2.png")
bg3=pygame.image.load("bg3.png")
bg4=pygame.image.load("bg4.jpg")
bg5=pygame.image.load("bg5.jpg")
cloud=pygame.image.load("clipart.png")
blast=pygame.image.load("blast.gif")
pygame.display.set_icon(logo)

#Sounds & Music
pygame.mixer.music.load("PUBG.mp3")
effect1=pygame.mixer.Channel(0)
effect1.set_volume(0.2)
effect2=pygame.mixer.Channel(1)
effect1.set_volume(0.2)
blast_sound=pygame.mixer.Sound("boom.wav")
lost_sound=pygame.mixer.Sound("loss1.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

NewWord()
#To continuosly run the game loop
while True:
	if (score>=50 and score<100):
		if score<55:
			print("Speed after 50 :",speed)
			pygame.display.update()
			win.blit(award,(200,300))
			pygame.display.update()
			time.sleep(1)
			score=55
		win.blit(bg2,(0,0))
		font=pygame.font.SysFont("ComicSansMs",35)
		win.blit(cloud,(word_x-35,word_y-30))
	elif (score>=150 and score<250):
		if score<155:
			print("Speed after 150 :",speed)
			pygame.display.update()
			win.blit(award,(200,300))
			pygame.display.update()
			time.sleep(1)
			score=155
			speed=2.0
		win.blit(bg3,(0,0))

		font=pygame.font.SysFont("ComicSansMs",25)
		win.blit(cloud,(word_x-40,word_y-40))
	elif (score>=250 and score<350):
		if score<255:
			print("Speed after 250 :",speed)
			pygame.display.update()
			win.blit(award,(200,300))
			pygame.display.update()
			time.sleep(1)
			score=255
			speed=1.7
		win.blit(bg4,(0,0))
		win.blit(cloud,(word_x-35,word_y-30))

	elif (score>=350):
		if score<355:
			print("Speed after 350 :",speed)
			score=355
			speed=2.2
		win.blit(bg5,(0,0))
		win.blit(cloud,(word_x-35,word_y-30))

	else:
		win.blit(bg1,(0,0))
		win.blit(cloud,(word_x-25,word_y-20))
	win.blit(text,(word_x,word_y))
	word_y+=speed
	word_caption=wfont.render(choosen_word,True,red)
	win.blit(word_caption,(15,50))
    
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif (event.type==pygame.KEYDOWN):
			press_word+=pygame.key.name(event.key)
			if choosen_word.startswith(press_word):
				text=font.render(press_word,True,blue)
				if choosen_word==press_word:
					score+=len(choosen_word)
					effect1.play(blast_sound,maxtime=600)
					win.blit(blast,(word_x,word_y))
					pygame.display.update()
					time.sleep(0.02)
					pygame.display.update()
					speed+=0.05
					print(speed)
					print(word_y)
					NewWord()
			else:
				text = font.render(press_word,True,red)
				press_word = ''
	score_caption=wfont.render(str(score),True,blue)
	win.blit(score_caption,(15,5))
	if(word_y<y-5):
		pass
	else:
		count=pygame.mixer.Channel(1).get_busy()
		if count==1:
			pass
		else:
			effect2.play(lost_sound,maxtime=3000)
		win.blit(text1,(150,260))
		win.blit(text2,(150,360))
		pygame.display.update()
		event=pygame.event.wait()
		if(event.type==pygame.QUIT):
			pygame.quit()
			sys.exit()
		if(event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
			score=0
			speed=1
			font=pygame.font.SysFont("ComicSansMs",45)
			NewWord()
			pygame.mixer.music.play()            
		if(event.type==pygame.KEYDOWN and event.key==pygame.K_y):        

                    print("loss lcnt",lcnt)
                    if lcnt==3:
                        print("inside new if")
                        win.blit(text3,(50,150))
                        pygame.display.update()
                        time.sleep(5)
                        score=0
                        speed=1
                        font=pygame.font.SysFont("ComicSansMs",45)
                        NewWord()
                        lcnt=0
                        pygame.mixer.music.play()
                    else:
                        print("inside new else")
                        lcnt=lcnt+1
                        print("else lcnt",lcnt)
                        NewWord()
	pygame.display.update()