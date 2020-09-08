import cv2
import glob
import numpy as np
import os


corrected_count = 0

images = glob.glob("./*.jpg")
ref_img = cv2.imread("reference_img.jpg")
for image in images:
    if "reference_img.jpg" in image:
        continue
    img = cv2.imread(image)
    if img.shape[0] != ref_img.shape[0] or img.shape[1] !=ref_img.shape[1]:
        img = cv2.resize(img, (ref_img.shape[1], ref_img.shape[0]))
    t1 = np.mean((ref_img-img)**2)
    img_rot = np.rot90(img, 2)
    t2 = np.mean((ref_img-img_rot)**2)
    if t1 > t2:
        cv2.imwrite("./corrected/"+os.path.basename(image), img_rot)
        corrected_count += 1

print("Metric : ", corrected_count/(len(images)-1))