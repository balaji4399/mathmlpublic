# from pix2text import Pix2Text, merge_line_texts
# from PIL import Image as im,ImageDraw , ImageEnhance , ImageFilter
# import cv2
# import re
# import torch
# # from super_resolution import cartoon_upsampling_4x
# import numpy as np
# import warnings
# warnings.filterwarnings('ignore')
# # import cv2.dnn_superres as dnn_superres

# # sr = dnn_superres.DnnSuperResImpl_create()
                                         
# sr = cv2.dnn_superres.DnnSuperResImpl_create()

# path = "FSRCNN_x4.pb"

# sr.readModel(path)

# sr.setModel("fsrcnn",4)

                                                                                                                                     
# # from RealESRGAN import RealESRGAN

# img_fp = 'io/SS1.JPG'
# img_form=img_fp.split('.')[1]
# # if img_form=='.jpg' or img_form=='.JPG' :
# img = cv2.imread(img_fp)
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # cv2.imwrite('mb.jpg',img)
# # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# # model = RealESRGAN(device,scale=4)
# # model.load_weights('weights/RealESRGAN_x4.pth', download=True)
# # img_fp='/content/M.png'
# # image = im.open(img_fp).convert('RGB')
# # enhancer = ImageEnhance.Contrast(image)
# # image = enhancer.enhance(1)
# # image.save(img_fp)
# # img = cv2.imread(img_fp)
# # sr_image = model.predict(image)

# # sr_image.save(img_fp)

# result = sr.upsample(img)

# # large_image = cartoon_upsampling_4x( '/content/ren.png', './a_4x_larger_output_image.png')
# # result = sr.upsample(img)

# # Resized image
# # resized = cv2.resize(result,dsize=None,fx=4,fy=4)
# resized = cv2.resize(result,dsize=None,fx=4,fy=4)
# cv2.imwrite('/content/res.jpg',resized)
# # else:
# #   img = cv2.imread(img_fp)
# #   result = sr.upsample(img)
# #   cv2.imwrite('/content/res.png',result)
# # img = im.open(img_fp).convert('RGB')

# # enhancer = ImageEnhance.Contrast(img)
# # img = enhancer.enhance(1)
# # img = img.point(lambda x: 0 if x < 150 else 255)
# # img.save('rgb.JPG')

# # p2t = Pix2Text(languages=['en'],text_config={'score_threshold':0.5,'det_bbox_max_expand_ratio':0.5})
# p2t = Pix2Text(languages=['en'],text_config={'det_model_name':"en_PP-OCRv3_det",'score_threshold':0.5,'det_bbox_max_expand_ratio':0.5})
# outs = p2t('res.jpg')


# outs = [out for out in outs if out['type'] == 'isolated']

# # pattern = re.compile(r'[+-\/*=±]')

# for out in outs:
#   text = out['text']
#   # if pattern.search(text):
#   #   annotations.append(out)
#   text=text.strip()
#   text=text.replace('$$','').replace('\prime','2').replace('\circ','2').replace('{{}','').replace('{}','').replace('\\','').replace('{}','').replace('&','').replace(', , ,','').replace('pm','±').replace('leqslant','≤').replace('leq','≤')
#   print(text)