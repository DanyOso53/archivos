import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

donde= "C:/Users/dmald/Downloads"
haciadonde="C:/Users/dmald/OneDrive/Escritorio/Filtro"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt',".docx"],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class movimientoarchivo(FileSystemEventHandler) : 
      
      def on_created(self, event):
                    name, extension = os.path.splitext(event.src_path)
                    time.sleep(1)
                    for key, value in dir_tree.items(): 
                          time.sleep(1)
                          if extension in value:
                                nombrearchivo = os.path.basename(event.src_path)
                                ruta1= donde + "/"+ nombrearchivo
                                ruta2= haciadonde + "/"+ key
                                ruta3= haciadonde + "/"+ key + "/" + nombrearchivo
                                time.sleep(3)
                    
                
                                if os.path.exists(ruta2):
                                            print("moviendo "+ nombrearchivo + " ...")
                                            shutil.move(ruta1, ruta3)
                                else: 
                                            os.makedirs(ruta2)
                                            print("moviendo "+ nombrearchivo + " ...")
                                            shutil.move(ruta1, ruta3)

                    
        
   
       
        

docs= movimientoarchivo()
monitorear= Observer()
monitorear.schedule(docs,donde,recursive=True )
monitorear.start()

while True :
      time.sleep(2)
      print("ejecutando...")
















