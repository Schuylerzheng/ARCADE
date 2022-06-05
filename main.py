@namespace
class SpriteKind:
    Backdrop = SpriteKind.create()
def Game_over(Winlose: bool):
    game.over(Winlose, effects.splatter)

def on_on_overlap(sprite, otherSprite):
    game.reset()
sprites.on_overlap(SpriteKind.player, SpriteKind.Backdrop, on_on_overlap)

Main_char = sprites.create(assets.image("""
    Cuphead
"""), SpriteKind.player)
LEVEL = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
scene.set_background_color(9)
scene.set_background_image(assets.image("""
    TREE
"""))
info.set_life(3)

def on_forever():
    Main_char.y += 1
forever(on_forever)
