""" 
    django-domain-language is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from django import template
from django.urls import translate_url as django_translate_url

from domain_lang.models import DomainLanguageMapping



register = template.Library()

@register.simple_tag()
def translate_url(url, language_code):
    # Returns an absolute url
    query = DomainLanguageMapping.objects.filter(language=language_code)
    if query.exists():
        mapping = query[0]
        url = django_translate_url(url, mapping.language)
        protocol = url.rpartition('//')[0] + url.rpartition('//')[1]
        domain = mapping.domain
        path = url.partition('/')[0] + url.partition('/')[-1]
        return protocol + domain + path
    return url

