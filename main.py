def on_sound_loud():
    global fade, H
    fade = 0
    H = 100
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_gesture_shake():
    global fade, H
    fade = 0
    H = 180
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

H = 0
fade = 0
strip = neopixel.create(DigitalPin.P2, 8, NeoPixelMode.RGB)

def on_forever():
    global fade
    for índice in range(8):
        strip.clear()
        strip.set_pixel_color(índice, neopixel.hsl(H, 255, 15))
        strip.show()
        basic.pause(fade)
    fade += 10
    if fade > 1000:
        fade = 1000
basic.forever(on_forever)
