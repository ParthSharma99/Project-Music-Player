import pygame,time,os

pygame.init()
pygame.mixer.init()


gameDisplay = pygame.display.set_mode((800,600))

pygame.display.update()


white=(255,255,255)

yellow = (200,200,0)
l_yellow = (255,255,0)

l_red = (255,0,0)
red =(230,0,0)
orange = (255,160,0)
l_green  = (0,255,0)
green = (34,177,76)

grey =(50,50,50)
black = (0,0,0)
gameExit = False

img = pygame.image.load('bvs_standoff_wpw.jpg')

files = []
font = pygame.font.SysFont(None,35)
for filename in os.listdir("C:\\Users\\Family\\Desktop\\new"):
    if filename.endswith(".mp3"):
        files.append(filename)
nam = list(files)

path = "C:\\Users\\Family\\Desktop\\new\\"
for i in range(len(files)):
    files[i] = path + files[i]   
    

    
file_index = 0
pygame.mixer.music.load(files[file_index])
#-----------------------------------------------Functions

def text_objects(text,color):
    textSurface = font.render(text,True,color)
    return textSurface , textSurface.get_rect()
    


def text(msg,color,x,y,w,h):
    textSurf,textRect = text_objects(msg,color)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf , textRect)
    
#-----------------------------------------------Buttons

def play(text,x,y,w,h,inactive_col,active_col):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global n
    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(gameDisplay,active_col,(x,y,w,h))
        
        if click[0]==1 :
            if pygame.mixer.music.get_busy()==1:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()
                  
        
    else:
        pygame.draw.ellipse(gameDisplay,inactive_col,(x,y,w,h))

        
def pause(text,x,y,w,h,inactive_col,active_col):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(gameDisplay,active_col,(x,y,w,h))
        
        if click[0]==1:
            pygame.mixer.music.pause()
                
        
    else:
        pygame.draw.ellipse(gameDisplay,inactive_col,(x,y,w,h)) 


def next_(text,x,y,w,h,inactive_col,active_col):
    global file_index
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(gameDisplay,active_col,(x,y,w,h))
        
        if click[0]==1:
            if files[file_index] == files[-1]:
                file_index=0
                pygame.mixer.music.stop()
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()
            else:
                file_index += 1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()
            
        
    else:
        pygame.draw.ellipse(gameDisplay,inactive_col,(x,y,w,h))

def prev_(text,x,y,w,h,inactive_col,active_col):
    global file_index
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(gameDisplay,active_col,(x,y,w,h))
        
        if click[0]==1:
            if files[file_index] == files[0]:
                file_index = -1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()
            else:

                file_index -= 1
                pygame.mixer.music.stop()
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()
            
        
    else:
        pygame.draw.ellipse(gameDisplay,inactive_col,(x,y,w,h)) 

#----------------------------------------------------Main
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,orange,(0,400,800,200))
        

        play('Play',250,500,100,50,green,l_green)
        pause('Pause',450,500,100,50,red,l_red)
        prev_('Prev',100,500,100,50,yellow,l_yellow)
        next_('Next',600,500,100,50,yellow,l_yellow)

        pygame.draw.rect(gameDisplay,black,(80,400,600,50))
        name = str(nam[file_index])
        text(name,white,350,400,100,50)
        
        text('Play',black,250,500,100,50)
        text('Pause',black,450,500,100,50)
        text('Prev',black,100,500,100,50)
        text('Next',black,600,500,100,50)
        
        
        pygame.gameDisplay.blit(img,(0,-20))
        pygame.display.update()

            
pygame.quit()


