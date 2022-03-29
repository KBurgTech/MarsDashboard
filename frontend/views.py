import random

from django.views.generic import TemplateView

from backend import weather_api, distance_api, api, color_api, picture_api
from backend.mood import MOODS, MOODS_NAME


def average(lst):
    return sum(lst) / len(lst)


def heartbeat_to_mood(avg_heartbeat):
    avg = 80
    if avg_heartbeat >= avg + 10:
        return MOODS.Depressed
    if avg_heartbeat >= avg + 8:
        return MOODS.Angry
    if avg_heartbeat >= avg + 1:
        return MOODS.Anxious

    if avg_heartbeat < avg:
        return MOODS.Calm

    return MOODS.Normal


def calculate_color(mood, sleep):
    mood_col = [int(numeric_string) for numeric_string in color_api.get_color_for_mood(mood).split(",")]
    if sleep < 7:
        mood_col[0] = (mood_col[0] + 255) / 2
        mood_col[1] = (mood_col[1] + 0) / 2
        mood_col[2] = (mood_col[2] + 0) / 2

    return f"{mood_col[0]}, {mood_col[1]}, {mood_col[2]}"


def calculate_lighting(mood, sleep):
    color = calculate_color(mood, sleep)
    return color

JOKES = [
    "What do Alexander the Great and Winnie the Pooh have in common? Same middle name.",
    "I was horrified when my wife told me that my six-year-old son wasn't actually mine. Apparently I need to pay more attention during school pick-up.",
    "What is the opposite of a croissant? A happy uncle.",
    "If April showers bring May flowers, what do May flowers bring? Pilgrims.",
    "Which branch of the military accepts toddlers? The infantry.",
    "Did you know you can actually listen to the blood in your veins? You just have to listen varicosely.",
    "Though I enjoy the sport, I could never date a tennis player. Love means nothing to them.",
    "I have a joke about time travel, but I'm not gonna share it. You guys didn't like it.",
    "What's the opposite of irony? Wrinkly.",
    "I was kidnapped by mimes once. They did unspeakable things to me.",
]


def random_joke():
    return random.choice(JOKES)


def get_status(mood):
    if mood == MOODS.Depressed:
        return f"down. Here is a joke for you: {random_joke()}"
    if mood == MOODS.Angry:
        return "mad about something. Talking can help!"
    if mood == MOODS.Anxious:
        return "anxious today. Did you get enough exercise?"
    if mood == MOODS.Normal:
        return "having a good day! Enjoy it!"

    return "doing well! Continue!"


def get_image_search(mood):
    if mood == MOODS.Depressed:
        return f"happy"
    if mood == MOODS.Angry:
        return "peace"
    if mood == MOODS.Anxious:
        return "calm"
    if mood == MOODS.Normal:
        return "sunshine"

    return "mars"


class IndexView(TemplateView):
    template_name = "Index.html"

    def get_context_data(self, **kwargs):
        OVERRIDES = {
            'Mood': MOODS.Depressed,
            'Avg_Heartbeat': None,
            'Avg_Sleep': None,
            'Avg_Sleep_Interrupt': None,
            'Weather': None
        }
        context = super(IndexView, self).get_context_data(**kwargs)
        context['weather'] = weather_api.get_weather()
        context['distance'] = {
            'au': '{:#.3} '.format(distance_api.distance(1)),
            'km': '{:#.3} '.format(distance_api.distance_km(1)),
            'time': '{:#.3} '.format(distance_api.distance_km(1) / (1079252848.80 * 0.9))
        }
        context['health'] = {
            'sleep': api.sleep_api(),
            'heartbeat': api.hearbeat_api()
        }
        context['data'] = {
            'heartbeat_avg': OVERRIDES['Avg_Heartbeat'] or average(
                context['health']['heartbeat']['datasets'][0]['data']),
            'mood': OVERRIDES['Mood'] or heartbeat_to_mood(
                OVERRIDES['Avg_Heartbeat'] or average(context['health']['heartbeat']['datasets'][0]['data'])),
            'mood_str': MOODS_NAME[OVERRIDES['Mood']] if OVERRIDES['Mood'] is not None else MOODS_NAME[
                heartbeat_to_mood(
                    OVERRIDES['Avg_Heartbeat'] or average(context['health']['heartbeat']['datasets'][0]['data']))],
            'sleep_avg': OVERRIDES['Avg_Sleep'] or average(context['health']['sleep']['datasets'][0]['data']),
            'sleep_interrupt_avg': OVERRIDES['Avg_Sleep_Interrupt'] or average(
                context['health']['sleep']['datasets'][1]['data'])
        }
        context['message'] = {
            'status': get_status(context['data']['mood'])
        }
        context['settings'] = {
            'color': f"rgba({calculate_color(context['data']['mood'], context['data']['sleep_avg'])},0.3)",
            'light': f"rgb({calculate_lighting(context['data']['mood'], context['data']['sleep_avg'])})",
            'background': picture_api.get_animal_picture_link(get_image_search(context['data']['mood'])),
        }

        return context
