# ball_types.py


class Ball(object):
    """Represent a ball."""

    def __init__(self, ball_type="regular") -> None:
        """Initialize ball type."""
        self.ball_type = ball_type

    
    
ball_1 = Ball()
ball_2 = Ball("super")

print(ball_1.ball_type)
print(ball_2.ball_type)
