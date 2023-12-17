# from flask import Flask, send_from_directory
# app = Flask(__name__)
 
# @app.route("/<filename>")
# def home(filename):
#     return send_from_directory('detected_image', filename)

 
# if __name__ == "__main__":
#     app.run()

import cv2
#Python 재설치 했으니까 이따가 인터넷 환경에서 모듈 설치 ㄱㄱ
import numpy as np

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")  
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]


classes = []
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")


cap = cv2.VideoCapture(0)  

# cap = cv2.VideoCapture(url)
#URL을 사용할 경우 문자열의 형태로 url 넣기

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, channels = frame.shape

    # 이미지를 YOLO 입력 형식으로 처리
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confs = []
    boxes = []

    #오브젝트 정보 추출
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            conf = scores[class_id]
            if conf > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                #박스 관련
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confs.append(float(conf))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.5, 0.4) 

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confs[i]

            cv2.rectangle(frame, (x, y), (x + w, y + h), [0,0,0], 2)
            cv2.putText(frame, f"{label} {(confidence*100):.2f}%", (x, y + 30), cv2.FONT_HERSHEY_PLAIN, 1, [0,0,0], 2)

            try:
                if label == 'person':
                    cropped_img = frame[y:y+h, x:x+w]
                    cv2.imwrite(f'../Web/detected_image/person_{i+1}.jpg', cropped_img)  # 이미지 저장
            except cv2.error:
                print(cropped_img)
                break

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == 27:  # esc 종료
        break

cap.release()
cv2.destroyAllWindows()

