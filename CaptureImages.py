import cv2
import time
import random
import dropbox
start_time = time.time()
def takeSnapShot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        result=False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
takeSnapShot()

def uploadFile(img_name):
    access_token="LrMrhctMFYcAAAAAAAAAAR3v1yLs0iM2MUbBoH0qi-6O1dQyH1bfxLPLVstm2BLQ"
    file=img_name
    file_from=file
    file_to="/newFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
   

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if((time.time()-start_time)<=300):
            name=takeSnapShot()
            uploadFile(name)

main()         





