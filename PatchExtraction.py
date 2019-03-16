import cv2

class PatchExtraction:
    def __init__(self, imageName, minutiaeSets,size):
        super(PatchExtraction, self).__init__()
        self.size = size
        self.imageName = imageName
        self.minutiaeSets = minutiaeSets

    def extract():
        image = cv2.imread(self.imageName, cv2.IMREAD_GRAYSCALE)
        n=0
        for x,y,theta in self.minutiaeSets:
            raw_patch = mat(image,x,y,size*2*1.42)
            rotateMat = cv2.getRotationMatrix2D((width/2, height/2), angle, scale=1.0)
            rotateImage = cv2.warpAffine(raw_patch,rotateMat,)
            raw_patch = mat(image,height/2,wifth/2,size*2)
            cv2.imwrite("{}{}.bmp".format(self.imageName,n))
            n+=1
