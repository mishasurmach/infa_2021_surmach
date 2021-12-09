import turtle as t

scale = 30

def move(movement):
    t.goto(t.xcor() + scale * movement[0], t.ycor() + scale * movement[1])

font = open('text.txt', 'r')
           
def drawnum(num):
    nums = font.read()
    
    for i in range(len(num)):
        digit = int(num[i])
        t.pu()
        t.goto(2 * (i-5) * scale, 0)
        move(nums[digit][0])
        t.pd()
        for k in range(len(nums)):
            nums[digit][movement][k] = int(nums[digit][movement][k])
            for j in range(1, len(nums[digit])):
                move(nums[digit][j])

t.shape('turtle')
t.shapesize(0.8)
t.speed(2)
t.color('blue')

drawnum(input())

font.close()
