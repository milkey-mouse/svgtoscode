import sys

from svgpathtools import svg2paths2, Line
from webcolors import name_to_rgb, normalize_hex

CURVE_RESOLUTION = 100
ROUND_DECIMALS = 5
DEFAULT_COLOR = (128, 128, 128)

def normalize_coord(coord, viewbox):
    if viewbox is None:
        return round(coord.real, ROUND_DECIMALS), \
               round(coord.imag, ROUND_DECIMALS)
    else:
        return round(coord.real - viewbox[0], ROUND_DECIMALS), \
               round(viewbox[3] - coord.imag + viewbox[1], ROUND_DECIMALS)

def convert(paths, attributes, viewbox):
    for path, path_attributes in zip(paths, attributes):
        for subpath in path.continuous_subpaths():
            yield ("START", *normalize_coord(subpath[0].start, viewbox))
            for segment in subpath:
                if isinstance(segment, Line):
                    yield ("MOVE", *normalize_coord(segment.end, viewbox))
                else:
                    for i in range(0, CURVE_RESOLUTION):
                        sample = segment.point(i / (CURVE_RESOLUTION - 1))
                        yield ("MOVE", *normalize_coord(sample, viewbox))
            if "fill" in path_attributes:
                fill = path_attributes["fill"]
                if fill.startswith("#"):
                    yield ("FILL", *bytes.fromhex(normalize_hex(fill)[1:]))
                else:
                    yield ("FILL", *name_to_rgb(fill))
            else:
                yield ("FILL", *DEFAULT_COLOR)

if len(sys.argv) < 2:
    print("usage: svg2paths [svg]")
    sys.exit(1)

*svg, svg_attributes = svg2paths2(sys.argv[1])

if "viewbox" in svg_attributes:
    viewbox = map(int, svg_attributes["viewbox"].split())
else:
    viewbox = None
    for line in convert(*svg, None):
        if line[0] in {"START", "MOVE"}:
            if viewbox is None:
                viewbox = [line[1], line[2], line[1], line[2]]
            else:
                viewbox = [min(viewbox[0], line[1]), min(viewbox[1], line[2]),
                           max(viewbox[2], line[1]), max(viewbox[3], line[2])]

for line in convert(*svg, viewbox):
    print(*line)
