from functools import wraps

from django.http import JsonResponse, HttpResponseServerError

from .exceptions import ParsingException
from .scrapers.character import scrape_character_by_id
from .scrapers.item import scrape_item_by_id


def json_api(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            json = f(*args, **kwargs)
        except ParsingException as e:
            return HttpResponseServerError(e.message)
        return JsonResponse(json.as_dict())
    return decorated


@json_api
def scrape_character_view(request, lodestone_id):
    return scrape_character_by_id(lodestone_id)


@json_api
def scrape_item_view(request, lodestone_id):
    return scrape_item_by_id(lodestone_id)
