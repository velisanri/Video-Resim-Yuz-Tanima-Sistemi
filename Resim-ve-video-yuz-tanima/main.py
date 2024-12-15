import cv2

face_cascade = cv2.CascadeClassifier(
    r"classifier/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(r"photos/test.mp4")
while cap.isOpened():
    # Videodan bir kare okur. '_' değeri kullanılmayan bir dönüş değeridir (okuma başarılı mı bilgisi).
    _,img = cap.read()

    #img = cv2.imread(r"photos/deniz.jpeg.jpg")

    # Okunan kareyi gri tonlamaya çevirir (Yüz tespiti için).
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Gri tonlamalı görüntüde yüz tespiti yapar.
    # 1.1: Ölçek faktörü (yüz algılama sırasında farklı boyutlar için),
    # 4: Minimum komşu dikdörtgen sayısı (algılama doğruluğunu artırır).
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    # Tespit edilen yüzler için bir döngü başlatır.
    for(x,y,w,h) in faces:
         # Yüzün bulunduğu alana yeşil bir dikdörtgen çizer.
        # (x, y): Dikdörtgenin sol üst köşesi,
        # (x+w, y+h): Dikdörtgenin sağ alt köşesi,
        # (0, 255, 0): RGB formatında yeşil renk,
        # 3: Çizgi kalınlığı.
        cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

    # Tespit edilen yüzleri gösteren görüntüyü ekrana getirir.
    cv2.imshow('img',img)
    # Klavyeden 'q' tuşuna basıldığında döngüyü kırar.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Video kaynağını serbest bırakır.
cap.release()
