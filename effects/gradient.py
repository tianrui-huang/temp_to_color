from openrgb.utils import RGBColor


class Gradient:
    def __init__(self, points):
        self.points = points
    
    @staticmethod
    def lerp_color(color1, color2, t):
        '''线性插值两个颜色'''
        r = round(color1.red + (color2.red - color1.red) * t)
        g = round(color1.green + (color2.green - color1.green) * t)
        b = round(color1.blue + (color2.blue - color1.blue) * t)
        return RGBColor(r, g, b)

    def color(self, temperature):
        points = self.points
        if temperature <= points[0][0]:
            return points[0][1]
        if temperature >= points[-1][0]:
            return points[-1][1]
        for (t1, c1), (t2, c2) in zip(points, points[1:]):
            if t1 <= temperature <= t2:
                ratio = (temperature - t1) / (t2 - t1)
                return self.lerp_color(c1, c2, ratio)
            
        raise RuntimeError("Gradient calculation failed")
