from utils_cv.image_processing import crop, resize_image
import cv2
import sys
sys.path.append("./")


def crop_objects(img):
    '''
    Detect objects then crop objects and return list of image of size 224, 224

            Parameters :
                    img (image): (w, h, 3)

            Return:
                    List(img): size (224, 224, 3)
    '''

    WIDTH = 224
    HEIGHT = 224

    Conf_threshold = 0.4
    NMS_threshold = 0.4

    net = cv2.dnn.readNet('config/yolov4-tiny.weights',
                          'config/yolov4-tiny.cfg')
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

    _, _, boxes = model.detect(img, Conf_threshold, NMS_threshold)

    img_list = []
    for box in boxes:

        # increase box size to not crop some parts of objects
        box[0], box[1] = box[0] * 0.98, box[1] * 0.98
        box[2], box[3] = box[2] * 1.02, box[3] * 1.02

        cropped_img = crop(img, box)
        cropped_img = resize_image(cropped_img, (WIDTH, HEIGHT))
        img_list.append(cropped_img)

    return img_list


def crop_objects_coord(img):
    '''
    Detect objects then crop objects and return list of image of size 224, 224 and the coordinate of the croped object.

            Parameters :
                    img (image): (w, h, 3)

            Return:
                    List(img): size (224, 224, 3)
    '''

    WIDTH = 224
    HEIGHT = 224

    Conf_threshold = 0.4
    NMS_threshold = 0.4

    net = cv2.dnn.readNet('config/yolov4-tiny.weights',
                          'config/yolov4-tiny.cfg')
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)

    _, _, boxes = model.detect(img, Conf_threshold, NMS_threshold)

    img_list = []
    for box in boxes:

        # increase box size to not crop some parts of objects
        box[0], box[1] = box[0] * 0.98, box[1] * 0.98
        box[2], box[3] = box[2] * 1.02, box[3] * 1.02

        cropped_img = crop(img, box)
        cropped_img = resize_image(cropped_img, (WIDTH, HEIGHT))
        img_list.append(cropped_img)

    return img_list, boxes
