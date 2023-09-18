# Skripsi: Analisis Kinerja YOLO (You Only Look Once) untuk Deteksi Objek pada Penyakit Tanaman Kentang
Kentang adalah salah satu tanaman umbi yang berpotensi menjadi makanan po-
kok, serta memiliki tinggi manfaat bagi tubuh. Banyaknya peran kentang menyebabkan
peningkatan permintaan dan nilai ekonomi kentang. Namun produktivitas kentang di In-
donesia pada tahun 2022 masih sangat rendah yaitu 19,2 ton/ha. Selain itu, impor kentang
Indonesia pada Januari 2023 sangat tinggi yaitu sebesar 7160 ton. Berdasarkan rendahnya
produktivitas dan tingginya impor kentang di Indonesia, dapat diketahui bahwa produk-
si kentang di Indonesia belum memenuhi permintaan. Faktor utama yang menghambat
produksi kentang adalah penyakit tanaman. Penyakit yang umumnya menyerang dan me-
miliki dampak besar pada tanaman kentang adalah early blight (bercak kering) dan late
blight (hawar daun). Penyakit tersebut ditandai dengan pola pada daun yang dapat dikla-
sifikasikan oleh model machine learning maupun deep learning. Namun pada penelitian
sebelumnya, model belum dapat mendeteksi lokasi daun kentang yang terinfeksi. Pada
penelitian ini, model deep learning diterapkan untuk mendeteksi kelas dan lokasi pe-
nyakit tanaman kentang pada daun. Model deep learning yang digunakan adalah model
Convolutional Neural Network (CNN) dari keluarga You Only Look Once (YOLO) yai-
tu YOLOv5m, YOLOv6m, YOLOv7, dan YOLOv8m. Model dilatih dengan 2100 citra
dan divalidasi dengan 600 citra, kemudian diuji dengan 300 citra. Pengujian dilakuk-
an untuk mengetahui kinerja model berdasarkan akurasi deteksi, kompleksitas model,
dan waktu komputasi. Hasil pengujian kemudian dievaluasi untuk menemukan model
dengan kinerja terbaik. Model dengan kinerja terbaik untuk mendeteksi penyakit tanam-
an kentang adalah YOLOv6m dengan mAP@0.5 bernilai 0,995, mAP@0.5:0.95 bernilai
0,979, parameter berjumlah 34,8 juta, waktu pelatihan 1,55 jam, dan waktu deteksi 22,38
ms. YOLOv6m dipilih sebagai model terbaik karena YOLOv6m menghasilkan akurasi
deteksi yang sebanding dengan kompleksitas model dan waktu komputasinya. Deteksi
YOLOv6m mencapai hasil akurasi yang tinggi, baik pada citra terstruktur maupun citra
tidak terstruktur.
Kata kunci : Deep Learning, Convolutional Neural Network (CNN), You Only Look Once
(YOLO), Early Blight, Late Blight

Potato is one of the tuber crops that has the potential to become a staple food
and has high benefits for the body. The many roles of potato leads an increase in demand
and economic value of potato. However, productivity of potato in Indonesia still very low
at 19,2 ton/ha in 2022. In addition, Indonesia’s import of potato is very high in January
2023 that is 7160 tonnes. Based on low productivity and high import of potato in Indo-
nesia, it can be seen that potato production has not fulfilled the demand. The main factor
that inhibit potato production is plant disease. Disease that commonly attack and have
a big impact on potato plant is early blight and late blight. The diseases characterized
by pattern on potato leaves which can be classified by machine learning and deep lear-
ning models. However in several previous researchs, the models have not been able to
detect the location of infected potato leaves. In this research, the deep learning models
applied to detect the class and the location of potato diseases on leaves. The deep lear-
ning models used are Convolutional Neural Network (CNN) models from the You Only
Look Once (YOLO) family, especially YOLOv5m, YOLOv6m, YOLOv7, and YOLOv8m.
The models were trained with 2100 images and validated with 600 images, then tested
with 300 images. Testing was conducted to find out model performance based on dete-
ction accuracy, model complexity, and computation time. The test results are evaluated
to find the model with the best performance. The best performance model to detect potato
diseases is YOLOv6m with mAP@0.5 is 0,995, mAP@0.5:0.95 is 0,979, there are 34,8
million parameters, the training time is 1,55 hours, and the detection time is 22,38 ms.
YOLOv6m was chosen as the best model because YOLOv6m produces detection accura-
cy that is comparable with model complexity and computation time. YOLOv6m detection
achieves high accuracy results, both on structured image and unstructured image.
Keywords : Deep Learning, Convolutional Neural Network (CNN), You Only Look
Once (YOLO), Early Blight, Late Blight
