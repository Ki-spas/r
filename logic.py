import keras
import tensorflow as tf
from PIL import Image, ImageOps # Installing pillow instead of PIL
import numpy as np
def detect_thee( image, model , label):
  np.set_printoptions(suppress=True)
  model = tf.keras.models.load_model( model , compile=False)
  class_names = open(label, "r" ).readlines()
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  image = image.convert("RGB")
  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
  data[0] = normalized_image_array
  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]
  return class_name, confidence_score

def infor_class( name  , score ):
 if name == "деревья":
   if  score >= 50 :
    print("это дерево. Дерево — это многолетнее растение с одревесневающим стволом, корнями и кроной из ветвей. Оно относится к высшим растениям, обладая долговечностью и способностью расти в высоту в течение всей жизни. Деревья являются основой лесных экосистем, играя ключевую роль в кислородном балансе планеты, и делятся на хвойные и лиственные виды")
   else  :
     print(" скорее всего это дерево . Деревья и травы — это жизненные формы высших растений, объединенные общими биологическими процессами и строением. Они питаются через фотосинтез, имеют корни, листья, почки и стебли, а также нуждаются в воде и минералах из почвы для жизни и размножения. Главное различие — структура стебля (одревесневшая у деревьев, мягкая у трав)")

 else :
   if score  >= 50:
     print ( "это трава . Трава — это жизненная форма высших растений, имеющих мягкие, не одревесневающие надземные стебли, которые отмирают в конце сезона. Они составляют основной покров земли, включая газонные, дикорастущие, сорные и сельскохозяйственные культуры. Также травянистые растения используются как лекарственное сырье")
   else : print(" скорее всего это трава . Трава и деревья похожи тем, что оба являются высшими растениями: они фотосинтезируют (создают органику на свету), имеют корни, стебли (ствол) и листья, а также дышат и размножаются. В основе их сходства лежит общее строение клеток и потребность в воде, свете и питательных веществах из почвы.")


if __name__ == "__main__":
  name,score =  detect_thee ("image.jpg" ,"keras_model.h5" ,"labels.txt" )
  print(name)
  print(score)
