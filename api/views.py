from django.http import JsonResponse, HttpResponseServerError

from .exceptions import ParsingException
from .scrapers import scrape_character_by_id


def scrape_char_view(request, lodestone_id):
    try:
        char = scrape_character_by_id(lodestone_id)

    except ParsingException as e:
        return HttpResponseServerError(e.message)

    return JsonResponse(char.as_dict())
