# Charuco Board Information
___
  * Our calibration method relies on [Anipose](https://anipose.org)'s [Charuco-based](https://docs.opencv.org/3.4/df/d4a/tutorial_charuco_detection.html) calibration method to determine the location of each camera during a recording session. This information is later used to create the 3d reconstruction of the tracked points

  * IMPORTANT The Charuco board shown to the camera MUST be generated with the `cv2.aruco.DICT_4X4_250` dictionary! 
  
  * Ah high resoultion `png` of this Charuco board is in this repository at `/charuco_board_image_highRes.png`

## Generate your own charuco board
  * Use the following python commands (or equivalent). DO NOT CHANGE THE PARAMETERS OR THE CALIBRATION WILL NOT WORK:
	``` python
	import cv2
	
	aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_250) #note `cv2.aruco` can be installed via `pip install opencv-contrib-python`
	
	board = cv2.aruco.CharucoBoard_create(7, 5, 1, .8, aruco_dict)
	
	charuco_board_image = board.draw((2000,2000)) #`2000` is the resolution of the resulting image. Increase this number if printing a large board (bigger is better! Esp for large spaces!
	
	cv2.imwrite('charuco_board_image.png',charuco_board_image)
	
	```
