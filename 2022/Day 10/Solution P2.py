data = open('2022\Day 10\Input.in').read().split('\n')
sprite_position = 1
crt_position = 0
crt = []
cycle = 1

def draw_on_crt(screen, crtpos, spritepos):
    if crtpos >= (spritepos -1) and crtpos <= (spritepos + 1):
        screen.append('#')
        if crtpos % 40 == 0: crtpos = 0
        crtpos += 1
    else:
        screen.append('.')
        if crtpos % 40 == 0: crtpos = 0
        crtpos += 1
    return screen, crtpos

for i in data:
    i = i.split(' ')
    if i[0] == 'addx':
        crt, crt_position = draw_on_crt(crt, crt_position, sprite_position)
        cycle += 1
        crt, crt_position = draw_on_crt(crt, crt_position, sprite_position)
        cycle += 1
        sprite_position += int(i[1])

    elif i[0] == 'noop':
        crt, crt_position = draw_on_crt(crt, crt_position, sprite_position)
        cycle += 1

for i in range(len(crt)):
    if not i % 40 == 0:
        print(crt[i], end="")
    else:
        print('')