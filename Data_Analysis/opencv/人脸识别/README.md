# opencv
1. 在opencv_pyhton中，子模块cv2，该模块中有opencv相应的方法封装于此
2. cv2读取图片格式是BGR
3. cv2显示图片，   
	cv2.imshow('winname', img);   
	cv2.waitKey(time)   
	cv2.destroyAllWindows()
4. 猫脸识别，CasCadeClassifier(级联分类，给什么数据，识别什么样的图片)
5. detectMultiScale检测目标值的方法
	- img, 待检对象
	- scaleFactor缩放比例默认值是1.1
	- minNeighbors周围检测出来数量，筛选条件（数值越大越苛刻，越小越松散）
	- minSize, 人脸最小尺寸的限制
	- maxSize, 人脸最大尺寸的限制

6. 识别人脸，人眼，嘴
7. cv2调用了摄像头，将摄像头所拍摄的图片进行了人脸识别