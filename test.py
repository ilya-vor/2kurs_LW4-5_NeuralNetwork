import paint
from NN import get_model
import numpy as np
import cv2


def rec_digit(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    gray = 255 - img
    # применяем пороговую обработку
    (thresh, gray) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    #gray = cv2.resize(gray, (28, 28))
    cv2.imwrite('gray' + img_path, gray)
    img = gray / 255.0
    img = np.array(img).reshape(-1, 28, 28, 1)
    out = str(np.argmax(model.predict(img)))
    return out


model = get_model()
#paint.main()
print(rec_digit('2.png'))
