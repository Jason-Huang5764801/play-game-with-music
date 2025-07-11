def on_log_full():
    control.reset()
datalogger.on_log_full(on_log_full)

def on_melody_started():
    global random, sprite, edge
    random = randint(0, 4)
    sprite = game.create_sprite(random, random)
    sprite.change(LedSpriteProperty.X, random)
    sprite.change(LedSpriteProperty.Y, random)
    sprite.if_on_edge_bounce()
    if sprite.is_touching_edge():
        datalogger.log(datalogger.create_cv("edge touched", edge))
        datalogger.mirror_to_serial(True)
        game.add_score(-1)
        edge += 1
    elif sprite.is_touching(game.create_sprite(2, 2)):
        game.add_score(1)
music.on_event(MusicEvent.MELODY_STARTED, on_melody_started)

edge = 1
sprite: game.LedSprite = None
random = 0
datalogger.include_timestamp(FlashLogTimeStampFormat.DAYS)

def on_forever():
    while True:
        music.play(music.string_playable("C5 A B G A F G E ", 500 / 2),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
