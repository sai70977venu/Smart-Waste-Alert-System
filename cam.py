import cv2
import keras
from keras.models import load_model
import numpy as np 
from server  import send

model = load_model('model.h5')
print(model.summary())


def show_webcam(mirror=False):
    count = 0
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        img = cv2.resize(img, (64, 64)).astype(np.float32)
        img = np.expand_dims(img, axis=0)
        res = model.predict(img)
        res = res[0]
        count += 1
        classes = ["Garbage","Fire", "Others"]
        st = classes[res.argmax()]
        if st != "Others" and count % 180 == 0:
            send(st)
        if(cv2.waitKey(1)==27):
            break
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()