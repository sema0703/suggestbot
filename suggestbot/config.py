#!/soft/python-2.6/bin/python
# -*- coding: utf-8 -*-
'''
SuggestBot configuration library.

If you add specific variables to this file, make sure you also
add an explanation of what they're for.

Copyright (C) 2005-2015 SuggestBot Dev Group

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the
Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
Boston, MA  02110-1301, USA.
'''

# $Id$

from __future__ import with_statement

# Dictionary to translate a language code to a descriptive language name
lang_codes={
    u'en': u'english',
    u'no': u'norwegian',
    u'sv': u'swedish',
    u'pt': u'portuguese',
    u'fa': u'persian',
    u'hu': u'hungarian',
    u'ru': u'russian',
}

# Edit comments used when posting recommendations
edit_comment = {
    'en': u"SuggestBot recommends these articles...",
    'no': u"AnbefalingsBot anbefaler disse artiklene...",
    'sv': u"FörslagsBot rekommenderar dessa artiklar...",
    'pt': u"SuggestBot recomenda estes artigos",
    'fa': u'SuggestBot recommends these articles...',
    'hu': u'SuggestBot recommends these articles...',
    'ru': u'SuggestBot предлагает следующие статьи...',
}

# Edit comments used when removing the request template
# from a user page
replace_comment = {
    'en': u"Removed SuggestBot request template to prevent multiple suggestions posts",
    'no': u"Fjernet mal for engangsanbefalinger så anbefalinger ikke sendes flere ganger",
    'sv': u"Tar bort FörslagsBots mall så förslag inte skickas fler gånger",
    'pt': u"Modelo de pedido de SuggestBot removido para evitar postagens múltiplas",
    'fa': u'Removed SuggestBot request template to prevent multiple suggestions posts',
    'hu': u'Removed SuggestBot request template to prevent multiple suggestions posts',
    'ru': u'Удаление шаблона запроса к SuggestBot для предотвращения дублирования сообщений'
}

# Table names for database tables containing task categories
# and articles found in those categories
task_table = {
    u'en': 'enwiki_work_category_data',
    u'no': 'nowiki_work_category_data',
    u'sv': 'svwiki_work_category_data',
    u'pt': 'ptwiki_work_category_data',
    u'fa': 'fawiki_work_category_data',
    u'hu': 'huwiki_work_category_data',
    u'ru': 'ruwiki_work_category_data'
}

# Configuration of categories containing articles that need work.
# update-data.py iterates over the keys in the dictionary and uses
# the various values to gather article titles.  We are doing a mapping
# from our work category names (e.g. "STUB"), to a set of categories
# that we will gather articles from, either by grabbing them directly,
# or by traversing the category tree.

# The format of the task dictionary is as follows:
# Keys: Our over-arching work category name (e.g. STUB)
# Values: A dictionary containing configuration for each work category,
#         the dictionary contains four key-value pairs as follows:
#     'categories': List of categories that we will directly
#                   gather article titles from.
#     'recurseCategories': Dictionary where the keys are category
#                          names, and the values are integers.
#                          We will traverse down sub-categories
#                          to the level defined by the integer.
#                          Thus a value of 1 will only look down one sub-level.
#     'inclusion': A string containing a regular expression we will use
#                  for inclusion.  Category names that do _not_ match
#                  this regex are ignored.
#     'exclusion': A string containing a regular expression we will use
#                  for exclusion.  Category names that _match_ this regex
#                  are ignored.

# Regular expressions used to match category names of stub categories
# so we disregard non-stub categories when traversing the category graph.
stub_re = {
    u"en": r"\b[Ss]tub", # English
    u"no": r"[Ss]tubb", # Norwegian
    u"sv": r"[Ss]tubb", # Swedish
    u"pt": ur"!Esboços (sobre|por|maiores que)", # Portuguese
    u'fa': ur'مقاله‌های خرد',
    u'hu': None,
    u'ru': ur"Незавершённые статьи",
}

