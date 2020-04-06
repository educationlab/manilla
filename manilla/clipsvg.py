#!/usr/bin/env python

import subprocess
import shlex
import cairo

import gi
gi.require_version('Rsvg', '2.0')
from gi.repository import Rsvg as rsvg

def get_svg_info(f_input):
    output = subprocess.check_output(
        shlex.split(f"inkscape --query-all {f_input}")
        )
    output = output.decode("utf-8")
    svg_info = output.split("\n")
    print(svg_info[0])

    return svg_info[0].split(",")[1:]

def clip_svg(f_input, f_output, margin):
    x, y, width, height = list(map(float, get_svg_info(f_input)))

    svg = rsvg.Handle.new_from_file(f_input)
    surface = cairo.SVGSurface(f_output, 
                               width + margin * 2, 
                               height + margin * 2 + 1)
    ctx = cairo.Context(surface)
    ctx.translate(-x + margin + 13, -y + margin + 11)
    svg.render_cairo(ctx)
    surface.finish()
