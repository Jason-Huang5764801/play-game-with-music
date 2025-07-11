datalogger.onLogFull(function () {
    control.reset()
})
music.onEvent(MusicEvent.MelodyStarted, function () {
    random = randint(0, 4)
    sprite = game.createSprite(random, random)
    sprite.change(LedSpriteProperty.X, random)
    sprite.change(LedSpriteProperty.Y, random)
    sprite.ifOnEdgeBounce()
    if (sprite.isTouchingEdge()) {
        datalogger.log(datalogger.createCV("edge touched", edge))
        datalogger.mirrorToSerial(true)
        game.addScore(-1)
        edge += 1
    } else if (sprite.isTouching(game.createSprite(2, 2))) {
        game.addScore(1)
    }
})
let sprite: game.LedSprite = null
let random = 0
let edge = 0
edge = 1
datalogger.includeTimestamp(FlashLogTimeStampFormat.Days)
basic.forever(function () {
    while (true) {
        music.play(music.stringPlayable("C5 A B G A F G E ", 500 / 2), music.PlaybackMode.UntilDone)
    }
})
