import cv2,os,random
cap = cv2.VideoCapture('TheChase.mkv')
success,image = cap.read()
#save frames to folder 
count = 0
success = True
while success:
  success,image = cap.read()
  print 'Read a new frame: ', success
  cv2.imwrite("Frames\\frame%d.jpg" % count, image)    
  count += 1
path = r"F:\Python Projects\Shuffle Frames\Frames"
frames_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
x=0
y=int(fps)
count=count_in=0 
random_filename=path+"\\frame0.jpg"
img = cv2.imread(random_filename)
height , width , layers =  img.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
while frames_count > count:
    while count_in<fps:
        num=random.randint(x,y)
        random_filename=path+"\\frame"+str(num)+".jpg"
        print (random_filename)
        img = cv2.imread(random_filename)
        out.write(img) # Write out frame to video
        #os.remove(random_filename) #if you want to delete file
        count_in+=1
    x=y+1
    y+=int(fps)
    count_in=0
    print(x,y)
    count+=int(fps)
cv2.destroyAllWindows()

