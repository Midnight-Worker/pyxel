import pyxel

SCREEN_WIDTH, SCREEN_HEIGHT, FPS = 320, 180, 30
PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_COLOR = 20, 20, 10, 10, 1

pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=FPS)
pyxel.load("res.pyxres")    # Resourcendatei aus dem Editor laden

def update(): 
    global PLAYER_X
    global PLAYER_Y 
    # --- Tastatur abfragen und
    #     Pfeiltasten prüfen ---
    if pyxel.btn(pyxel.KEY_LEFT):   # Wenn Button(btn) = Pfeiltaste Links
        PLAYER_X -= 1               # dann 1 Pixel von der X-koordinate abziehen

    if pyxel.btn(pyxel.KEY_RIGHT):  # Wenn Button = Pfeiltaste Rechts
        PLAYER_X += 1               # dann 1 Pixel zur X-Koordinate hinzurechnen

    if pyxel.btn(pyxel.KEY_UP):     # Wenn Button = Pfeiltaste hoch
        PLAYER_Y -= 1               # dann 1 Pixel von der Y-Koordinate abziehen

    if pyxel.btn(pyxel.KEY_DOWN):   # Wenn Button = Pfeiltaste runter
        PLAYER_Y += 1               # dann 1 Pixel zur Y-Kooridnate hinzuzählen
    
    # Der Inhalt von update() wird 30 mal pro Sekunde durchlaufen und
    # neu berechnet draw() löscht den Bildschirm und zeichnet 30 mal 
    # pro Sekunde das Bild an den neuen Koordinaten x und y auf dem
    # Bildschirm (Screen)
    
def draw(): 
    pyxel.cls(0) 
    
    Image_bank, Transparent_color = 0, 0
    Picture_u, Picture_v, Picture_w, Picture_h = 0, 0, 16, 16
    
    pyxel.blt(PLAYER_X, PLAYER_Y, Image_bank, Picture_u, Picture_v, Picture_w, Picture_h, Transparent_color)
    pyxel.text(20, 5, "Health - 100     Weapon - 20     A-Bomb - 1", 15)
    
pyxel.run(update, draw)