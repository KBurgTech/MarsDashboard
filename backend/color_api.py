from backend.mood import MOODS

# https://www.mountainvistapsychology.com/color-psychology-the-effects-of-color/

COLORS = {
    MOODS.Happy: "#44a0e3",
    MOODS.Angry: "#44a0e3",
    MOODS.Sad: "#eacf2a",
    MOODS.Anxious: "#0aa350",
}


def get_color_for_mood(mood):
    return COLORS[mood]
