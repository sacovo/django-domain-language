# django-domain-language
A django app that allows to swich the language based on the domain.

You might be runing a site called `mysite.com` and want to run the german version of the site under `meineseite.de`
this app helps you doing this. You can configure what domain should be served in what language. You can also use it to
configure language specific subdomains like de.mysite.com and fr.mysite.com.

# Installation
Install the package with 
```
python setup.py install
```

Add `domain_lang` to the installed apps
```Python
INSTALLED_APPS = [
    ...
    'domain_lang',
]
```

Add the Middleware **after** `LocaleMiddleware`
```Python
MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
    'domain_lang.middleware.DomainLanguageMiddleware',
    ...
]
```

If you want to have access to the configured domains in your templates add `domain_lang.context_processors.domain_language` to the context_processors.
```
TEMPLATES = [
    {
       ...
       'OPTIONS': {
            'context_processors': [
                ...
                'domain_lang.context_processors.domain_language',
            ],
        },
    },
]
```

Finally run the migrations to create the database tables.
```
python manage.py migrate
```

# Usage
After installing it and runing the django server you will find the DomainLanguageMappings in your admin.
There you can configure the domains and their respecitve language. The Middleware will then always set the acitve language based on the domain of the reuqest.
If no Mapping is configured for the active domain the language set by `LocaleMiddleware` will be in place.

## Cookies
You have to login for each domain seperatly. If you use subdomains for your langauge selection (en.example.com, de.example.com, ...)
you can prepend the `SESSION_COOKIE_DOMAIN` with a dot, which will allow you to log in once for all subdomains.
```
SESSION_COOKIE_DOMAIN = '.example.com'
```

## Template Context
If you have added `domain_lang.context_processors.domain_language` to your context_processors, all Mappings will be provided
in the variable called `language_mappings`. You can use this to show links to other versions of your site.

## Template Tag
This app provides one template tag that allows you to translate a domain. It will also translate the domain part of the given url according to the configured mappgings
```Django
{% load domain_lang %}

{% translate_url 'mysite.com/contact/' 'de' %} # Might be translated to meineseite.de/kontakt/
```

# LICENSE

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
