import pygame as pg

config = {
    'debug': 0
}

controls = [
    {
        'up': pg.K_w,
        'down': pg.K_s,
        'rotate_left': pg.K_a,
        'rotate_right': pg.K_d,
        'shoot': pg.K_f
    },
    {
        'up': pg.K_UP,
        'down': pg.K_DOWN,
        'rotate_left': pg.K_LEFT,
        'rotate_right': pg.K_RIGHT,
        'shoot': pg.K_SLASH
    },
]

layouts = [
    {
        'wall_sizes': [(1000, 10), (1000, 10), (10, 510), (10, 510), (800, 10), (800, 10)],
        'wall_positions': [(200, 100), (200, 600), (200, 100), (1200, 100), (400, 440), (200, 270)],
        'spawn_zones': [(260, 170, 20, 20), (1080, 500, 20, 20), (690, 350, 20, 20)],
        'powerup_zones': [(500, 500, 10, 10), (700, 200, 10, 10)]
    },
    {
        'wall_sizes': [(1000, 10), (1000, 10), (10, 510), (10, 510), (10, 160), (10, 160), (210, 10), (210, 10),
                       (10, 250), (10, 120), (230, 10), (240, 10), (10, 140), (240, 10)],
        'wall_positions': [(200, 100), (200, 600), (200, 100), (1200, 100), (330, 220), (530, 330), (330, 220),
                           (330, 490), (670, 100), (670, 480), (670, 350), (820, 480), (1060, 350), (820, 220)],
        'spawn_zones': [(260, 170, 20, 20), (1120, 500, 20, 20), (770, 280, 20, 20), (460, 410, 20, 20),
                        (590, 540, 20, 20)],
        'powerup_zones': [(270, 530, 10, 10), (580, 160, 10, 10), (1100, 160, 10, 10), (980, 420, 10, 10), (750, 540, 10, 10)]
    },
    {
        'wall_sizes': [(1000, 10), (1000, 10), (10, 510), (10, 510), (10, 260), (10, 260), (10, 270), (140, 10),
                       (280, 10), (420, 10), (140, 10), (10, 130), (140, 10), (10, 130)],
        'wall_positions': [(200, 100), (200, 600), (200, 100), (1200, 100), (340, 230), (1060, 230), (630, 100),
                           (340, 360), (930, 360), (500, 230), (500, 480), (490, 480), (780, 480), (780, 360)],
        'spawn_zones': [(260, 160, 20, 20), (990, 530, 20, 20), (1110, 160, 20, 20), (710, 360, 20, 20),
                        (430, 520, 20, 20)],
        'powerup_zones': [(570, 540, 10, 10), (700, 170, 10, 10), (560, 350, 10, 10), (850, 420, 10, 10), (270, 420, 10, 10)]
    },
    {
        'wall_sizes': [(1000, 10), (1000, 10), (10, 510), (10, 510), (280, 10), (280, 10), (440, 10), (140, 10),
                       (140, 10), (10, 130), (10, 130), (10, 130), (10, 130), (10, 130), (10, 140), (10, 140),
                       (10, 130)],
        'wall_positions': [(200, 100), (200, 600), (200, 100), (1200, 100), (200, 230), (780, 480), (340, 350),
                           (920, 350), (1070, 220), (340, 360), (630, 360), (490, 480), (630, 110), (920, 110),
                           (1060, 220), (780, 220), (920, 480)],
        'spawn_zones': [(260, 170, 20, 20), (1080, 420, 20, 20), (690, 290, 20, 20), (410, 490, 20, 20)],
        'powerup_zones': [(840, 550, 10, 10), (1000, 180, 10, 10), (980, 550, 10, 10), (270, 300, 10, 10)]
    },
    {
        'wall_sizes': [(1000, 10), (1000, 10), (10, 510), (10, 510), (140, 10), (140, 10), (140, 10), (140, 10),
                       (10, 130), (10, 130), (10, 130), (10, 130), (210, 10), (10, 220)],
        'wall_positions': [(200, 100), (200, 600), (200, 100), (1200, 100), (340, 230), (340, 480), (940, 230),
                           (940, 480), (940, 230), (340, 360), (480, 230), (1080, 360), (610, 230), (710, 380)],
        'spawn_zones': [(410, 300, 20, 20), (1010, 300, 20, 20), (700, 160, 20, 20)],
        'powerup_zones': [(570, 540, 10, 10), (710, 310, 10, 10), (1010, 540, 10, 10), (1130, 170, 10, 10),
                          (410, 170, 10, 10)]
    },
    {
        'wall_sizes': [(1000, 10), (1000, 10), (10, 510), (10, 510), (140, 10), (140, 10), (140, 10), (10, 130), (10, 130), (10, 130), (10, 130), (140, 10), (140, 10), (140, 10), (10, 130), (10, 130), (10, 130), (10, 130), (140, 10), (140, 10), (140, 10), (10, 130), (10, 130), (10, 130), (10, 130)],
        'wall_positions': [(200, 100), (200, 600), (200, 100), (1200, 100), (340, 230), (340, 480), (340, 350), (340, 230), (480, 230), (480, 480), (340, 480), (910, 230), (910, 480), (910, 350), (910, 230), (1050, 230), (1050, 480), (910, 480), (625, 230), (625, 480), (625, 350), (625, 230), (765, 230), (765, 480), (625, 480)],
        'spawn_zones': [(260, 280, 20, 20), (1120, 280, 20, 20), (690, 160, 20, 20), (550, 540, 20, 20), (840, 540, 20, 20)],
        'powerup_zones': [(555, 290, 10, 10), (700, 420, 10, 10), (840, 290, 10, 10), (985, 420, 10, 10), (410, 420, 10, 10)]
    },
    {
        'wall_sizes': [(1000, 10), (1000, 10), (10, 510), (10, 510), (140, 10), (10, 130), (140, 10), (10, 130),
                       (10, 130), (160, 10), (160, 10), (10, 130), (10, 130), (140, 10), (140, 10), (10, 130),
                       (10, 130), (10, 130)],
        'wall_positions': [(200, 100), (200, 600), (200, 100), (1200, 100), (340, 230), (340, 230), (485, 360),
                           (485, 360), (340, 480), (625, 230), (625, 480), (700, 480), (700, 100), (920, 230),
                           (780, 360), (910, 360), (1050, 230), (1050, 480)],
        'spawn_zones': [(260, 535, 20, 20), (1120, 160, 20, 20), (845, 290, 20, 20), (400, 160, 20, 20),
                        (630, 535, 20, 20)],
        'powerup_zones': [(400, 550, 10, 10), (750, 170, 10, 10), (980, 420, 10, 10), (550, 300, 10, 10)]
    },
    {
        'wall_sizes': [(1000, 10), (1000, 10), (10, 510), (10, 510), (140, 10), (280, 10), (10, 130), (10, 130),
                       (10, 120), (140, 10), (145, 10), (10, 130), (10, 130), (10, 130), (10, 260), (140, 10),
                       (140, 10), (140, 10), (140, 10)],
        'wall_positions': [(200, 100), (200, 600), (200, 100), (1200, 100), (340, 230), (340, 480), (340, 360),
                           (480, 230), (480, 490), (480, 360), (620, 230), (620, 100), (755, 230), (755, 480),
                           (910, 230), (910, 360), (1060, 230), (1060, 480)],
        'spawn_zones': [(260, 535, 20, 20), (400, 160, 20, 20), (630, 535, 20, 20), (980, 420, 20, 20),
                        (690, 170, 20, 20)],
        'powerup_zones': [(410, 420, 10, 10), (550, 300, 10, 10), (1120, 160, 10, 10), (830, 420, 10, 10)]
    },
]