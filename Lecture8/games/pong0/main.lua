WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 640

function love.load()
    love.window.setMode(WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        vsync = true,
        resizable = false
    })
end

function love.draw()
    -- font size is 12
    love.graphics.printf(("Hello Pong!", 0, WINDOW_HEIGHT / 2 - 6, WINDOW_WIDTH, 'center'))

end