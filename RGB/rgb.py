def rgb(r, g, b):
    def clamp(val):
        return max(0, min(255,val))
    return '{:02X}{:02X}{:02X}'.format(clamp(r),clamp(g),clamp(b))