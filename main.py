import pygame,time,os

pygame.init()
pygame.mixer.init()

Display = pygame.display.set_mode((800,600))
img = pygame.image.load("flash.png")



white=(255,255,255)

yellow = (200,200,0)
l_yellow = (255,255,0)

l_red = (255,0,0)
red =(230,0,0)

orange = (255,160,0)

l_green  = (0,255,0)
green = (34,177,76)

l_ok =(175,100,100)
ok = (150,100,100)

black = (0,0,0)

grey = (90,90,90)
gameExit = False
volume = 0.75

def filter_files(path, extension):
    return [file for root, dirs, files in os.walk(path) for file in files if file.endswith(extension)]

files = []
font = pygame.font.SysFont('Arial',25)

for filename in os.listdir("C:\\Users\\Family\\Music\\Songs\\"):
    if filename.endswith(".mp3"):
        files.append(filename)
nam = list(files)
print (nam)

path = "C:\\Users\\Family\\Music\\Songs\\"
for i in range(len(files)):
    files[i] = path + files[i]
file_index = 0
pygame.mixer.music.load(files[file_index])
#-----------------------------------------------Functions
def play_song():
    pygame.mixer.music.load(files[file_index])
    pygame.mixer.music.play()

def text_objects(text,color):
    textSurface = font.render(text,True,color)
    return textSurface , textSurface.get_rect()



def text(msg,color,x,y,w,h):
    textSurf,textRect = text_objects(msg,color)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    Display.blit(textSurf , textRect)

#-----------------------------------------------Buttons

def play(text,x,y,w,h,inactive_col,active_col):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(Display,active_col,(x,y,w,h))

        if click[0]==1 :
            if pygame.mixer.music.get_busy()==1:
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.load(files[file_index])
                pygame.mixer.music.play()


    else:
        pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))


def pause(text,x,y,w,h,inactive_col,active_col):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(Display,active_col,(x,y,w,h))

        if click[0]==1:
            pygame.mixer.music.pause()


    else:
        pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))


def next_button(text,x,y,w,h,inactive_col,active_col):
    global file_index
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(Display,active_col,(x,y,w,h))

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
        pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))

def prev_button(text,x,y,w,h,inactive_col,active_col):
    global file_index
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pos = pygame.mixer.music.get_pos()
    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(Display,active_col,(x,y,w,h))

        if click[0]==1:
            if pos>5000:
                play_song()
            else:
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
        pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))





def volume_up(text,x,y,w,h,inactive_col,active_col):
    global volume
    pygame.mouse.get_cursor()
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(Display,active_col,(x,y,w,h))
        if click[0]==1:
            if volume != 1.0:
                pygame.mixer.music.set_volume(volume + 0.075)
                volume += 0.075
            else:
                pass
    else:
        pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))

def volume_down(text,x,y,w,h,inactive_col,active_col):
    global volume
    pygame.mouse.get_cursor()
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > cur[0] > x and y+h > cur[1] > y:
        pygame.draw.ellipse(Display,active_col,(x,y,w,h))
        if click[0]==1:
            if volume != 0:
                pygame.mixer.music.set_volume(volume - 0.075)
                volume -= 0.075
            else:
                pass
    else:
        pygame.draw.ellipse(Display,inactive_col,(x,y,w,h))

#----------------------------------------------------Main
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        pygame.draw.rect(Display,grey,(0,400,800,200))
        Display.blit(img,(0,-20))

        play('Play',250,500,100,50,green,l_green)
        pause('Pause',400,500,100,50,red,l_red)
        prev_button('Prev',105,500,100,50,yellow,l_yellow)
        next_button('Next',550,500,100,50,yellow,l_yellow)
        volume_up('+',700,30,30,30,l_ok,ok)
        volume_down('-',700,400,30,30,l_ok,ok)

        pygame.draw.rect(Display,white,(703,75,25,310))
        pygame.draw.rect(Display,grey,(703,75,25,10))
        pygame.draw.rect(Display,grey,(703,375,25,10))


        text('Play',black,250,500,100,50)
        text('Pause',black,400,500,100,50)
        text('Prev',black,105,500,100,50)
        text('Next',black,550,500,100,50)
        text('+',black,700,30,30,30)
        text('-',black,700,400,30,30)



        name = str(nam[file_index])
        text(name,white,350,425,100,50)
        pygame.display.update()


pygame.quit()


