# AICUP-2021-Traditional_Chinese_Scene_Text_Scene
## Install 
<pre><code> $ git clone https://github.com/ultralytics/yolov5</code></pre>
<pre><code> $ cd yolov5</code></pre>
<pre><code> $ pip install -r requirements.txt</code></pre>
## Links

* yolov5 file

You may be using [https://drive.google.com/drive/folders/1eFujH_Cv-ygDIAZUzALhcxiSMpWIhY-e?usp=sharing](https://drive.google.com/drive/folders/1eFujH_Cv-ygDIAZUzALhcxiSMpWIhY-e?usp=sharing).
* Colab

You may be using [https://drive.google.com/drive/folders/1Q_4tzM9pKTcsa6opo2VUAhslmhYQA4WV?usp=sharing](https://drive.google.com/drive/folders/1Q_4tzM9pKTcsa6opo2VUAhslmhYQA4WV?usp=sharing).
## Environment Setting
* yolov5/data資料夾中新增TWStreet.yaml

* Goole Driver下載yolov5\runs\train\exp8\weights\best.pt把它放在yolov5資料夾中指定位置

## Training

**第一次訓練**  
<pre><code>!python train.py --img 640 --batch 8 --epochs 300 --data data/TWStreet.yaml --weights yolov5x.pt
</code></pre>
**Colab中斷 想持續訓練**
<pre><code>!python train.py --img 640 --batch 8 --epochs 300 --data data/TWStreet.yaml --weights /content/drive/MyDrive/yolov5/runs/train/exp8/weights/last.pt
</code></pre>

## Images

![This is a alt text.](img_3010.jpg "This is a sample image.")
