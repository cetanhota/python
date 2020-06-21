from picamera import PiCamera as pc
from time import sleep, time
import numpy as np
import tensorflow as tf
from scripts.label_image import_load_graph,read_tensor_from_image_file,load_labels

cam = pc()
image="/home/pi/Desktop/snap.jpg"
cam.capture(image)
print("Captured in {}".format(image))

graph = load_graph('tf_files/retrained_graph.pb')

t = read_tensor_from_image_file(image,
				input_height=224,
				input_width=224,
				input_mean=128,
				input_std=128)
input_operation = graph.get_operation_by_name('import/input')
output_operation = graph.get_operation_by_name('import/final_result')

with tf.Session(graph=graph) as sess:
	start = time()
	results = sess.run(output_operation.outputs[0],
					{input_operation.outputs[0]: t})
	end = time()
results = np.squeeze(results)

top_k = results.argsort()[-5:][::-1]
labels = load_labels('tf_files/retrained_labels.txt')

for in top_k:
	print(labels[i],results[i])