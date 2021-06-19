# AICUP-2021-Traditional_Chinese_Scene_Text_Scene
## Install 
<pre><code> $ git clone https://github.com/ultralytics/yolov5</code></pre>
<pre><code> $ cd yolov5</code></pre>
<pre><code> $ pip install -r requirements.txt</code></pre>
## Environment Setting
* yolov5\data資料夾中新增TWStreet.yaml

* 下載附檔中yolov5\runs\train\exp8\weights\best.pt把它放在yolov5資料夾中指定位置

## Training

**第一次訓練**  
<pre><code>!python train.py --img 640 --batch 8 --epochs 300 --data data/TWStreet.yaml --weights yolov5x.pt
</code></pre>
**Colab中斷 想持續訓練**
<pre><code>!python train.py --img 640 --batch 8 --epochs 300 --data data/TWStreet.yaml --weights /content/drive/MyDrive/yolov5/runs/train/exp8/weights/last.pt
</code></pre>
## Detecting
<pre><code>import torch
import os
path = './res'
if not os.path.exists(path):
    os.makedirs(path)
text_name = 'res.txt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path='/content/drive/MyDrive/yolov5/runs/train/exp8/weights/best.pt')
model.conf = 0.55  # confidence threshold (0-1)
model.iou = 0.45  # NMS IoU threshold (0-1)
model.classes = None

#1-1000是PublicTest
for i in range(1,1001):
    imgs = '/content/drive/MyDrive/PublicTestDataset/PublicTestDataset/img/'+'img_'+str(i)+'.jpg' 
    results = model(imgs)
    results.print()  
    results.save()  # or .show()
    #print(results.xyxy[0])  # print img1 predictions (pixels)
    res = results.xyxy[0].numpy()
    #print(results.xyxy[0].numpy())
    f_txt= open(os.path.join(path, text_name), 'a')
    count = i
    for i in range(res.shape[0]):
        x_min = res[i][0]
        y_min = res[i][1]
        x_max = res[i][2]
        y_max = res[i][3]
        conf = res[i][4]
        f_txt = open('./res/' + text_name,'a')
        f_txt.write("%d ,%d ,%d ,%d ,%d ,%d ,%d ,%d ,%d ,%f\n" %  (count,round(x_min),round(y_min),round(x_max),round(y_min),round(x_max),round(y_max),round(x_min),round(y_max),conf))
f_txt.close()
</code></pre>
### Unordered

* Item 1
* Item 2
* Item 2a
* Item 2b

### Ordered

1. Item 1
1. Item 2
1. Item 3
  1. Item 3a
  1. Item 3b

## Images

![This is a alt text.](/image/sample.png "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.
