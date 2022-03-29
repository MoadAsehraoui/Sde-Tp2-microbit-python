def on_button_pressed_a():
    images.icon_image(IconNames.HAPPY).show_image(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    images.icon_image(IconNames.SAD).show_image(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Hello SdE2!")
Var1 = "Moad Asehraoui"

def on_forever():
    led.plot(2, 3)
    basic.pause(200)
    led.unplot(2, 3)
basic.forever(on_forever)


# Exo 3:
if input.button_is_pressed(Button.A):
    images.icon_image(IconNames.HAPPY).show_image(1)
elif input.button_is_pressed(Button.B):
    images.icon_image(IconNames.SAD).show_image(0)

def on_forever():
    pass
basic.forever(on_forever)

# Exo 4 : 

var4 = 0
for var5 in range(5):
    var4 = var5 / 1
    for index in range(4):
        led.plot(var4, var4)
        var5 += 1

def on_forever():
    pass
basic.forever(on_forever)

