from django.http import HttpResponse
from PIL import Image
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
import json
import base64
import numpy as np
import sys
sys.path.append("./")
from utils_cv.crop_objects import crop_objects
from utils_cv.crop_objects import crop_objects_coord
from utils_cv.fruit_classification import fruit_classify
from utils_cv.image_processing import draw_multiple_rectangles

def get_imgresponse(img):

	img = img[:, :, ::-1]
	image = Image.fromarray(img)
	data = BytesIO()
	image.save(data, "JPEG")
	data64 = base64.b64encode(data.getvalue())
	img_data = u'data:img/jpeg;base64,'+data64.decode('utf-8')
	res = HttpResponse(img_data, content_type="image/jpeg")
	res['Access-Control-Allow-Origin'] = "*"
	#res['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
	#res['Access-Control-Allow-Headers'] = 'Origin, Content-Type, X-Auth-Token'
	#res['Access-Control-Allow-Credentials'] = 'true'
	#res['Access-Control-Max-Age'] = '1728000'
	return res

def decode_request(image_data):
	forma, imgstr = image_data.split(';base64,')
	base64_decoded = base64.b64decode(imgstr)
	image = Image.open(BytesIO(base64_decoded))
	a = np.array(image)
	a = a[:, :, :3] # remove alpha channel
	return a[:, :, ::-1]

@csrf_exempt
def send(request):
	image_data = json.loads(request.body)["image"]
	imgnp = decode_request(image_data)

	imglist, coords = crop_objects_coord(imgnp)
	labels = []
	for img in imglist:
		labels.append(fruit_classify(img))

	imgnp = draw_multiple_rectangles(np.float32(imgnp), coords, labels).astype('uint8')
	return get_imgresponse(imgnp)
