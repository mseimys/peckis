import cv2


def preprocess(filename):
    img = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    mask = img[:,:,3]
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = cv2.boundingRect(contours[0])
    img = img[y:y+h, x:x+w,3] # crop and take only the alpha layer
    img = cv2.resize(img, (28, 28))
    return img.reshape((1, 784)).astype("float32") / 255
