USER_AGENT_DICT = {
    'Mozilla/5.0 (Windows NT 6.1)': {
        'browser': "Mozilla",
        'system': "other",
        'is_default': True
    },
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Linux',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36': {
        'browser': "Chrome",
        'system': 'Windows',
        'is_default': False,
    },
    # Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    },
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)': {
        'browser': "Firefox",
        'system': 'Windows',
        'is_default': False,
    }

}

PARAMS = [
    {'name': 'data-cmd',
     'value': 'ok-disc'
     },
]
BASE_URL = 'https://boards.4chan.org'

SECTION = {
    # Japanese Culture
    'Anime & Manga': {
        'short_name': 'a',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/a',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Anime/Cute': {
        'short_name': 'c',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/c',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Anime/Wallpapers': {
        'short_name': 'w',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/w',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Mecha': {
        'short_name': 'm',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/m',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Cosplay & EGL': {
        'short_name': 'cgl',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/cgl',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Cute/Male': {
        'short_name': 'cm',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/cm',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Flash': {
        'short_name': 'f',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/f',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Transportation': {
        'short_name': 'n',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/n',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Otaku Culture': {
        'short_name': 'jp',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/jp',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Video Games': {
        'short_name': 'v',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/v',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Video Games Generals': {
        'short_name': 'vg',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/vg',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Pokémon': {
        'short_name': 'vp',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/vp',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Retro Games': {
        'short_name': 'vr',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/vr',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    # Interests
    'Comics & Cartoons': {
        'short_name': 'co',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/co',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Technology': {
        'short_name': 'g',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/g',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Television & Film': {
        'short_name': 'tv',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/tv',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Weapons': {
        'short_name': 'k',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/k',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Auto': {
        'short_name': 'o',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/o',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Animals & Nature': {
        'short_name': 'an',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/an',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Traditional Games': {
        'short_name': 'tg',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/tg',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Sports': {
        'short_name': 'sp',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/sp',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Alternative Sports': {
        'short_name': 'asp',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/asp',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Science & Math': {
        'short_name': 'sci',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/sci',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'History & Humanities': {
        'short_name': 'his',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/his',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'International': {
        'short_name': 'int',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/int',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Outdoors': {
        'short_name': 'out',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/out',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Toys': {
        'short_name': 'toy',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/toy',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    # Creative
    'Oekaki': {
        'short_name': 'i',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/i',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Papercraft & Origami': {
        'short_name': 'po',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/po',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Photography': {
        'short_name': 'p',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/p',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Food & Cooking': {
        'short_name': 'ck',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/ck',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Artwork/Critique': {
        'short_name': 'ic',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/ic',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Wallpapers/General': {
        'short_name': 'wg',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/wg',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Literature': {
        'short_name': 'lit',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/lit',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Music': {
        'short_name': 'mu',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/mu',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Fashion': {
        'short_name': 'fa',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/fa',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    '3DCG': {
        'short_name': '3',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/3',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Graphic Design': {
        'short_name': 'gd',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/gd',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Do-It-Yourself': {
        'short_name': 'diy',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/diy',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Worksafe GIF': {
        'short_name': 'wsg',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/wsg',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Quests': {
        'short_name': 'qst',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/qst',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    # Other
    'Business & Finance': {
        'short_name': 'biz',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/biz',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Travel': {
        'short_name': 'trv',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/trv',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Fitness': {
        'short_name': 'fit',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/fit',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Paranormal': {
        'short_name': 'x',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/x',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Advice': {
        'short_name': 'adv',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/adv',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'LGBT': {
        'short_name': 'lgbt',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/lgbt',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Pony': {
        'short_name': 'mlp',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/mlp',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Current News': {
        'short_name': 'news',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/news',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Worksafe Requests': {
        'short_name': 'wsr',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/wsr',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Very Important Posts': {
        'short_name': 'vip',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/vip',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    # Misc.
    'Random': {
        'short_name': 'b',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/b',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'ROBOT9001': {
        'short_name': 'r9k',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/r9k',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Politically Incorrect': {
        'short_name': 'pol',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/pol',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'International/Random': {
        'short_name': 'bant',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/bant',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Cams & Meetups': {
        'short_name': 'soc',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/soc',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Shit 4chan Says': {
        'short_name': 's4s',
        'category': 'not_adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/s4s',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    # Adult
    'Sexy Beautiful Women': {
        'short_name': 's',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/s',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': None,
                'arg_value': None,
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Hardcore': {
        'short_name': 'hc',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/hc',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Handsome Men': {
        'short_name': 'hm',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/hm',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Hentai': {
        'short_name': 'h',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/h',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Ecchi': {
        'short_name': 'e',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/e',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Yuri': {
        'short_name': 'u',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/u',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },

    'Hentai/Alternative': {
        'short_name': 'd',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/d',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },

    'Yaoi': {
        'short_name': 'y',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/y',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },

    'Torrents': {
        'short_name': 't',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/t',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },

    'High Resolution': {
        'short_name': 'hr',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/hr',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Adult GIF': {
        'short_name': 'gif',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/gif',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Adult Cartoons': {
        'short_name': 'aco',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/aco',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },
    'Adult Requests': {
        'short_name': 'r',
        'category': 'adult',
        'base_url': BASE_URL,
        'section_url': f'{BASE_URL}/r',
        'forbidden_words': [],
        'params': [
            {
                'arg_name': 'data-cmd',
                'arg_value': 'ok-disc',
            },
        ],
        'headers': {
            'user agent': 'Mozilla/5.0 (Windows NT 6.1)'},
    },

}
BAD_RESPONSE_CODES = [
    111,
    110,
    101,
    400,
    401,
    402,
    403,
    404,
    405,
    406,
    407,
    408,
    409,
    410,
    411,
    412,
    413,
    414,
    415,
    416,
    417,
    418,
    451,
    500,
    501,
    502,
    503,
    504,
    505,
    506,
    507,
    508,
    509,
    510,
    511,
]

GOOD_RESPONSE_CODES = [
    200,
    201,
    202,
    203,
    204,
    205,
    206,
    300,
    301,
    302,
    303,
    304,
    305,
    306,
    307,
    310,
    100,
]

RESPONSE_DICT = {
    '200': 'OK',
    '201': 'Created',
    '202': 'Accepted',
    '203': 'Non-Authoritative Information',
    '204': 'No content',
    '205': 'Reset Content',
    '206': 'Partial Content',
    '300': 'Multiple Choices',
    '301': 'Moved Permanently',
    '302': 'Found',
    '303': 'See Other',
    '304': 'Not Modified',
    '305': 'Use Proxy',
    '306': 'Switch Proxy',
    '307': 'Temporary Redirect',
    '310': 'Too many redirects',
    '100': 'Continue',
    '111': 'Connection refused',
    '110': 'Connection Timed Out',
    '101': 'Connection Timed Out',
    '400': 'Bad Request',
    '401': 'Unauthorized',
    '402': 'Payment Required',
    '403': 'Forbidden',
    '404': 'Not Found',
    '405': 'Method Not Allowed',
    '406': 'Not Acceptable',
    '407': 'Proxy Authentication Required',
    '408': 'Request Timeout',
    '409': 'Conflict',
    '410': 'Gone',
    '411': 'Length required',
    '412': 'Precondition Failed',
    '413': 'Request Entity Too Large',
    '414': 'Request-URI Too Long',
    '415': 'Unsupported Media Type',
    '416': 'Requested Range Not Satisfiable',
    '417': 'Expectation Failed',
    '418': 'I’m a teapot',
    '451': 'Unavailable For Legal Reasons',
    '500': 'Internal Server Error',
    '501': 'Not Implemented',
    '502': 'Bad Gateway',
    '503': 'Service Unavailable',
    '504': 'Gateway Timeout',
    '505': 'HTTP Version Not Supported',
    '506': 'Variant Also Negotiates',
    '507': 'Insufficient Storage (WebDAV)',
    '508': 'Loop Detected (WebDAV)',
    '509': 'Bandwidth Limit Exceeded',
    '510': 'Not Extended',
    '511': 'Network Authentication Required',
}

FORBIDDEN_WORDS = [
    'READ FIRST',
    'SCAT',
    'POOP',
    'SHEMALE',
    'THICK',
    'THICC',
    'REKT',
    'GAY',
    'LGBT',
    'CHASTITY',
    'CHASITY',
    'TRAP',
    'PEGGING',
    'FEMDOM',
    'TRANSSEXUAL',
    'TRANS',
    'WHALE',
    'BIG GIRL',
    'NAZI',
    'SHOOTING',
    'MOSQUE',
    'KILL',
    'TRANNY',
    'MIDGET',
    'GRANNY',
    'CHUBBY',
    'PREGNANCY',
    'PREGNANT',
    'GILF',
    'DIAPER',
    'FAT ',
    'HAIRY',


]
