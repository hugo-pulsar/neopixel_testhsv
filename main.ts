input.onSound(DetectedSound.Loud, function () {
    fade = 0
    H = 100
})
input.onGesture(Gesture.Shake, function () {
    fade = 0
    H = 180
})
let H = 0
let fade = 0
let strip = neopixel.create(DigitalPin.P0, 8, NeoPixelMode.RGB)
basic.forever(function () {
    for (let índice = 0; índice <= 7; índice++) {
        strip.clear()
        strip.setPixelColor(índice, neopixel.hsl(H, 255, 15))
        strip.show()
        basic.pause(fade)
    }
    fade += 10
    if (fade > 1000) {
        fade = 1000
    }
})
