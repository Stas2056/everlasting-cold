
init 1:

    
    image li normal casual = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'image/sprites/li_casual.png', (0, 0), 'image/sprites/li_cry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1050, 1080), (0, 0), 'image/sprites/li_casual.png', (0, 0), 'image/sprites/li_cry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1050, 1080), (0, 0), 'image/sprites/li_casual.png', (0, 0), 'image/sprites/li_cry.png'))

    
