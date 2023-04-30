# 자동차
class Car():
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, accel):
        self.speed += accel

    def brake(self, brake_speed):
        self.speed -= brake_speed

    def get_speed(self):
        return self.speed


c = Car("Escalade", "hotpink", 120)
c.accelerate(20)
c.accelerate(100)
c.brake(10)
c.brake(10)
c.brake(30)
print(f"차량 종류{c.model}, 차량 색상{c.color}, 현재속도{c.speed}")
