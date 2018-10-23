import os,pygame

def filter_files(path, extension):
    path = path
    
    name= [file for root, dirs, files in os.walk(path) for file in files if file.endswith(extension)]
    return (name,path)


tup = filter_files('C:\\Users\\Family\\','.mp3')
files = []
for i in tup[0]:
    files.append(tup[1]+i)
pygame.init()
pygame.mixer.init()    
pygame.mixer.music.load(files[0])
pygame.mixer.music.play(files[0])
