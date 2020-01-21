from django import template
from dapsa.models import MiningQueue, TestDoc

register = template.Library()


def get_web(asin):
    amazons = {
        1: "https://www.amazon.com/dp/",
        3: "https://www.amazon.co.uk/dp/",
        4: "https://www.amazon.de/dp/",
        5: "https://www.amazon.fr/dp/",
        35691: "https://www.amazon.it/dp/",
        44551: "https://www.amazon.es/dp/",
        7: "https://www.amazon.ca/dp/"
    }
    marketplaceid = asin.marketplace_id

    return amazons[marketplaceid]+asin.asin+"/?psc=1"

@register.filter
def get_marketplace_name(asin):
    amazons = {
        1: "US",
        3: "UK",
        4: "DE",
        5: "FR",
        35691: "IT",
        44551: "ES",
        7: "CA"
    }
    marketplaceid = asin.marketplace_id
    return amazons[marketplaceid]

@register.filter
def open_tt(tt):
    return tt[2:]


register.filter('get_web', get_web)
