import pygame,os

pygame.init()
pygame.mixer.init()


Display = pygame.display.set_mode((800,600))

pygame.display.update()

#----------------------------------Colours
white=(255,255,255)

yellow = (190,210,0)
l_yellow = (255,255,0)

l_red = (255,0,0)
red =(220,0,0)
orange = (255,160,0)
l_green  = (0,255,0)
green = (34,177,76)

grey =(50,50,50)
d_grey =(70,50,50)
black = (0,0,0)
gameExit = False
#------------------------------------------------
path1 = str(input('Enter the full path of your songs folder : '))
path = path1.replace('\\','\\\\')
path += '\\'
files = []
names = []
font = pygame.font.SysFont('Century Gothic',25)

for filename in os.listdir(path):
    if filename.endswith(".mp3"):
        pat = os.path.abspath(filename)
        files.append(filename)
        names.append(filename)

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
    Display.blit(textSurf , textRect)
#-----------------------------------------------Buttons

i = 0
val = None
mus = 1

def play(text,x,y,w,h,inactive_col,active_col):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global i,val
    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(Display,active_col,(x,y,w,h))
        
        if click[0]==1 :
           
            if i%2==0:
                
                if pygame.mixer.music.get_busy()==1:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.load(files[file_index])
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play()
                    
                i+=1
                val=True
                
            elif i%2!=0:
                pygame.mixer.music.pause()
                i+=1
                val=False
        
    else:
        pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))



def next_(text,x,y,w,h,inactive_col,active_col):
    global file_index
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(Display,active_col,(x,y,w,h))
        
        if click[0]==1:
            if files[file_index] == files[-1]:
                file_index=0
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v)
                pygame.mixer.music.stop()
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()
            else:
                file_index += 1
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v)
                pygame.mixer.music.stop()
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()
        
    else:
        pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))

def prev_(text,x,y,w,h,inactive_col,active_col):
    global file_index
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(Display,active_col,(x,y,w,h))
        
        if click[0]==1:
            if files[file_index] == files[0]:
                file_index = -1
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v)
                pygame.mixer.music.stop()
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()
            else:

                file_index -= 1
                v = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(v)
                pygame.mixer.music.stop()
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()
            
        
    else:
        pygame.draw.ellipse(Display,inactive_col,(x,y,w,h)) 




def vol_up(text,x,y,w,h,inactive_col,active_col):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global mus
    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.rect(Display,active_col,(x,y,w,h))
        
        if click[0]==1 :
            v = pygame.mixer.music.get_volume()
            pygame.mixer.music.set_volume(v+0.1)
        
    else:
        pygame.draw.rect(Display,inactive_col,(x,y,w,h))

def vol_down(text,x,y,w,h,inactive_col,active_col):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global mus
    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.rect(Display,active_col,(x,y,w,h))
        
        if click[0]==1 :
            v = pygame.mixer.music.get_volume()
            pygame.mixer.music.set_volume(v-0.1)
                  
    else:
        pygame.draw.rect(Display,inactive_col,(x,y,w,h))

    
#----------------------------------------------------Main Working
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        Display.fill(grey)
        
        
       
        pygame.draw.rect(Display,l_red,(0,400,800,200))
        pygame.draw.rect(Display,red,(0,400,400,200))
        
        
        
        
        play('Play',350,500,100,50,orange,l_green)
        prev_('Prev',100,500,100,50,yellow,l_yellow)
        next_('Next',600,500,100,50,yellow,l_yellow)
        vol_up('Volume +',650,200,130,50,l_yellow,yellow)
        vol_down('Volume -',650,300,130,50,l_yellow,yellow)
        
        
        pygame.draw.rect(Display,black,(0,400,800,50))
        name = str(names[file_index])
        text(name,white,350,400,100,50)
        
        if val == True:
            text('Pause',black,350,500,100,50)
        else:
            text('Play',black,350,500,100,50)
            
        text('Prev',black,100,500,100,50)
        text('Next',black,600,500,100,50)
        text('Volume +',black,670,200,100,50)
        text('Volume -',black,670,300,100,50)
        
        
        
        pygame.display.update()

            
pygame.quit()


