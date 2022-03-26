import os
from extensions import extension_paths
import shutil 
from folders import *

# file types

registry = open("bug_registry.txt","a")

registry.truncate()
registry.write("Bug and expeptions registry:\n")

all_files = list()
all_dirs = list()
# Iterate for each dict object in os.walk()
for root, dirs, files in os.walk(path):
    # Add the files list to the the all_files list
    all_dirs.append(dirs)
    all_files.extend(files)
  
for files in all_files:
    extension = os.path.splitext(files)
   
    try:
        category = extension_paths[extension[1]]

    except:
        category = None

    if category == 'text/text_files':
        print("moving...")
        
        try:
            shutil.move(path+files, text)
        
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    elif category == 'media/audio':
        print("moving...")
        try:
            shutil.move(path+files, audio)
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    elif category == "media/video":
        print("moving...")
        try:
            shutil.move(path+files, video)
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    elif category == "media/images":
        print("moving...")
        try:
            shutil.move(path+files, images)
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    elif category == "other/compressed":
        print("moving...")
        try:
            shutil.move(path+files, compressed)
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    elif category == "other/internet":
        print("moving...")
        try:
            shutil.move(path+files,internet)
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    elif category == 'programming/database':
        print("moving...")
        try:
            shutil.move(path+files, data)
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    elif category == 'other/executables':
        print("moving...")
        try:
            shutil.move(path+files, exe)
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    elif category == 'programming/':
        print("moving...")
        try:
            shutil.move(path+files, programming)
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    elif category == "/Users/facun/Downloads/":
        print("moving...")
        try:
            shutil.move(path+files, "/Users/facun/Downloads/text")
        except Exception as e:
            registry.write(e.__class__.__name__)
    
    else:
        print("moving...")
        try:
            shutil.move(path+files, "/Users/facun/Downloads/other")
        except Exception as e:
            registry.write(e.__class__.__name__)


registry.close()
