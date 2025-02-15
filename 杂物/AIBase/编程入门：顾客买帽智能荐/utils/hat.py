from utils.detect_face import *

def hat_recommend(img, hat_path):
    rec = get_faces(img)[0]
    if rec is not None:
        x, y = img.shape[0:2]
        crop = img[rec[1]:rec[3], rec[0]:rec[2]]

        # 不均匀图中图
        ax = plt.subplot(1, 2, 1)
        plt.axis('off')
        ax.set_title('Face')
        plt.imshow(crop)
        url = 'hats/' + hat_path
        hat = get_image(url)
        if hat is None:
            print('错误! 推荐帽子图片不存在!')
        else:
            x, y = crop.shape[0:2]
            x1, y1 = hat.shape[0:2]
            #等比例
            ratio = min(x1/x, y1/y)
            X = round(x * ratio)
            Y = round(y * ratio)
            hat = cv2.resize(hat, (Y, X))
            ax = plt.subplot(1, 2, 2)
            ax.set_title('Recommended hat')
            plt.axis('off')
            plt.imshow(hat)
            plt.show()
    else:
        print('错误! 图像中未检测到人脸!')
def hats_recommend(img, hats_list):
    rec = get_faces(img)[0]
    if rec is not None:
        x, y = img.shape[0:2]
        crop = img[rec[1]:rec[3], rec[0]:rec[2]]
        # fig = plt.figure()
        # 不均匀图中图
        number_hats = len(hats_list)
        rows = None
        cols = 3
        if number_hats % cols == 0:
            rows = int(number_hats/cols)
        else:
            rows = int(number_hats//cols +1)
        width = cols * 2 # 3*N宫格宽度
        height = (rows + 1) * 2 # 3*N宫格高度
        fig, axs = plt.subplots(int(rows+1), cols, figsize=(width, height))
        axs[0, 0].axis('off')
        axs[0, 0].set_title('Face')
        axs[0, 0].imshow(crop)
        for i in range(rows):
            for j in range(min(cols, number_hats-(i)*cols)):
                url = 'hats/' + str(hats_list[(i)*cols+j])
                hat = get_image(url)
                if hat is None:
                    print(f'错误! 推荐列表中名称为：{hats_list[(i)*cols+j]}的帽子图片不存在!')
                else:
                    x, y = crop.shape[0:2]
                    x1, y1 = hat.shape[0:2]
                    # 等比例
                    ratio = min(x1 / x, y1 / y)
                    X = round(x * ratio)
                    Y = round(y * ratio)
                    hat = cv2.resize(hat, (Y, X))
                    title = 'hat' + str(hats_list[(i) * cols + j])
                    axs[i + 1, j].set_title(title)
                    axs[i + 1, j].imshow(hat)

        for i in range(rows+1):
            for j in range(cols):
                axs[i, j].axis('off')
        plt.tight_layout()
        plt.show()
    else:
        print('错误! 图像中未检测到人脸!')
