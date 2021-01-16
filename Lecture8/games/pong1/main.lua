WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 640

VIRTUAL_WIDTH = 432
VIRTUAL_HEIGHT = 243

function love.load()
    love.graphics.setDefaultFilter('nearest', 'nearest')
    
    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        vsync = true,
        resizable = false
    })
end

push = require 'push'

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    end   
end

function love.draw()
    push:apply('start')

    -- font size is 12
    love.graphics.printf("Hello Pong!", 0, VIRTUAL_HEIGHT / 2 - 6, VIRTUAL_WIDTH, 'center')
    
    push:apply('end')
end