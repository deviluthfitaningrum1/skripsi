# Skripsi: Analisis Kinerja YOLO (You Only Look Once) untuk Deteksi Objek pada Penyakit Tanaman Kentang
Kentang adalah salah satu tanaman umbi yang berpotensi menjadi makanan pokok, serta memiliki tinggi manfaat bagi tubuh. Banyaknya peran kentang menyebabkan
peningkatan permintaan dan nilai ekonomi kentang. Namun produktivitas kentang di Indonesia pada tahun 2022 masih sangat rendah yaitu 19,2 ton/ha. Selain itu, impor kentang
Indonesia pada Januari 2023 sangat tinggi yaitu sebesar 7160 ton. Berdasarkan rendahnya
produktivitas dan tingginya impor kentang di Indonesia, dapat diketahui bahwa produksi kentang di Indonesia belum memenuhi permintaan. Faktor utama yang menghambat
produksi kentang adalah penyakit tanaman. Penyakit yang umumnya menyerang dan memiliki dampak besar pada tanaman kentang adalah early blight (bercak kering) dan late
blight (hawar daun). Penyakit tersebut ditandai dengan pola pada daun yang dapat diklasifikasikan oleh model machine learning maupun deep learning. Namun pada penelitian
sebelumnya, model belum dapat mendeteksi lokasi daun kentang yang terinfeksi. Pada
penelitian ini, model deep learning diterapkan untuk mendeteksi kelas dan lokasi penyakit tanaman kentang pada daun. Model deep learning yang digunakan adalah model
Convolutional Neural Network (CNN) dari keluarga You Only Look Once (YOLO) yaitu YOLOv5m, YOLOv6m, YOLOv7, dan YOLOv8m. Model dilatih dengan 2100 citra
dan divalidasi dengan 600 citra, kemudian diuji dengan 300 citra. Pengujian dilakukan untuk mengetahui kinerja model berdasarkan akurasi deteksi, kompleksitas model,
dan waktu komputasi. Hasil pengujian kemudian dievaluasi untuk menemukan model
dengan kinerja terbaik. Model dengan kinerja terbaik untuk mendeteksi penyakit tanaman kentang adalah YOLOv6m dengan mAP@0.5 bernilai 0,995, mAP@0.5:0.95 bernilai
0,979, parameter berjumlah 34,8 juta, waktu pelatihan 1,55 jam, dan waktu deteksi 22,38
ms. YOLOv6m dipilih sebagai model terbaik karena YOLOv6m menghasilkan akurasi
deteksi yang sebanding dengan kompleksitas model dan waktu komputasinya. Deteksi
YOLOv6m mencapai hasil akurasi yang tinggi, baik pada citra terstruktur maupun citra
tidak terstruktur.

Kata kunci : Deep Learning, Convolutional Neural Network (CNN), You Only Look Once
(YOLO), Early Blight, Late Blight

Dataset: https://drive.google.com/file/d/1UwtR3dcTv6ghTlfQGp8AcQtIbu6ZsApR/view?usp=sharing

Sampel hasil deteksi: https://drive.google.com/drive/folders/1GZmaUwjFdv4XN-ywgXS_jDbX_NhaCexx?usp=sharing

Model: YOLOv5m, YOLOv6m, YOLOv7, YOLOv8m
