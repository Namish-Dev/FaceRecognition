import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)

import sqlite3

def insertorupdate(ID, Name, Age):
    conn = sqlite3.connect("Database.db")
    
    # Corrected table name to STUDENTS
    cmd = "SELECT * FROM STUDENTS WHERE ID=" + str(ID)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
        
    if isRecordExist == 1:
        # Corrected table name to STUDENTS
        conn.execute("UPDATE STUDENTS SET Name=? WHERE ID=?", (Name, ID))
        conn.execute("UPDATE STUDENTS SET Age=? WHERE ID=?", (Age, ID))
    else:
        # Corrected table name to STUDENTS
        conn.execute("INSERT INTO STUDENTS(ID, Name, Age) VALUES(?, ?, ?)", (ID, Name, Age))
    
    conn.commit()
    conn.close()


ID=input("Enter User ID:")
Name=input("Enter User Name:")
Age=int(input("Enter User Age:"))

insertorupdate(ID,Name,Age)


sampleNum=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite("Dataset/user."+str(ID)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    
    if(sampleNum>5):
        break
cam.release()
cv2.destroyAllWindows()
