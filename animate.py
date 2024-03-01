import turtle
import time

list = []

screen = turtle.Screen()
screen.bgcolor("black")

# Register shapes

class Car(turtle.Turtle):
    def __init__(self, rank, base_speed, react_time):
        super().__init__()
        # turtle.Turtle.__init__(self)
        self.rank = rank
        self.base_speed = base_speed
        self.speed = base_speed
        self.slowing = False
        self.waiting_to_act = False
        self.react_time = react_time
        self.until_react = react_time

        self.penup()
        self.shape("circle")
        self.goto(-screen.window_width() / 2 + 20, 0)
        self.color("dark sea green")
        self.animate()

    def decrement_until_react(self):
        self.until_react -= 100

    def begin_slowing(self):
        self.slowing = True

    def change_speed(self, new_speed):
        self.speed = new_speed
        
    def animate(self):
        self.forward(self.speed)
        screen.ontimer(self.animate, 1000)
        
def spawn_cars(max_cars):
    n = 1
    while n <= max_cars:
        speed = 100
        react_time = 200
        list.append(Car(n, speed, react_time))
        n += 1
        
def within_vision(car, car_ahead):
    # for now, set to 200 units you can see over the dashboard
    distance_between = car_ahead.xcor() - car.xcor()
    if (car_ahead.slowing and 
    distance_between <= 200 and
    distance_between > 0):
        car.waiting_to_act = True

def detect_risk(car_num):
    car = list[car_num]
    # case 1: the first car instantly stops
    if (car.rank == 1 and car.slowing):
        car.change_speed = 0
    # i.e. car.rank > 1
    else:
        car_ahead = list[car_num - 1]
        within_vision(car, car_ahead)
        
def respond_to_traffic():
    i = 0
    slowing_time = 20
    gap = 100
    while i < max_cars:
        car = list[i]
        print("looking at car", car.rank)
        if (i > 0):
            front_car = list[i-1]
            detect_risk(i)
            distance_before_collide = front_car.xcor() - car.xcor()
            if (car.waiting_to_act == True and car.slowing == False):
                # Case 1: Still haven't registered the reaction
                if (car.until_react == 0):
                    # Case 1a) begin to slow
                    car.begin_slowing()
                    car.change_speed(distance_before_collide/slowing_time)
                    print("C", car.rank, "begins to slow, new speed is ", car.speed)
                else:
                    # Case 1b) continue waiting for driver to react --> eventually develop to make sure no acciedental overtakes e.g. car 2 speeds over car 1
                    car.decrement_until_react()
            elif (car.slowing and distance_before_collide <= gap):
                # Case 2: HALT!
                car.speed = 0
                print("halt")
            elif (car.slowing and distance_before_collide >= gap):
                # Case 3: Continue slowing
                car.speed = distance_before_collide/2
        elif (i == 0 and car.slowing == True):
            car.speed = 0
        elif (i == 0 and car.waiting_to_act == True):
            car.decrement_until_react()
        car.animate()
        i += 1

def incident(lead_car_rank, time):
    screen.ontimer(list[lead_car_rank].begin_slowing(), time)
    # make this interactive later on

# CONTROL BOX:
max_cars = 3

spawn_cars(max_cars)
incident(0, 500)

while list[2].xcor() < screen.window_width() / 2:
    time.sleep(2)
    respond_to_traffic()

screen.mainloop()
