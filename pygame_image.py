import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgs = pg.transform.flip(bg_img, True, False)
    kk_img = pg.transform.flip(pg.image.load("ex01/fig/3.png"), True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if tmr==3200:
            tmr=0
        tmr += 1

        screen.blit(bg_img, [0-tmr, 0])
        screen.blit(bg_imgs, [1600-tmr, 0])
        screen.blit(bg_img, [3200-tmr, 0])
        if tmr%100 >= 50:
            screen.blit(kk_imgs[0], [300, 200])
        else:
            screen.blit(kk_imgs[1], [300, 200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
