from transformers import TrOCRProcessor
from optimum.onnxruntime import ORTModelForVision2Seq
import os
import zipfile
import latex2mathml.converter
import warnings
warnings.filterwarnings('ignore')
from PIL import Image

processor = TrOCRProcessor.from_pretrained('breezedeus/pix2text-mfr')
model = ORTModelForVision2Seq.from_pretrained('breezedeus/pix2text-mfr', use_cache=False)
prohibited_symbols = {'+', '-', '*', '/','±','=','>','<'}

def download_img(url):
    return Image.open(url).convert('RGB')

def extractImage(imageList, prs, ppt_filename):
    for pageNum,slide in enumerate(prs.slides):
       pageNum+=1
       for imgNum,shape in enumerate(slide.shapes):
        if hasattr(shape,"image"):
          imgNum+=1
          if shape.image:
             image_data = shape.image.blob
             image_name = shape.image.filename
             temp_img_name = f"{ppt_filename.split('.')[0]}_{pageNum}_{imgNum}_{image_name}"
             imageList.append(temp_img_name)
             with open(temp_img_name, "wb") as f:
                f.write(image_data)

def processImage(data,fileName):
    try:
        prcessedtextFile = textGenerationfunc(data,fileName)
        return prcessedtextFile
    except Exception as e:
        print(e.args)

def processImagezip(image , fileName):
    try:
        prcessedtextFile = textGenerationfunczip(image,fileName)
        return prcessedtextFile
    except Exception as e:
        print(e.args)

def readImages(file):
    success = False
    if not os.path.exists("outtxt1"):
        os.mkdir('outtxt1')
    try:
        with zipfile.ZipFile(file, "r") as zip_ref:
            for filename in zip_ref.namelist():
                if (filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith(".png") or filename.endswith(".PNG")) and (not filename.startswith("__MACOSX/")):
                    with zip_ref.open(filename, "r") as image_data:
                        csv = processImagezip(image_data , filename)
                    del image_data
        success=True
        return success
    except Exception as e:
        print(e.args)

def textGenerationfunc(data,fileName):
    imgName = fileName.split('.')[0]
    images=[download_img(data)]
    pixel_values = processor(images=images, return_tensors="pt").pixel_values
# print(f'pixel_values', pixel_values)
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
    targetTxt = f"output_text/{imgName}.txt"
    for i in range(0,len(generated_text)):
        generated_texts = generated_text[i].split('\\\\')
        with open(targetTxt, 'w') as f:
    # Iterate through each element in the list
            for text in generated_texts:
                if any(symbol in text for symbol in prohibited_symbols):                             
                    text=text.replace('$$','').replace('sin','999999999').replace('cos','999999998').replace('tan','9999999997').replace('cosec','9999999996').replace('sec','9999999995').replace('cot','9999999994').replace(' ','').replace('cdot',' ').replace('\prime','2').replace('begin{aligned}','').replace('\circ','2').replace('{{}','').replace("{}",'').replace('\\','').replace('&','').replace(',,,','').replace('pm','±').replace('leqslant','≤').replace('leq','≤')
                    text=text.strip()
            # text='{{frac}{f(a+h)-f(a)}{h}}={frac}{(2a^{2}+4ah+2h^{2}-5a-5h+1)-(2a^{2}-5a+1)}{h}}'
                    mathml_output = latex2mathml.converter.convert(text)
                    mathml_output=mathml_output.replace('&#x0007C;','|').replace('&#x00021;','').replace('&#x00028;','(').replace('999999999','sin').replace('999999998','cos').replace('9999999997','tan').replace('9999999996','cosec').replace('9999999995','sec').replace('9999999994','cot').replace('&#x0002B;','+').replace('&#x00029;',')').replace('&#x0002F;','/').replace('&#x0002A;','*').replace('<mi>','').replace('&#x0002C;','').replace('</mi>','').replace('stretchy="false"','').replace(' ','').replace('&#x0003E;','>').replace('&#x0003C;','<').replace('&#x0003D;','=').replace('&#x02212;','-').replace('&#x000A0','~').replace('displaystyle','')
# 
        # Write each element to the text file
                    f.write(mathml_output + '\n')
                                                           
# Close the file
        f.close()
        # totalGeneratedTextList.append(generated_texts)
    return targetTxt

def textGenerationfunczip(data,fileName):
    imgName = fileName.split('.')[0]
    images=[download_img(data)]
    pixel_values = processor(images=images, return_tensors="pt").pixel_values
# print(f'pixel_values', pixel_values)
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)
    targetTxt = f"outtxt1/{imgName}.txt"
    for i in range(0,len(generated_text)):
        generated_texts = generated_text[i].split('\\\\')
        with open(targetTxt, 'w') as f:
    # Iterate through each element in the list
            for text in generated_texts:
                if any(symbol in text for symbol in prohibited_symbols):                             
                    text=text.replace('$$','').replace('sin','999999999').replace('cos','999999998').replace('tan','9999999997').replace('cosec','9999999996').replace('sec','9999999995').replace('cot','9999999994').replace(' ','').replace('cdot',' ').replace('\prime','2').replace('begin{aligned}','').replace('\circ','2').replace('{{}','').replace("{}",'').replace('\\','').replace('&','').replace(',,,','').replace('pm','±').replace('leqslant','≤').replace('leq','≤')
                    text=text.strip()
            # text='{{frac}{f(a+h)-f(a)}{h}}={frac}{(2a^{2}+4ah+2h^{2}-5a-5h+1)-(2a^{2}-5a+1)}{h}}'
                    mathml_output = latex2mathml.converter.convert(text)
                    mathml_output=mathml_output.replace('&#x0007C;','|').replace('&#x00021;','').replace('&#x00028;','(').replace('999999999','sin').replace('999999998','cos').replace('9999999997','tan').replace('9999999996','cosec').replace('9999999995','sec').replace('9999999994','cot').replace('&#x0002B;','+').replace('&#x00029;',')').replace('&#x0002F;','/').replace('&#x0002A;','*').replace('<mi>','').replace('&#x0002C;','').replace('</mi>','').replace('stretchy="false"','').replace(' ','').replace('&#x0003E;','>').replace('&#x0003C;','<').replace('&#x0003D;','=').replace('&#x02212;','-').replace('&#x000A0','~').replace('displaystyle','')
# 
        # Write each element to the text file
                    f.write(mathml_output + '\n')

# Close the file
        f.close()
        # totalGeneratedTextList.append(generated_texts)
    return targetTxt