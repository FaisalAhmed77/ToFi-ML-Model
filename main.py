
# load and display an image with Matplotlib
from matplotlib import image
from matplotlib import pyplot
import matplotlib.pyplot as plt
from PIL import Image
import pandas as pd
import numpy as np
import seaborn as sns
from gtda.homology import CubicalPersistence
from gtda.diagrams import BettiCurve
from gtda.diagrams import Silhouette
import glob

# Setting Dimension

homology_dimensions = [1]
CP = CubicalPersistence(
                    homology_dimensions=homology_dimensions,
                    coeff=3,
                    n_jobs= 1
)
BC = BettiCurve()
#SC = Silhouette(0.5)

# Reading Viable Tumor images from Files


file = "C://Users/16823/Desktop/All Datasets/Tumor_tiles_256x256_final/train/viable/"

img_file = list(glob.glob1(file, "*.jpg"))
img = []
for i in img_file:
    img.append(i)

data = []
for i in img:
    image_path = file + i
    gray_h1=Image.open(image_path).convert('L')
    im_gray_h1 = np.array(gray_h1)
    diagram_h1_0 =CP.fit_transform(np.array(im_gray_h1)[None, : , :])
    y_betti_curves_h1_0 = BC.fit_transform(diagram_h1_0)
    data.append(np.reshape(y_betti_curves_h1_0,100))
df0 = pd.DataFrame(data)
df0["label"] = [0]*len(data)

df0.to_excel("df_vt_Betti_1.xlsx")
df0

# Reading Non Viable tumor from files

file1 = "C://Users/16823/Desktop/All Datasets/Tumor_tiles_256x256_final/train/non-viable-tumor/"

img_file1 = list(glob.glob1(file1, "*.jpg"))
img1 = []
for i in img_file1:
    img1.append(i)

data1 = []
for i in img1:
    image_path1 = file1 + i
    gray_h1=Image.open(image_path1).convert('L')
    im_gray_h1 = np.array(gray_h1)
    diagram_h1_0 =CP.fit_transform(np.array(im_gray_h1)[None, : , :])
    y_betti_curves_h1_0 = BC.fit_transform(diagram_h1_0)
    data1.append(np.reshape(y_betti_curves_h1_0,100))
df01 = pd.DataFrame(data1)
df01["label"] = [1]*len(data1)

df01.to_excel("df_nvt_Betti_1.xlsx")
df01


# Reading Non Tumor images from Files


file2 = "C://Users/16823/Desktop/All Datasets/Tumor_tiles_256x256_final/train/non-tumor/"

img_file2 = list(glob.glob1(file2, "*.jpg"))
img2 = []
for i in img_file2:
    img2.append(i)

data2 = []
for i in img2:
    image_path2 = file2 + i
    gray_h1=Image.open(image_path2).convert('L')
    im_gray_h1 = np.array(gray_h1)
    diagram_h1_0 =CP.fit_transform(np.array(im_gray_h1)[None, : , :])
    y_betti_curves_h1_0 = BC.fit_transform(diagram_h1_0)
    data2.append(np.reshape(y_betti_curves_h1_0,100))
df02 = pd.DataFrame(data2)
df02["label"] = [2]*len(data2)

df02.to_excel("df_nt_Betti_1.xlsx")
df02