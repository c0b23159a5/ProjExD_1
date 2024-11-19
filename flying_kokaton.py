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
    bg_img1 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_rect = kk_img.get_rect()
    kk_rect.center = (300, 200)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        key_lst = pg.key.get_pressed()
        spped_x,speed_y =-1,0
        if key_lst[pg.K_UP]:
            speed_y += -1
            # kk_rect.move_ip(0, -1)
        elif key_lst[pg.K_DOWN]:
            speed_y += 1
            # kk_rect.move_ip(0, 1)
        if key_lst[pg.K_LEFT]:
            spped_x += -1
            # kk_rect.move_ip(-1, 0)
        elif key_lst[pg.K_RIGHT]:
            spped_x += 2
            # kk_rect.move_ip(1, 0)
        kk_rect.move_ip(spped_x,speed_y)

        background_image_frame_move = -(tmr%3200)
        screen.blit(bg_img, [background_image_frame_move, 0])
        screen.blit(bg_img1, [background_image_frame_move+1600, 0])
        screen.blit(bg_img, [background_image_frame_move+3200, 0])
        screen.blit(bg_img1, [background_image_frame_move+4800, 0])
        screen.blit(kk_img, kk_rect)
        # screen.blit(kk_img, [300, 200])

        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()