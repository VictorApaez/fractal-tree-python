import turtle

def draw_tree(branch_len, t):
    if branch_len > 3:
        if branch_len < 20:
            t.color("green")
        else:
            t.color("brown")

        t.forward(branch_len)
        t.right(20) 
        draw_tree(branch_len - 10, t)
        t.left(40) 
        draw_tree(branch_len - 10, t)
        t.right(20)
        t.backward(branch_len)

t = turtle.Turtle()
t.speed('fastest')
win = turtle.Screen()

t.left(90)  
t.up()
t.backward(150)
t.down()
t.color("brown")

draw_tree(100, t)  
win.exitonclick() 
