from pathlib import Path
import colorsys


class Colour:
    def __init__(self, colour: list = [0, 0, 0], type: str = "RGB") -> None:

        self.r = colour[0]
        self.g = colour[1]
        self.b = colour[2]

        self.type = type
    
    def __repr__(self) -> None:
        return f"{self.type}: {self.r} {self.g} {self.b}"
    
    def to_RGB(self) -> None:
        if self.type == "HSV":
            rgb_colour = colorsys.hsv_to_rgb(self.r, self.g, self.b)

            self.r = rgb_colour[0]
            self.g = rgb_colour[1]
            self.b = rgb_colour[2]

            self.type = "RGB"
        else:
            print("Not a HSV colour")
    
    def to_HSV(self) -> None:
        if self.type == "RGB":
            hsv_colour = colorsys.rgb_to_hsv(self.r, self.g, self.b)

            self.r = hsv_colour[0]
            self.g = hsv_colour[1]
            self.b = hsv_colour[2]

            self.type = "HSV"
        else:
            print("Not an RGB colour")
    
    def export_24bit(self) -> list:
        colour_24bit = []

        colour_24bit.append(self._convert_to_8bit(self.r))
        colour_24bit.append(self._convert_to_8bit(self.g))
        colour_24bit.append(self._convert_to_8bit(self.b))

        return colour_24bit

    def _convert_to_8bit(self, value: float) -> int:
        value_8bit = int(value * 255)

        return value_8bit

def generate_hsv_colour_table(num_h: int, num_s: int, num_v: int) -> list[Colour]:
    h_increment = 1 / num_h
    s_increment = 1 / (num_s - 1)
    v_increment = 1 / (num_v - 1)
    
    hsv_colour_list = []

    # generate greyscale values
    for value in range(0, num_v):
        hsv_colour_list.append(Colour([0.0, 0.0, value * v_increment], type="HSV"))
    
    # generate colour values
    for hue in range(0, num_h):
        for sat in range(1, num_s):
            for val in range(1, num_v):
                hsv_colour_list.append(Colour([hue * h_increment, sat * s_increment, val * v_increment], type="HSV"))
    
    return hsv_colour_list


colour_table = generate_hsv_colour_table(12, 5, 5)

rgb_table = []
for colour in colour_table:
    colour.to_RGB()
    rgb_table.append(colour.export_24bit())

for colour in rgb_table:
    print(colour)

