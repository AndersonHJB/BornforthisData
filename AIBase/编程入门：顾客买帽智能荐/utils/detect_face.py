# 引入库
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import tempfile
import requests

'''读取图像的相关函数'''
def _tmppath_from_url(url):
    tmpfile = tempfile.mktemp()
    r = requests.get(url)
    if r.status_code != 200:
        raise IOError("download failed.")
    with open(tmpfile, 'wb') as f:
        f.write(r.content)  #对应的内容，也就是图片
    return tmpfile

def get_image(path):
    '''Read image from path or url.'''
    if path.startswith('http'):
        path = _tmppath_from_url(path)
    if os.path.exists(path):
        img = cv2.imread(path, cv2.IMREAD_COLOR)[:, :, ::-1]
    else:
        print("No such file")
        return None
    return img

'''显示图像的函数'''
def display_img(img):
    """在屏幕上显示图像并保持输出直到用户按下一个键"""
    # 显示图像
    plt.imshow(img)
    plt.show()

'''下面是一个动态调整图像大小的函数，当图像超过一定宽度时调整输入图像的大小'''
# from: https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # 初始化要调整大小的图像的尺寸并获取图像尺寸
    dim = None
    (h, w) = image.shape[:2]
    # 如果宽度和高度都为 None，则返回原始图像
    if width is None and height is None:
        return image
    # 检查宽度是否为 None
    if width is None:
        # 计算高度的比例并构建尺寸
        r = height / float(h)
        dim = (int(w * r), height)
    # 否则，高度为 None
    else:
        # 计算宽度的比例并构建尺寸
        r = width / float(w)
        dim = (width, int(h * r))
    # 调整图像大小
    return cv2.resize(image, dim, interpolation = inter)

'''下面是人脸检测，性别、年龄预测的函数'''

# 定义人脸、年龄和性别检测模型的权重和架构变量
FACE_PROTO = "weights/deploy.prototxt" # 来源: https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt
FACE_MODEL = "weights/res10_300x300_ssd_iter_140000_fp16.caffemodel" # 来源: https://raw.githubusercontent.com/opencv/opencv_3rdparty/dnn_samples_face_detector_20180205_fp16/res10_300x300_ssd_iter_140000_fp16.caffemodel

# 性别模型的架构
GENDER_MODEL = 'weights/deploy_gender.prototxt' # 来源: https://drive.google.com/open?id=1W_moLzMlGiELyPxWiYQJ9KFaXroQ_NFQ
# 性别模型预训练权重
GENDER_PROTO = 'weights/gender_net.caffemodel' # 来源: https://drive.google.com/open?id=1AW3WduLk1haTVAxHOkVS_BEzel1WXQHP

# 每个Caffe模型都会规定输入图像的形状，同时需要进行图像预处理，如均值减法来消除光照变化的影响
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
# 性别类别
GENDER_LIST = ['Male', 'Female']

# 年龄模型的架构
AGE_MODEL = 'weights/deploy_age.prototxt' # download from: https://drive.google.com/open?id=1kiusFljZc9QfcIYdU2s7xrtWHTraHwmW
# 年龄模型预训练权重
AGE_PROTO = 'weights/age_net.caffemodel' # download from: https://drive.google.com/open?id=1kWv0AjxGSN0g31OeJa02eBGM0R_jcjIl

# CNN网络输出层的8个年龄类别
AGE_INTERVALS = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)',
                 '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']

# 加载模型
face_net = cv2.dnn.readNetFromCaffe(FACE_PROTO, FACE_MODEL) # 加载人脸 Caffe 模型
age_net = cv2.dnn.readNetFromCaffe(AGE_MODEL, AGE_PROTO) # 加载年龄预测模型
gender_net = cv2.dnn.readNetFromCaffe(GENDER_MODEL, GENDER_PROTO) # 加载性别预测模型

# 检测图像中是否存在人脸的函数，如果存在会返回人脸位置
def get_faces(frame, confidence_threshold=0.5):
    # 将图像帧转换为 blob 以便为 NN 输入做好准备
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104, 177.0, 123.0))
    # 将图像设置为 NN 的输入
    face_net.setInput(blob)
    # 执行推理并获得预测
    output = np.squeeze(face_net.forward())
    # 初始化结果列表
    faces = []
    # 循环检测面孔
    for i in range(output.shape[0]):
        confidence = output[i, 2]
        if confidence > confidence_threshold:
            box = output[i, 3:7] * \
                np.array([frame.shape[1], frame.shape[0],
                         frame.shape[1], frame.shape[0]])
            # 转换为整数
            start_x, start_y, end_x, end_y = box.astype(np.int32)
            # 把检测框加宽一点
            start_x, start_y, end_x, end_y = start_x - \
                10, start_y - 10, end_x + 10, end_y + 10
            start_x = 0 if start_x < 0 else start_x
            start_y = 0 if start_y < 0 else start_y
            end_x = 0 if end_x < 0 else end_x
            end_y = 0 if end_y < 0 else end_y
            # 添加到列表
            faces.append((start_x, start_y, end_x, end_y))
    return faces


# 检测图像中人脸的性别
def get_gender_predictions(face_img):
    blob = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=MODEL_MEAN_VALUES, swapRB=False, crop=False
    )
    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    i = gender_preds[0].argmax()
    gender = GENDER_LIST[i]
    gender_confidence_score = gender_preds[0][i]
    return gender

# 检测图像中人脸的年龄
def get_age_predictions(face_img):
    blob = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=MODEL_MEAN_VALUES, swapRB=False
    )
    age_net.setInput(blob)
    age_preds = age_net.forward()
    i = age_preds[0].argmax()
    age = eval(AGE_INTERVALS[i])  # 年龄段信息
    age_confidence_score = age_preds[0][i] # 年龄段置信度
    return age


# 综合性函数：同时检测图像中人脸的年龄、性别，并将相关信息及人脸检测框绘制到图像上
def predict_age_and_gender(img):
    """Predict the gender of the faces showing in the image"""
    # 初始化帧大小
    frame_width = 640
    frame_height = 360
    # 复制原始图像并resize
    frame = img.copy()
    if frame.shape[1] > frame_width:
        frame = image_resize(frame, width = frame_width)
    # 预测图像中的人脸
    faces = get_faces(frame)
    if len(faces) != 0 :
        # 循环处理每一个检测出的人脸
        for i, (start_x, start_y, end_x, end_y) in enumerate(faces):
            face_img = frame[start_y: end_y, start_x: end_x]
            
            gender = get_gender_predictions(face_img) # 性别预测
            
            age = get_age_predictions(face_img) # 年龄预测
            
            # 绘制检测框
            yPos = start_y - 15
            while yPos < 15:
                yPos += 15
            box_color = (0, 0, 255) if gender == "Male" else (255, 0, 0) # 注：颜色顺序BGR
            cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), box_color, 2)
            
            # 设置标签信息
            gender_label = f"Gender-{gender}"
            age_label = f"Age-{age}"

            # 在图像上添加标签信息
            font_scale = 0.54
            cv2.putText(frame, gender_label, (start_x, yPos-5),
                        cv2.FONT_HERSHEY_SIMPLEX, font_scale, box_color, 2)
            cv2.putText(frame, age_label, (start_x, yPos+10),
                        cv2.FONT_HERSHEY_SIMPLEX, font_scale, box_color, 2)
    else:
        print("图中没有人脸")
        gender, age = None, None
    # 显示处理的照片
    display_img(frame)
    
    return gender, age