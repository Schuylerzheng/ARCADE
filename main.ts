namespace SpriteKind {
    export const Backdrop = SpriteKind.create()
}
function Game_over (Winlose: boolean) {
    game.over(Winlose, effects.splatter)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Backdrop, function (sprite, otherSprite) {
    game.reset()
})
let Main_char = sprites.create(assets.image`Cuphead`, SpriteKind.Player)
let LEVEL = sprites.create(assets.image`Scene1`, SpriteKind.Backdrop)
LEVEL.setPosition(0, 0)
LEVEL.setScale(100, ScaleAnchor.Middle)
scene.setBackgroundColor(9)
scene.setBackgroundImage(assets.image`Scene2`)
info.setLife(3)
scene.cameraFollowSprite(Main_char)
forever(function () {
    while (false) {
        Main_char.y += 1
    }
})
