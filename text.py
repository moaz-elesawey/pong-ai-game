from constants import WHITE


def render_text(text, x, y, font, color=WHITE):
    _text = font.render(text, True, WHITE)
    text_rect = _text.get_rect()
    text_rect.center = (x, y)

    return _text, text_rect

