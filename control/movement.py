from gpiozero import Motor

class Movement():
    def __init__(self) -> None:
        self.Rmotor = Motor(6,5) # 핀 넘버 추가하기
        self.Lmotor = Motor(27,22) #얘도 핀 넘버 추가하기
        return
    
    def forward(self):
        self.Rmotor.forward(speed=1)
        self.Lmotor.forward(speed=1)
    
    def rightForward(self):
        self.Rmotor.forward(speed=0.5)
        self.Lmotor.forward(speed=1)

    def leftForward(self):
        self.Rmotor.forward(speed=1)
        self.Lmotor.forward(speed=0.5)   
    
    def backward(self):
        self.Rmotor.backward(speed=1)
        self.Lmotor.backward(speed=1)

    def rightBackward(self):
        self.Rmotor.backward(speed=0.5)
        self.Lmotor.backward(speed=1)

    def leftBackward(self):
        self.Rmotor.backward(speed=1)
        self.Lmotor.backward(speed=0.5)

    def rightRotate(self):
        self.Rmotor.backward(speed=1)
        self.Lmotor.forward(speed=1)

    def leftRotate(self):
        self.Lmotor.backward(speed=1)
        self.Rmotor.forward(speed=1)
    
    def stop(self):
        self.Lmotor.stop()
        self.Rmotor.stop()