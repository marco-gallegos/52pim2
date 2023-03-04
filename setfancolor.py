import click
from rpi_ws281x import PixelStrip, Color


# LED strip configuration:
LED_COUNT = 16        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Define a dictionary of color names and their RGB values
COLORS = {
    "l_aubergine":    (119,33,111),
    "d_aubergine":    (44,0,30),
    "red":          (255, 0, 0),
    "green":        (0, 255, 0),
    "blue":         (0, 0, 255),
    "yellow":       (255, 255, 0),
    "purple":       (255, 0, 255),
    "white":        (255,255, 255),
    "bee":           (100,100,0)
}

# print([COLORS.keys()])

# Define a CLI command to set the color
@click.command()
@click.argument("color_name", type=click.Choice(list(COLORS.keys())))
def set_color(color_name:str):
    color = COLORS[color_name]

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    
    click.echo(f"Set color to {color_name} {color}")

    for pixel in range(strip.numPixels()):
        strip.setPixelColor(pixel,  Color(color[0], color[1], color[2]))
        strip.show()


if __name__ == "__main__":
    set_color()
