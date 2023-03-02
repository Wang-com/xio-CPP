import numpy as np
import cv2


def line_params(p1, p2):
    """
    p:(x, y), y = w * x + b
    :param p1: point 1
    :param p2: point 2
    :return: w, b
    """
    x1, y1 = p1
    x2, y2 = p2

    w = (y2 - y1) / (x2 - x1)
    b = (y1 * x2 - x1 * y2) / (x2 - x1)

    return w, b


def y_(x, w, b):
    y = w * x + b
    return y


def x_(y, w, b):
    x = (y - b) / w
    return x


def create_mask(orig_img, lines):
    img = cv2.imread(orig_img)
    mask = np.zeros_like(img)
    height, width, channel = mask.shape
    print(height, width)

    left, top, right, bottom = lines
    for x in range(width):
        for y in range(height):
            if x_(y, left[0], left[1]) <= x <= x_(y, right[0], right[1]) and \
                    y_(x, top[0], top[1]) <= y <= y_(x, bottom[0], bottom[1]):
                mask[y, x, 2] = 255
    return mask


def add_mask(orig_mask, lines):
    mask = cv2.imread(orig_mask)
    height, width, channel = mask.shape
    print(height, width)

    left, top, right, bottom = lines
    for x in range(width):
        for y in range(height):
            if x_(y, left[0], left[1]) <= x <= 500 and \
                    y_(x, top[0], top[1]) <= y <= y_(x, bottom[0], bottom[1]):
                mask[y, x, 2] = 255
    return mask


def main():
    # orig_img = '../images/records/vlcsnap-2019-08-02-16h01m50s221.png'
    # left = line_params((180, 210), (35, 370))
    # top = line_params((180, 210), (500, 330))
    # right = line_params((500, 330), (495, 479))
    # bottom = line_params((0, 479), (495, 479))

    # sawanini_1
    orig_img = cv2.imread('D:\\XIO_Safe_1_alarm_X_2\\images\\masks\\'
                          'mask_1_1.jpg')
    mask = np.zeros_like(orig_img)

    # points = np.array([[176, 138], [154, 421], [638, 327], [554, 150], [358, 170], [348, 126]],
    #                   dtype=np.int32)
    # points = np.array([[423, 263], [420, 239], [252, 227], [217, 285], [437, 305], [438, 279],
    #                    [471, 280], [467, 268], [437, 265]], dtype=np.int32)
    # points = np.array([[245, 216], [259, 284], [407, 256], [351, 199]],
    #                   dtype=np.int32)
    # points = np.array([[379, 44], [420, 70], [420, 198], [497, 241], [460, 434],
    #                    [460, 479], [80, 479], [117, 296], [201, 97], [228, 46]],
    #                   dtype=np.int32)
    # points = np.array([[250, 226], [173, 355], [433, 397], [438, 306], [487, 308],
    #                    [482, 269], [424, 263], [421, 238]],
    #                   dtype=np.int32)
    # points = np.array([[76, 0], [506, 0],[514,76], [550, 122], [82, 192], [85, 185]],
    #                dtype=np.int32) # 2_2
    #points = np.array([[228, 124], [220, 149], [247, 150], [246, 171], [430, 189], [433, 180], [539, 194], [531, 158]],
    #                  dtype=np.int32)  # 2_rush
    points = np.array([[29, 308], [54, 328], [132, 324], [159, 349], [506, 263], [420, 222], [351, 241], [350, 183],
     [129, 228], [126, 295]],
                        dtype=np.int32) # 2_1
    # points = np.array([[320,8], [365,55], [400,31], [508,166], [496,170], [600, 291], [283,449],[229,426], [85, 75]],
    #                  dtype=np.int32) # 1_rush
    # points = np.array([[173, 150], [89, 286], [585, 280], [584, 155]],
    #                   dtype=np.int32) # 2_weld
    # points = np.array([[221, 136], [237, 170], [555, 212], [547, 189]])
    # points = np.array([[254, 303],[235, 220], [261, 198], [357, 182], [444, 262]],
    #                    dtype=np.int32) # 1_1
    mask = cv2.fillPoly(mask, [points], (0, 80, 255))
    # baobantongyong
    # orig_img = '../images/records/vlcsnap-2019-09-03-09h50m51s942.png'
    # left = line_params((115, 77), (23, 479))
    # top = line_params((115, 77), (397, 93))
    # right = line_params((397, 93), (405, 479))
    # bottom = line_params((23, 479), (405, 479))
    # mask = create_mask(orig_img, [left, top, right, bottom])

    # orig_mask = '../images/masks/penfenshang.jpg'
    # left = line_params((180, 150), (68, 479))
    # top = line_params((180, 150), (445, 210))
    # right = line_params((445, 210), (495, 479))
    # bottom = line_params((65, 479), (490, 479))
    # mask = add_mask(orig_mask, [left, top, right, bottom])

    # orig_img = '../images/records/vlcsnap-2019-08-02-16h02m31s252.png'
    # left = line_params((100, 175), (45, 385))
    # top = line_params((100, 175), (170, 180))
    # right = None
    # bottom = line_params((45, 385), (490, 385))
    # # mask = create_mask(orig_img, [left, top, right, bottom])
    # orig_mask = '../images/masks/sawanini_2.jpg'
    # left = line_params((220, 100), (169, 188))
    # top = line_params((220, 115), (480, 115))
    # right = None
    # bottom = line_params((100, 175), (170, 183))
    # mask = add_mask(orig_mask, [left, top, right, bottom])

    cv2.imshow('mask', mask)

    cv2.imwrite('../images/masks/mask_2_1.jpg', mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':

    # img_path = '../images/records/vlcsnap-2019-08-02-16h02m06s098.png'
    # mask_path = '../images/masks/sawanini_2.jpg'
    #
    # img = cv2.imread(img_path)
    # mask = cv2.imread(mask_path)
    #
    # overlap = cv2.addWeighted(img, 1, mask, 0.6, 0)
    #
    # cv2.imshow('overlap', overlap)
    # cv2.waitKey(0)
    main()

