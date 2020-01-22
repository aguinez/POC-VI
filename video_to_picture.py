import cv2
print(cv2.__version__)
uri = "/home/alex/Imágenes/VID-20190814-WA0031/VID-20190814-WA0031_VID-20190814-WA0031.mp4"
vidcap = cv2.VideoCapture(uri)
success,image = vidcap.read()
count = 0
success = True
while success:
	cv2.imwrite("/home/alex/Imágenes/frame%d.jpg" % count, image)     # save frame as JPEG file
	success,image = vidcap.read()
	print('Read a new frame: ', success)
	count += 1