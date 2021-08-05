import cv2 , random
def Get_Frame(path):
    vidcap = cv2.VideoCapture(path)
    length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    vidcap.set(cv2.CAP_PROP_POS_FRAMES , (length//3))
    success,image = vidcap.read()
    fname= random.randint(1,1000000000000)
    cv2.imwrite(f"Rj{fname}.jpg", image)     # save frame as JPEG file  
    vidcap.set(cv2.CAP_PROP_POS_FRAMES , (length//1.5))
    success,image = vidcap.read()
    try: 
        fname2= random.randint(1,1000000000000)
        cv2.imwrite(f"Rj{fname2}.jpg", image)     # save frame as JPEG file 
        return [f"Rj{fname}.jpg",f"Rj{fname2}.jpg"]
    except:
        return [f"Rj{fname}.jpg"]
        