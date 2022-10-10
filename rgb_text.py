import framebuf

def text(display, text, x=0, y=0, color=0xffff, background=0x0000):
    x = min(display.width - 1, max(0, x))
    y = min(display.height - 1, max(0, y))
    w = display.width - x
    h = min(display.height - y, 8)
    #+1 height for background fill, to fix line draw problem
    h2 = min(display.height - y, 8)
    buffer = bytearray(display.width * h * 2)
    fb = framebuf.FrameBuffer(buffer, w, h, framebuf.RGB565)
    fb2 = framebuf.FrameBuffer(buffer, w, h2, framebuf.RGB565)
    for line in text.split('\n'):
        fb2.fill(background)
        #changed y from 0 to 1 to so text is not cut at the top
        fb.text(line, 0, 1, color)
        display.blit_buffer(buffer, x, y, w, h)
        y += 8;
        if y >= display.height:
            break