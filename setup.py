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
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-domain-language",
    version = "0.0.1",
    author = "Sandro Covo",
    author_email = "sandro@sandrocovo.ch",
    description = ("A django app that allows to swich the language based on the domain",),
    license = "GPLv3",
    keywords = "django translation",
    url = "",
    packages=['domain_lang'],
    long_description=read('README'),
)
