import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
CHARACTER_SCALING = 5
MOVEMENT_SPEED = 2

RIGHT = 0
LEFT = 1


def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, mirrored=True)
    ]


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.set_position(100, 100)
        self.idle_texture_pair = load_texture_pair("ninja_idle.png")
        self.texture = self.idle_texture_pair[RIGHT]
        self.scale = CHARACTER_SCALING
        self.character_face_direction = RIGHT
        self.walk_textures = []
        self.current_texture = 0
        for i in range(2):
            texture = load_texture_pair(f"ninja_walk{i}.png")
            self.walk_textures.append(texture)

    def update(self):
        """
        Update the sprite.
        """
        if self.change_x < 0:
            self.character_face_direction = LEFT
        elif self.change_x > 0:
            self.character_face_direction = RIGHT

        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.change_x == 0 and self.change_y == 0:
            self.texture = self.idle_texture_pair[self.character_face_direction]
            #start a timer/ waiting period
            #if timer exceeds certIN LIMIT PLY ANIMATION

        else:
            self.current_texture += 1
            if self.current_texture > 1:
                self.current_texture = 0
            self.texture = self.walk_textures[self.current_texture][self.character_face_direction]


class MenuScreen(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Menu Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text("Press Esc. to pause", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100, arcade.color.BLACK,
                         font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = CultGame()
        self.window.show_view(game)


class CultGame(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)
        self.player = Player()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        self.player.update()


# class MyGame
#     def
#
# class PauseScreen
#     def
#


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Instruction and Game Over Views Example")
    menu = MenuScreen()
    window.show_view(menu)

    arcade.run()


if __name__ == "__main__":
    main()