tasks = {
    u'en': {
        'MERGE': {
            'categories': [u'All articles to be merged',
                           u'Articles to be merged'],
            'recurseCategories': {u'Merge by month': 1},
            'inclusion': None,
            'exclusion': stub_re[u'en'] },
        'WIKIFY': {
            'categories': [u'All articles covered by WikiProject Wikify'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None},
        'CLEANUP': {
            'categories': [u'All pages needing cleanup',
                           u'Articles with excessive see also sections',
                           u'Wikipedia introduction cleanup'
                           u"All articles needing copy edit"],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'SOURCE': {
            'categories': [u'All articles lacking reliable references',
                           u'All articles needing additional references',
                           u'All articles lacking sources',
                           u'All articles with topics of unclear notability',
                       ],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'EXPAND': {
            'categories': [u'All articles to be expanded',
                           u"All Wikipedia articles in need of updating"],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'STUB': {
            'categories': [],
            'recurseCategories': {u'Stub_categories': 5},
            'inclusion': stub_re[u'en'],
            'exclusion': None, },
        'ORPHAN': {
            'categories': [u'All orphaned articles'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'UNENC': { # unencyclopædic articles
            'categories': [u'All NPOV disputes',
                           u'All articles that may contain original research'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
    },
    u'pt': {
        'STUB': {
            'categories': [u"!Artigos mínimos", ],
            'recurseCategories': {u"!Esboços": 5},
            'inclusion': stub_re[u'pt'],
            'exclusion': None,
        },
        'TRANSLATE': {
            'categories': [],
            'recurseCategories': {u"!Artigos em tradução": 5},
            'inclusion': None,
            'exclusion': stub_re[u'pt'],
        },
        'SOURCE': {
            'categories': [u"!Artigos com referências não fiáveis",
                           u"!Artigos com citações quebradas"],
            'recurseCategories': {u"!Artigos que carecem de fontes": 5,
                                  u"!Artigos que carecem de fontes secundárias": 5,
                                  u"!Artigos que necessitam de verificação factual": 5},
            'inclusion': None,
            'exclusion': stub_re[u'pt'],
        },
        'MERGE': {
            'categories': [],
            'recurseCategories': {u"!Artigos a sofrerem fusão": 5},
            'inclusion': r"(!Artigos a sofrerem)|(!Artigos de .* a sofrerem)",
            'exclusion': stub_re[u'pt'],
        },
        'CLEANUP': {
            'categories': [],
            'recurseCategories': {u"!Páginas a reciclar": 3,
                                  u"!Artigos que necessitam de esclarecimento": 2},
            'inclusion': None,
            'exclusion': stub_re[u'pt'],
        },
        'UPDATE': {
            'categories': [],
            'recurseCategories': {u"!Artigos com dados desatualizados": 3,
                                  u"!Artigos contendo afirmações potencialmente datadas": 3,
                                  u"!Artigos a expandir": 3,
                                  u"!Artigos parciais": 3},
            'inclusion': None,
            'exclusion': stub_re[u'pt'],
        },
        'IMAGES': {
            'categories': [],
            'recurseCategories': {u"!Artigos sem imagens": 5},
            'inclusion': None,
            'exclusion': stub_re[u'pt'],
        },
    },
    u'no': {
        'KILDER': {
            # Note: As of 2013-11-11, there's only four source-related
            # categories on Norwegian Wikipedia.  We choose to recurse
            # rather than list them in case they change their category
            # structure in the future.
            'categories': [],
            'recurseCategories': {u'Artikler som trenger referanser': 3},
            'inclusion': None,
            'exclusion': stub_re[u'no'],
        },
        'FLETT': {
            "categories": [u'Artikler_som_bør_flettes'],
            "recurseCategories": {},
            "inclusion": None,
            "exclusion": stub_re[u'no'],
        },
        'OPPRYDNING': {
            "categories": [],
            "recurseCategories": {u'Opprydning': 1},
            "inclusion": None,
            "exclusion": stub_re[u'no'],
        },
        'OBJEKTIV': {
            "categories": [u'Objektivitet', u'Nøyaktighet',
                           u'Uencyklopediske_artikler'],
            "recurseCategories": {},
            "inclusion": None,
            "exclusion": stub_re[u'no'],
        },
        'UFULLSTENDIG': {
            "categories": [u'Ufullstendige_lister'],
            "recurseCategories": {},
            "inclusion": None,
            "exclusion": stub_re[u'no'],
        },
        'UTVID': {
            "categories": [u'Snevre_artikler', u'Sider som må utvides'],
            "recurseCategories": {},
            "inclusion": None,
            "exclusion": stub_re[u'no'],
        },
    'STUBBER': {
        "categories": [],
        "recurseCategories": {
            u'Stubber etter størrelse': 2,
        u'Stubber': 5},
        "inclusion": stub_re[u'no'],
        "exclusion": None,
    },
        'VSTUBB': {
            "categories": [u'Viktige stubber'],
            "recurseCategories": {},
            "inclusion": None,
        "exclusion": None,
        },
    },
    u'sv': {
        u'INFOGA': {
            'categories': [u'Samtliga artiklar föreslagna för sammanslagningar och delningar',],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
    },
        u'WIKIFIERA': {
            'categories': [u'Artiklar som behöver wikifieras-samtliga'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
    u'UOPPDATERAD': {
        'categories': [u'Ej uppdaterad-samtliga',
                       u'Samtliga utgångna bäst före'],
        'recurseCategories': {},
        'inclusion': None,
        'exclusion': None,
    },
        u'GLOBALT': {
        'categories': [u'Wikipedia:Globalt perspektiv-samtliga', ],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        u'SPRÅK': {
            'categories': [],
            'recurseCategories': {u'Artiklar som behöver språkvård': 2},
            'inclusion': None,
            'exclusion': stub_re[u'sv'],
        },
    u'KÄLLOR': {
        'categories': [u'Alla artiklar som behöver källor', ],
        'recurseCategories': {},
        'inclusion': None,
        'exclusion': None,
    },
        u'STÄDA': {
            'categories': [],
            'recurseCategories': {u'Städa': 2},
            'inclusion': None,
            'exclusion': stub_re[u'sv'],
        },
        u'STUBBAR': {
            'categories': [],
            'recurseCategories': {'Stubbar': 5},
            'inclusion': stub_re[u'sv'],
            'exclusion': ur'(Ofullständiga listor)|mallar',
        },
    },
    u'ru': {
        u'STUB': {
            'categories': [],
            'recurseCategories': {u'Незавершённые статьи по темам':5},
            'inclusion': stub_re[u'ru'],
            'exclusion': None,
        },
        'WIKIFY': {
            'categories': [u'Википедия:Статьи к викификации'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'SOURCE': {
            'categories': [u'Википедия:Статьи с утверждениями без источников'],
            'recurseCategories': {u'Википедия:Статьи с утверждениями без источников':1,
                                  u'Википедия:Статьи без ссылок на источники': 1},
            'inclusion': None,
            'exclusion': ur'Википедия:Статьи с сомнительной значимостью',
        },
        'EXPAND': {
            'categories': [u'Википедия:Статьи с незавершёнными разделами'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'ORPHAN': {
            'categories': [],
            'recurseCategories': {u'Википедия:Изолированные статьи': 1},
            'inclusion': None,
            'exclusion': stub_re[u'ru'],
        },
        'OBJECTIVITY': {
            'categories': [u'Википедия:Статьи, нейтральность которых поставлена под сомнение'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'IMAGES': {
            'categories': [u'Википедия:Статьи без иллюстраций'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'CLEANUP': {
            'categories': [u'Википедия:Статьи к переработке'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'UPDATE': {
            'categories': [u'Википедия:Статьи для обновления'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'TRANSLATE': {
            'categories': [],
            'recurseCategories': {u'Википедия:Запросы на перевод': 1},
            'inclusion': None,
            'exclusion': None,
        },
        'RELIABILITY': {
            'categories': [u'Википедия:Статьи, достоверность которых требует проверки'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'NOTABILITY': {
            'categories': [u'Википедия:Статьи с сомнительной значимостью'],
            'recurseCategories': {u'Википедия:Статьи с сомнительной значимостью по давности': 1},
            'inclusion': None,
            'exclusion': None,
        },
    },
    u'fa': {
        'STYLE': {
            'categories': [u'همه مقاله‌های نیازمند ویرایش سبک'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'EXPAND': {
            'categories': [u'مقاله‌های نیازمند گسترش'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'MERGE': {
            'categories': [u'صفحه‌های نامزد ادغام'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'OBJECTIVITY': {
            'categories': [u'همه اختلاف‌ها در بی‌طرفی'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'ORPHAN': {
            'categories': [u'مقاله‌های یتیم'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'STUB': {
            'categories': [],
            'recurseCategories': {u'رده‌های خرد':
                                  1},
            'inclusion': stub_re[u'fa'],
            'exclusion': None,
        },
        'SOURCE': {
            'categories': [u'مقاله‌های با منبع ناکافی',
                           u'همه مقاله‌های دارای عبارت‌های بدون منبع'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'IMAGES' : {
            'categories': [],
            'recurseCategories' : {u'مقاله‌های نیازمند تصویر':
                                   1},
            'inclusion': None,
            'exclusion': None,
        },
        'TRANSLATE': {
            'categories': [u'مقاله‌های نیازمند اصلاح ترجمه'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'UPDATE': {
            'categories': [u'رده:مقاله‌های نیازمند به روز شدن'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
        'WIKIFY': {
            'categories': [u'مقاله‌های نیازمند به ویکی‌سازی'],
            'recurseCategories': {},
            'inclusion': None,
            'exclusion': None,
        },
    }
}


# URL to the Tool Labs webservice used to get quality metadata
# (num. images, num. wikilinks, num. broken wikilinks) for articles
qualws_url = ur'http://tools.wmflabs.org/suggestbot/quality_metadata'

# Variables that control how we handle regulars, and store them
# in the suggestbot database.

# Name of the table that holds the list of regulars in the suggestbot database
regulars_table = "regular_users"

# Name of the table that stores logs of recommendations
reclog_table = "recommendation_log"

# Template for the name of the table that stores text index terms
term_table = "{lang}wiki_terms"

# Name of the table that stores articles in need of parsing
parse_queue = "parse_queue"

# The number of days after which we regard a user as retired,
# meaning we stop sending them suggestions.
# FIXME: make this into a relative measure, e.g. after k number of posts,
# depending on how often they get them?
retired_days = 60

# The number of seconds between checks for new suggestion requests
suggest_req_poll = 300

# Tables for storing information about requests
req_logtable = "request_log"
req_seedstable = "request_seeds"
req_recstable = "request_recs"

# The number of seconds we wait between retrieving recent changes
rc_delay = 3600

# Template filename for the recent changes daemon's pickle files
rc_pickle = "../data/recentchanges-updatetitles-{0}.dat"

# Number of days we keep revisions for, for each language
rc_keep = {
    u'en': 90,
    u'ru': 274,
    u'sv': 925,
    u'pt': 720,
    u'no': 1461,
    u'fa': 1461,
    u'hu': 1461
}

# Configuration of text tables used to store data
text_table = {
    u'en': u'enwiki_solr_text',
    u'sv': u'svwiki_solr_text',
    u'no': u'nowiki_solr_text',
    u'pt': u'ptwiki_solr_text',
    u'fa': u'fawiki_solr_text',
    u'hu': u'huwiki_solr_text',
    u'ru': u'ruwiki_solr_text',
}

# Configuration of database tables used to store revision data
# (used by the co-edit recommender)
# NOTE: this duplicates $COEDIT_TABLES in config.pm
revision_table = {
    u'en': u'enwiki_revisions',
    u'no': u'nowiki_revisions',
    u'sv': u'svwiki_revisions',
    u'pt': u'ptwiki_revisions',
    u'fa': u'fawiki_revisions',
    u'ru': u'ruwiki_revisions',
    u'hu': u'huwiki_revisions'
}

# Configuration of URLs to query each language's Solr backend,
# Page ID is substituted in at runtime.
# NOTE: we currently have separate URLs for each language to allow
# tweaking of parameters like minimum term frequency in the source document (mintf),
# minimum document frequency (mindf), and minimum word length (minwl)
solr_baseurl = {
    u'en': u"http://localhost:8080/solr/English/mlt?q=id:{pageid}&mlt.fl=text&mlt.mindf=2&mlt.mintf=2&fl=id,titleText,score&mlt.match.include=false&rows=1000&mlt.minwl=5&wt=json",
    u'no': u"http://localhost:8080/solr/Norwegian/mlt?q=id:{pageid}&mlt.fl=text&mlt.mindf=2&mlt.mintf=2&fl=id,titleText,score&mlt.match.include=false&rows=1000&mlt.minwl=5&wt=json",
    u'sv': u"http://localhost:8080/solr/Swedish/mlt?q=id:{pageid}&mlt.fl=text&mlt.mindf=2&mlt.mintf=2&fl=id,titleText,score&mlt.match.include=false&rows=1000&mlt.minwl=5&wt=json",
    u'pt': u"http://localhost:8080/solr/Portuguese/mlt?q=id:{pageid}&mlt.fl=text&mlt.mindf=2&mlt.mintf=2&fl=id,titleText,score&mlt.match.include=false&rows=1000&mlt.minwl=5&wt=json",
    u'fa': u"http://localhost:8080/solr/Persian/mlt?q=id:{pageid}&mlt.fl=text&mlt.mindf=2&mlt.mintf=2&fl=id,titleText,score&mlt.match.include=false&rows=1000&mlt.minwl=5&wt=json",
    u'hu': u"http://localhost:8080/solr/Hungarian/mlt?q=id:{pageid}&mlt.fl=text&mlt.mindf=2&mlt.mintf=2&fl=id,titleText,score&mlt.match.include=false&rows=1000&mlt.minwl=5&wt=json",
    u'ru': u"http://localhost:8080/solr/Russian/mlt?q=id:{pageid}&mlt.fl=text&mlt.mindf=2&mlt.mintf=2&fl=id,titleText,score&mlt.match.include=false&rows=1000&mlt.minwl=5&wt=json",
}

# Mapping language codes to URLs used to delete pages from Solr's
# search index
solr_delurl = {
    u'en': u'http://localhost:8080/solr/English/update/json',
    u'no': u'http://localhost:8080/solr/Norwegian/update/json',
    u'sv': u'http://localhost:8080/solr/Swedish/update/json',
    u'pt': u'http://localhost:8080/solr/Portuguese/update/json',
    u'fa': u'http://localhost:8080/solr/Persian/update/json',
    u'hu': u'http://localhost:8080/solr/Hungarian/update/json',
    u'ru': u'http://localhost:8080/solr/Russian/update/json',
}

# Configuration of what templates to use.  Complete title
# to the Wikipedia userspace article that contains the template.
# Each key is a language code, which then contains a dictionary
# where one key is 'request', that points to the template for
# one-time requests, and the other is 'regulars', which points
# to the template to use for our regular users.

# For the popularity and quality study in Aug-Sept 2011, we have added
# templates for each of the four experimental groups. (the control group
# uses 'regulars')
templates = {
    u'en': {
        'request': u'User:SuggestBot/Templates/RequestsPlain',
        'plain': u'User:SuggestBot/Templates/RegularsPlain',
        'regulars': u'User:SuggestBot/Templates/RegularsFull',
        # 'regulars': u'User:SuggestBot/Templates/Regulars',
        'popqual': u'User:SuggestBot/Templates/studytemplate-1',
        'pop': u'User:SuggestBot/Templates/studytemplate-2',
        'qual': u'User:SuggestBot/Templates/studytemplate-3',
        'combined': u'User:SuggestBot/Templates/studytemplate-4',
    },
    u'no': {
        'request': u'Bruker:AnbefalingsBot/Maler/Anbefaling',
        'regulars': u'Bruker:AnbefalingsBot/Maler/Anbefaling',
    },
    u'sv': {
        'request': u'Användare:FörslagsBot/Mallar/Enstaka',
        'regulars': u'Användare:FörslagsBot/Mallar/Regelbundna',
    },
    u'pt': {
        'request': u'Usuário(a):SuggestBot/Templates/Requests',
        'regulars': u'Usuário(a):SuggestBot/Templates/Regulars',
    },
    u'ru': {
        u'request': u'Участник:SuggestBot/Шаблоны/Запросы',
        u'regulars': u'Участник:SuggestBot/Шаблоны/Регулярные',
    },
    u'fa': {
        u'request': u'کاربر:SuggestBot/Templates/Requests',
        u'regulars': u'کاربر:SuggestBot/Templates/Regulars',
    }
}

# Templates added by our regular users.
config_templare = {
    u'en': { 'config': u'User:SuggestBot/config',
             'userbox': u'User:SuggestBot/userbox', },
    u'no': { 'config': u'Bruker:AnbefalingsBot/konfigurasjon',
             'userbox': u'Bruker:AnbefalingsBot/brukerboks', },
    u'sv': { 'config': u'Användare:FörslagsBot/konfiguration',
             'userbox': u'Användare:FörslagsBot/användarruta', },
    u'pt': { 'config': u'Usuário(a):SuggestBot/config',
             'userbox': u'Usuário(a):SuggestBot/userbox', },
    u'ru': { 'config': u'Участник:SuggestBot/Настройка',
             'userbox': u'Участник:SuggestBot/userbox',
         },
    u'fa': {
        'config': u'کاربر:SuggestBot/config',
        'userbox': u'کاربر:SuggestBot/userbox',
    }
}

# Which references we'll ignore when looking for backlinks
# when processing the regular user templates.
templater_stoplist = {
    'en': [u'User:SuggestBot/config',
           u'User:SuggestBot/Getting Recommendations Regularly', ],
    'no': [u'Bruker:AnbefalingsBot/konfigurasjon',
           u'Bruker:AnbefalingsBot/Jevnlige Anbefalinger', ],
    'sv': [u'Användare:FörslagsBot/konfiguration',
           u'Användare:FörslagsBot/Få rekommendationer regelbundet'],
    'pt': [ u'Usuário(a):SuggestBot/config',
            u'Usuário(a):SuggestBot/Getting suggestions regularly',
            u'Usuário(a):SuggestBot/Obtendo sugestões regularmente'],
    'ru': [ u'Участник:SuggestBot/Настройка',
            u'Участник:SuggestBot/Регулярные рекомендации' ],
    'fa': [ u'کاربر:SuggestBot/config',
            u'کاربر:SuggestBot/Getting suggestions regularly', ]
}

# Request templates used in the WP:Teahouse experiment
teahouse_templates = {
    u'en': [u'User:SuggestBot/th-suggest'],
    u'sv': [u'Användare:FörslagsBot/fr-förslag'],
    u'no': [],
    u'pt': [],
    u'fa': [],
    u'ru': [],
    u'hu': []
}

# Templates used for one-time requests.
# Outermost dictionary maps language codes to template configurations
# for that language.  Inner dictionary maps a template name to
# its known synonyms (synonyms are redirects to the template)
request_template = {
    u'en': {u"User:SuggestBot/suggest":
            [u"User:SuggestBot/th-suggest"],
        },
    u'no': {u'Bruker:AnbefalingsBot/anbefaling':
            [],
        },
    u'sv': {u'Användare:FörslagsBot/förslag':
            [u'Användare:FörslagsBot/fr-förslag'],
        },
    u'pt': {u'Usuário(a):SuggestBot/suggest':
            [],
            u'User:SuggestBot/suggest': [],
        },
    u'ru': { u'Участник:SuggestBot/suggest': [],
             u'User:SuggestBot/suggest': [],
         },
    u'fa': { u'کاربر:SuggestBot/suggest':
             [u'ربات پیشنهاددهنده'],
             u'User:SuggestBot/suggest':
             [u'ربات پیشنهاددهنده'],
         }
}

# Regular expressions used to match the section heading of requests
# associated with the WP:Teahouse experiment (maybe also elsewhere).
# Section headings matching this regular expression are deleted as
# SuggestBot posts the recommendations.
request_head_re = {
    u'en': ["[=]{1,3}\s*.* your editing suggestions are on the way.*\s*[=]{1,3}"],
    u'no': [],
    u'sv': ["[=]{1,3}\s*.*, dina förslag är på väg.*\s*[=]{1,3}"],
    u'pt': [],
    u'fa': [],
    u'ru': [],
    u'hu': []
}

# Name of the category parameter used in Teahouse suggestions,
# users copy & paste WikiProject names into these
th_category = {
    u'en': u'category',
    u'no': u'',
    u'sv': u'kategori',
    u'pt': u'',
    u'fa': u'',
    u'ru': u'',
    u'hu': u''
}

# Suffix used in category names to match WikiProject category names,
# e.g. on enwiki we must add ' articles' to match it correctly.
wikiproject_suffix = {
    u'en': u' articles',
    u'no': u'',
    u'sv': u'',
    u'pt': u'',
    u'fa': u'',
    u'ru': u'',
    u'hu': u''
}

# Placeholder text added when a page would otherwise be empty,
# used to make sure our edits actually get saved
empty_placeholder = {
    u'en': u'<!-- Empty placeholder left by SuggestBot, feel free to delete when necessary -->',
    u'no': u'<!-- Fyllkommentar lagt igjen av AnbefalingsBot, kan fjernes ved behov -->',
    u'sv': u'<!-- Fyllkommentar från FörslagsBot, kan tas bort vid behov -->',
    u'pt': u'<!-- Empty placeholder left by SuggestBot, feel free to delete -->',
    u'fa': u'<!-- Empty placeholder left by SuggestBot, feel free to delete -->',
    u'ru': u'<!-- Empty placeholder left by SuggestBot, feel free to delete -->',
    u'hu': u''
}

# Base-filename of file to store names of users where the configuration
# didn't parse correctly.
userlist_warnings = '../data/userlists/regulars/warnings.txt'

# Dictionary of accepted parameters for our configuration templates.
# Keys are language codes, which then map to a dictionary where each
# key is the parameter name used for the template in said language,
# and the value is the global parameter name.
template_parameters = {
    'en': {
        u'frequency': 'frequency',
        u'replace': 'replace',
        u'headlevel': 'headlevel',
    },
    'no': {
        u'frekvens': 'frequency',
        u'erstatt': 'replace',
        u'nivå': 'headlevel',
    },
    'sv': {
        u'frekvens': 'frequency',
        u'ersätt': 'replace',
        u'nivå': 'headlevel',
    },
    'pt': {
        u'frequência': 'frequency',
        u'substituir': 'replace',
        u'nível': 'headlevel',
    },
    'ru': {
        u'частота': 'frequency',
        u'заменять': 'replace',
        u'уровень': 'headlevel',
    },
    'fa': {
        u'frequency': 'frequency',
        u'replace': 'replace',
        u'level': 'headlevel',
    }
}

# Regular expressions for matching desired frequency of recommendations.
# Keys are language codes, values are the regular expression used for
# matching in that language.
once_monthly = {
    'en': ur"monthly|once a month",
    'no': ur"en gang i måneden",
    'sv': ur"en gång i månaden",
    'pt': ur"mensalmente|uma vez por mês",
    'ru': ur"ежемесячно|раз в месяц",
    'fa': ur'monthly|once a month',
}
twice_monthly = {
    'en': ur"twice a month|(every|once (a|every)) (fortnight|two weeks)",
    'no': ur"to ganger i måneden|annenhver uke",
    'sv': ur"två gånger i månaden",
    'pt': ur"quinzenalmente|duas vezes por mês",
    'ru': ur"дважды в месяц",
    'fa': ur'twice a month|every two weeks',
}
weekly = {
    # NOTE: we're allowing users to specify getting them daily, but serve them weekly
    'en': ur"(once a|twice a|every) (week|day)|weekly|daily",
    'no': ur"en gang i uken",
    'sv': ur"en gång i veckan",
    'pt': ur"uma vez por semana|semanalmente",
    'ru': ur"еженедельно|раз в неделю",
    'fa': ur'(once a|every) week|weekly',
}
        
# Dictionary holding the text of the header of the SuggestBot
# post in each language we understand.  When replacing recommendations,
# we search for this text in the document we're working on.
rec_headers = {
    'en': u'== Articles you might like to edit, from SuggestBot ==',
    'no': u'== Artikler du med glede kan redigere, fra AnbefalingsBot ==',
    'sv': u'== Artiklar du kanske vill redigera, från FörslagsBot ==',
    'pt': u'== Artigos que você gostaria de editar, de SuggestBot ==',
    'ru': u'== Статьи, которые Вам возможно захочется исправить, от SuggestBot ==',
    'fa': u'== مقاله‌های پیشنهادی توسط ربات پیشنهاددهنده ==',
}

rec_header_re = {
    'en': u'Articles you might like to edit, from SuggestBot',
    'no': u'Artikler du med glede kan redigere, fra AnbefalingsBot',
    'sv': u'Artiklar du kanske vill redigera, från FörslagsBot',
    'pt': u'Artigos que você gostaria de editar, de SuggestBot',
    'ru': u'Статьи, которые Вам возможно захочется исправить, от SuggestBot',
    'fa': u'مقاله‌های پیشنهادی توسط ربات پیشنهاددهنده',
}

# Dictionarly holding lists of titles of subsections of SuggestBot's
# post.  We will also delete the contents of these sub-headers if
# the user has invoked the "replace" option.
sub_header_re = {
    u'en': [u"Changes to SuggestBot's suggestions"],
    u'no': [],
    u'sv': [],
    u'pt': [],
    u'fa': [],
    u'ru': [],
    u'hu': []
}
        
# Regular expressions to match a Yes/No parameter value in
# all languages we speak.  Matching is done case-insensitively.
re_yes = {
    'en': ur'\s*yes\s*',
    'no': ur'\s*ja\s*',
    'sv': ur'\s*ja\s*',
    'pt': ur'\s*sim\s*',
    'ru': ur'\s*да\s*',
    'fa': ur'\s*yes\s*',
}
re_no = {
    'en': ur'\s*no\s*',
    'no': ur'\s*nei\s*',
    'sv': ur'\s*nej\s*',
    'pt': ur'\s*não\s*',
    'ru': ur'\s*нет\s*',
    'fa': ur'\s*no\s*',
}

## Regular expressions to match list-articles in the given language
## (should be in sync with the same in toolserver/links-server-*.py)
list_re = {
    u'en': ur'[Ll]ist[ _]of[ _]',
    u'no': ur'[Ll]iste[ _]over[ _]',
    u'sv': ur'[Ll]ista[ _]över[ _]',
    u'pt': ur'[Ll]ista[ _]de[ _]',
    u'hu': ur'[ _]listája$',
    u'fa': ur'^فهرست',
    u'ru': ur'(^Список|(:Алфавитный[ _]|Хронологический[ _])список)|—[ _]список'
}

# P-value cutoffs for determining if an article-specific task suggestion
# is a "yes" or a "maybe"
task_p_yes = 0.1
tesk_p_maybe = 015
        
# Maps our five dimensions to human-comprehensible task names
humantasks = {
    u'length': u'content',
    u'lengthToRefs': u'sources',
    u'headings': u'headings',
    u'numImages': u'images',
    u'completeness': u'links'
}

# Mapping of yes/maybe/no for each task category to table-sort template
# and if necessary files with matching alt-texts
task_map = {
    u'content-yes': u'{{{{Hs|0.0}}}} [[File:Redx2.svg|18px|alt=Please add more content|link={rectitle}|Please add more content]]',
    u'content-maybe': u'{{{{Hs|1.0}}}} [[File:Question mark basic.svg|20px|alt=Please check the article, it might need more content|link={rectitle}|Please check the article, it might need more content]]',
    u'content-no': u'{{{{Hs|2.0}}}}',
    
    u'headings-yes': u'{{{{Hs|0.0}}}} [[File:Redx2.svg|18px|alt=Please create proper section headings|link={rectitle}|Please create proper section headings]]',
    u'headings-maybe': u'{{{{Hs|1.0}}}} [[File:Question mark basic.svg|20px|alt=Please check the article, it might not have all the necessary section headings|link={rectitle}|Please check the article, it might not have all the necessary section headings]]',
    u'headings-no': u'{{{{Hs|2.0}}}}',
    
    u'images-yes': u'{{{{Hs|0.0}}}} [[File:Redx2.svg|18px|alt=Please add more images|link={rectitle}|Please add more images]]',
    u'images-maybe': u'{{{{Hs|1.0}}}} [[File:Question mark basic.svg|20px|alt=Please check the article, it might need more images|link={rectitle}|Please check the article, it might need more images]]',
    u'images-no': u'{{{{Hs|2.0}}}}',
    
    u'links-yes': u'{{{{Hs|0.0}}}} [[File:Redx2.svg|18px|alt=Please add more wikilinks|link={rectitle}|Please add more wikilinks]]',
    u'links-maybe': u'{{{{Hs|1.0}}}} [[File:Question mark basic.svg|20px|alt=Please check the article, it might need more wikilinks|link={rectitle}|Please check the article, it might need more wikilinks]]',
    u'links-no': u'{{{{Hs|2.0}}}}',
    
    u'sources-yes': u'{{{{Hs|0.0}}}} [[File:Redx2.svg|18px|alt=Please add more sources|link={rectitle}|Please add more sources]]',
    u'sources-maybe': u'{{{{Hs|1.0}}}} [[File:Question mark basic.svg|20px|alt=Please check the article, it might need more sources|link={rectitle}|Please check the article, it might need more sources]]',
    u'sources-no': u'{{{{Hs|2.0}}}}',
}

## Dictionary mapping low/medium/high quality
## to appropriate strings with format-parameters for inserting
## assessment class and predicted class
quality_map = {
    u'low': u'[[File:Stars310.svg|60 px|alt=Quality: Low, Assessed class: {assessedclass}, Predicted class: {predclass}|link={rectitle}|Quality: Low, Assessed class: {assessedclass}, Predicted class: {predclass}]]',
    u'medium': u'[[File:Stars320.svg|60 px|alt=Quality: Medium, Assessed class: {assessedclass}, Predicted class: {predclass}|link={rectitle}|Quality: Medium, Assessed class: {assessedclass}, Predicted class: {predclass}]]',
    u'high': u'[[File:Stars330.svg|60 px|alt=Quality: High, Assessed class: {assessedclass}, Predicted class: {predclass}|link={rectitle}|Quality: High, Assessed class: {assessedclass}, Predicted class: {predclass}]]',
}

# Table name of the status information table in the database
# (it holds one row for each defined language)
status_table = 'status_info'

# List of names of the different study groups used in the fall 2011
# experiment on adding information.
# self.config['STUDYGROUPS'] = {
#     'en': ['pop', 'qual', 'popqual', 'combined', 'control'],
#     'no': [],
#     'sv': [],
#     'pt': [],
#     }

# Dictionary mapping high/medium/low popularity,
# high/medium/low quality, and high/medium/low needslove
# to wikicode to include them in our templates.
# self.config['POPULARITY_MAP'] = {
#     u'low': u'[[File:Gnome-stock person.svg|22 px|alt=Readership: Low|Readership: Low]]',
#     u'medium': u'[[File:Gnome-system-users.svg|28 px|alt=Readership: Medium|Readership: Medium]]',
#     u'high': u'[[File:Icon of three people in different shades of grey.svg|30 px|alt=Readership: High|Readership: High]]',
#     }
# self.config['QUALITY_MAP'] = {
#     u'low': u'[[File:Stars310.svg|60 px|alt=Quality: Low|Quality: Low]]',
#     u'medium': u'[[File:Stars320.svg|60 px|alt=Quality: Medium|Quality: Medium]]',
#     u'high': u'[[File:Stars330.svg|60 px|alt=Quality: High|Quality: High]]',
#     }
# self.config['COMBINED_MAP'] = {
#     u'low': u'[[File:Green cross.svg|15 px|alt=Opportunity: Low|Opportunity: Low]]',
#     u'medium': u'[[File:Green cross.svg|15 px|alt=Opportunity: Medium|Opportunity: Medium]] [[File:Green cross.svg|15 px|alt=|Opportunity: Medium]]',
#     u'high': u'[[File:Green cross.svg|15 px|alt=Opportunity: High|Opportunity: High]] [[File:Green cross.svg|15 px|alt=|Opportunity: High]] [[File:Green cross.svg|15 px|alt=|Opportunity: High]]',
#     }

## What language Wikipedia are we working on? Usually set by individual scripts
## as necessary.
wp_langcode = u"en"

# Server configurations
# The recommendation server will always listen on "localhost:$MAIN_SERVER_PORT'
main_server_port = 10010
coedit_hostname = "localhost"
coedit_hostport = 10001
textmatch_hostname = "localhost"
textmatch_hostport = 10003
edit_server_hostname = "localhost"
edit_server_hostport = 10007
filter_server_hostname = "localhost"
filter_server_hostport = 10009
popularity_and_quality_hostname= "localhost"
popularity_and_quality_hostport= 10008

textdaemon_hostname = "localhost"
textdaemon_hostport = 10128

classifier_hostname = "localhost"
classifier_hostport = 10129

# These are kept for backwards compatibility, as the links server is now on
# the Toolserver.  The port number is used for picking recommendations.
links_hostname = "localhost"
links_hostport = 10006

# How many contributions do we maximally grab through the API
# to base our recommendations on?
# FIXME: this should be called NEDITS instead!
nrecs = 500