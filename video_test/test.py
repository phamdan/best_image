import cv2
import os


if __name__ == '__main__' :
    path_to_video="IMG_5335.MOV"
    name_file=path_to_video.split(".")[0]

    capture = cv2.VideoCapture(path_to_video)
    num = 0
    
    save_folder = os.path.join("frame", name_file)
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    i=0
    list_frame=[]
    while True:
        ret, frame = capture.read()
        # print(frame.shape)
        # exit()
        if frame is None:
            break
        num +=1

        if(num%10==0):
            i+=1
        save_folder_new= os.path.join(save_folder, f"{i}")
        if not os.path.exists(save_folder_new):
            os.mkdir(save_folder_new)
        cv2.imwrite(os.path.join(save_folder_new,f'{name_file}_{num}.jpg'),frame)

   
    

    
