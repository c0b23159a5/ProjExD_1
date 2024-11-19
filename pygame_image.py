import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0
    # bg_width 800
    bg_img1 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        background_image_frame_move = -(tmr%3200)
        screen.blit(bg_img, [background_image_frame_move, 0])
        screen.blit(bg_img1, [background_image_frame_move+1600, 0])
        screen.blit(bg_img, [background_image_frame_move+3200, 0])
        screen.blit(bg_img1, [background_image_frame_move+4800, 0])

        screen.blit(kk_img, [300, 200])

        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()