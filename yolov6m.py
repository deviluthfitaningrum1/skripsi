# -*- coding: utf-8 -*-
"""YOLOv6m

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14vjnqeFqwpkAADoTZ9Rc56oFQoj5CCfS

## **Clone dan install YOLOv6**
"""

#mounting google drive
from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
#path direktori clone YOLOv6
# %cd /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6

#clone YOLOv6
!git clone https://github.com/meituan/YOLOv6.git

#path direktori hasil clone
cd YOLOv6

# Commented out IPython magic to ensure Python compatibility.
#install YOLOv6
# %pip install -r requirements.txt

#clone YOLOv6m
!wget https://github.com/meituan/YOLOv6/releases/download/0.2.0/yolov6m.pt

# Commented out IPython magic to ensure Python compatibility.
#install library addict
# %pip install addict

"""## **Implementasi dan Evaluasi Model YOLOv6**

###**Pelatihan dan Pengujian Data dengan epoch 20**

#### Pelatihan Data
"""

#melatih data dengan epoch 20
!python tools/train.py --batch 16 --img 640 --epochs 20 --conf configs/yolov6m_finetune.py --data-path data/dataset.yaml --device 0

"""#### Pengujian Data"""

#menguji model dengan dataset validasi
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch20/train/best_ckpt.pt --do_pr_metric=True --do_coco_metric=False

#menguji model dengan dataset pengujian
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch20/train/best_ckpt.pt --task test --do_pr_metric=True --do_coco_metric=False

"""#### Tugas Deteksi"""

#memprediksi dataset pengujian
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/train20/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/images/test --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --save-dir /content/drive/Shareddrives/Skripsi/Yolov6/result --device 0

#memprediksi data baru
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/testing --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --save-dir /content/drive/Shareddrives/Skripsi/Yolov6 --name testing20 --device 0

"""###**Pelatihan dan Pengujian Data dengan epoch 30**

#### Pelatihan Data
"""

#melatih data dengan epoch 30
!python tools/train.py --batch 16 --img 640 --epochs 30 --conf configs/yolov6m_finetune.py --data-path data/dataset.yaml --device 0

"""#### Pengujian Data"""

#menguji model dengan dataset validasi
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch30/train/weights/best_ckpt.pt --do_pr_metric=True --do_coco_metric=False

#menguji model dengan dataset pengujian
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch30/train/weights/best_ckpt.pt --task test --do_pr_metric=True --do_coco_metric=False

"""#### Tugas Deteksi"""

#memprediksi dataset pengujian
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/train30/weights/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/images/test --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --save-dir /content/drive/Shareddrives/Skripsi/Yolov6/result --device 0

#memprediksi data baru
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/runs/train/exp/weights/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/testing --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --device 0  --save-dir /content/drive/Shareddrives/Skripsi/Yolov6/result

"""###**Pelatihan dan Pengujian Data dengan epoch 40**

#### Pelatihan Data
"""

#melatih data dengan epoch 40
!python tools/train.py --batch 16 --img 640 --epochs 40 --conf configs/yolov6m_finetune.py --data-path data/dataset.yaml --device 0

"""#### Pengujian Data"""

#menguji model dengan dataset validasi
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch40/train/weights/best_ckpt.pt --do_pr_metric=True --do_coco_metric=False

#menguji model dengan dataset pengujian
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch40/train/weights/best_ckpt.pt --task test --do_pr_metric=True --do_coco_metric=False

"""#### Tugas Deteksi"""

#memprediksi dataset pengujian
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/train40/weights/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/images/test --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --save-dir /content/drive/Shareddrives/Skripsi/Yolov6/result --device 0

#memprediksi data baru
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/runs/train/exp1/weights/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/testing --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --device 0 --save-dir /content/drive/Shareddrives/Skripsi/Yolov6/result

"""###**Pelatihan dan Pengujian Data dengan epoch 50**

#### Pelatihan Data
"""

#melatih data dengan epoch 50
!python tools/train.py --batch 16 --img 640 --epochs 50 --conf configs/yolov6m_finetune.py --data-path data/dataset.yaml --device 0

"""#### Pengujian Data"""

#menguji model dengan dataset validasi
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch50/train/weights/best_ckpt.pt --do_pr_metric=True --do_coco_metric=False

#menguji model dengan dataset pengujian
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch50/train/weights/best_ckpt.pt --task test --do_pr_metric=True --do_coco_metric=False

"""#### Tugas Deteksi"""

#memprediksi dataset pengujian
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/train50/weights/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/images/test --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --save-dir /content/drive/Shareddrives/Skripsi/Yolov6/result --device 0

#memprediksi data baru
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/runs/train/exp2/weights/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/testing --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --device 0 --save-dir /content/drive/Shareddrives/Skripsi/Yolov6/detect

"""###**Pelatihan dan Pengujian Data dengan epoch 60**

#### Pelatihan Data
"""

#melatih data dengan epoch 60
!python tools/train.py --batch 16 --img 640 --epochs 60 --conf configs/yolov6m_finetune.py --data-path data/dataset.yaml --device 0

"""#### Pengujian Data"""

#menguji model dengan dataset validasi
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch60/train/weights/best_ckpt.pt --do_pr_metric=True --do_coco_metric=False

#menguji model dengan dataset pengujian
!python tools/eval.py --data data/dataset.yaml --batch 32 --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/epoch60/train/weights/best_ckpt.pt --task test --do_pr_metric=True --do_coco_metric=False

"""#### Tugas Deteksi"""

#memprediksi dataset pengujian
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/result/train60/weights/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/images/test --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --save-dir /content/drive/Shareddrives/Skripsi/Yolov6/result --device 0

#memprediksi data baru
!python tools/infer.py --weights /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/runs/train/exp/weights/best_ckpt.pt --source /content/drive/Shareddrives/Skripsi/Yolov6/testing --yaml /content/drive/Shareddrives/Skripsi/Yolov6/YOLOv6/data/dataset.yaml --device 0 --save-dir /content/drive/Shareddrives/Skripsi/Yolov6/detect