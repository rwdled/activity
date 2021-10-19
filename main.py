def on_gesture_shake():
    roll = randint(0, 6)
    if roll == 5:
        basic.show_leds("""
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            . # . # .
        """)
    elif roll == 4:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
        """)
    elif roll == 3:
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
        """)
    elif roll == 2:
        basic.show_leds("""
            # . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . #
        """)
    elif roll == 1:
        basic.show_leds("""
            . . . . .
            . # . . .
            . . . . .
            . . . # .
            . . . . .
        """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)