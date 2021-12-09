import turtle as t

scale = 30

def move(movement):
    t.goto(t.xcor() + scale * movement[0], t.ycor() + scale * movement[1])
def drawnum(num):
    nums = (((0, 0), (1, 0), (0, -2), (-1, 0), (0, 2)), #0
        ((0, -1), (1, 1), (0, -2,)), #1
        ((0, 0), (1, 0), (0, -1), (-1, -1), (1, 0)), #2
        ((0, 0), (1, 0), (-1, -1), (1, 0), (-1, -1)), #3
        ((0, 0), (0, -1), (1, 0), (0, 1), (0, -2)), #4
        ((1, 0), (-1, 0), (0, -1), (1, 0), (0, -1), (-1, 0)), #5
        ((1, 0), (-1, -1), (1, 0), (0, -1), (-1, 0), (0, 1), (1, 1)), #6
        ((0, 0), (1, 0), (-1, -1), (0, -1)), #7
        ((0, 0), (1, 0), (0, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (-1, 0), (0, 1)), #8
        ((0, -2), (1, 1), (0, 1), (-1, 0), (0, -1), (1, 0), (0, 1))) #9
    for i in range(len(num)):
        digit = int(num[i])
        t.pu()
        t.goto(2 * (i-5) * scale, 0)
        move(nums[digit][0])
        t.pd()
        for j in range(1, len(nums[digit])):
            move(nums[digit][j])

t.shape('turtle')
t.shapesize(0.8)
t.speed(2)
t.color('blue')

drawnum(input())

    
