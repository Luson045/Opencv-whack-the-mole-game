import cv2
import mediapipe as mp
import turtle
import random
import time
import os
import threading

def timer():
    global my_timer
    global stop
    my_timer=-5
    while True:
        my_timer+=1
        time.sleep(1)
timer_thread=threading.Thread(target=timer,daemon=True)
timer_thread.start()
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = 1980,1080
center_x = 0
center_y = 0
screen=turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
turtle.bgcolor("black")
text=turtle.Turtle()
text.speed(20)
text.goto(-450,300)
text.color("darkgreen")
text.begin_fill()
for i in range(4):
    text.fd(500)
    text.rt(90)
text.end_fill()
text.color("brown")
a=-400
b=200
for j in range(3):
    for i in range(3):
        text.penup()
        text.goto(a,b)
        text.pendown()
        text.begin_fill()
        text.circle(50)
        text.end_fill()
        a+=200
    a=-400
    b-=200
fire=turtle.Turtle()
turtle.addshape(os.getcwd()+"/hammer2.gif")
fire.shape(os.getcwd()+"/hammer2.gif")
fire.penup()
obj1=turtle.Turtle()
obj1.penup()
turtle.addshape(os.getcwd()+"/mole.gif")
obj1.shape(os.getcwd()+"/mole.gif")
obj1.speed(15)
obj1.goto(-800,600)
fire.speed(20)
text=turtle.Turtle()
text.penup()
text.color("lightblue")
text.hideturtle()
text.goto(400,200)
text.write("welcome\nsmash the \n MOUSE",font=("niagara solid",21,"bold"))
points=0
mx=[-400,-200,0]
my=[250,50,-150]
while True:
    if my_timer==60:
        turtle.clear()
        obj1.goto(-100,0)
        fire.goto(-100,70)
        text.clear()
        text.write("time up. \n your score:"+str(points),font=("niagara solid",27,"bold"))
        time.sleep(5)
        quit()
    text.clear()
    text.write("time: "+str(my_timer)+"/npoints: "+str(points),font=("niagara solid",27,"bold"))
    if random.randint(1,20) == 3:
        obj1.goto(random.choice(mx),random.choice(my))
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = (landmark.x*frame_width)
                y = (landmark.y*frame_width)
                if id == 9:
                    cv2.circle(img=frame, center=(int(x),int(y)), radius=10, color=(0, 255, 255))
                    center_x = (x*(screen_width//frame_width)//2)-600
                    center_y = -((screen_height//frame_height*y)//2-350)
                    fire.goto(center_x,center_y)
                if fire.distance(obj1)<=50:
                    text.clear()
                    obj1.goto(random.choice(mx),random.choice(my))
                    points+=1
                    text.write("time: "+str(my_timer)+"/npoints: "+str(points),font=("niagara solid",27,"bold"))
    cv2.imshow('your screen', frame)
    cv2.waitKey(1)
