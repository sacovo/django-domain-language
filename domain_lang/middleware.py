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
from django.utils import translation

from domain_lang.models import DomainLanguageMapping

class DomainLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        domain = request.META.get('HTTP_HOST', '')
        query = DomainLanguageMapping.objects.filter(domain=domain)

        if query.exists():
            mapping = query[0]
            translation.activate(mapping.language)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
