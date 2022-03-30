from backend.mood import MOODS

# https://www.mountainvistapsychology.com/color-psychology-the-effects-of-color/

COLORS = {
    MOODS.Happy: "244, 138, 29",
    MOODS.Angry: "68, 160, 227",
    MOODS.Sad: "234, 207, 42",
    MOODS.Anxious: "10, 163, 80",
    MOODS.Depressed: "255, 162, 0",
}


def get_color_for_mood(mood):
    if mood in COLORS:
        return COLORS[mood]
    else:
        return "200,200,200"
