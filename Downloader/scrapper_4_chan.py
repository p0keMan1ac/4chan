from bs4 import BeautifulSoup
import logging
import re
import urllib.request
import urllib.request
from Downloader.base_scrapper import BaseScrapper


class Scrapper4Chan(BaseScrapper):
    BASE_URL = 'https://boards.4channel.org'
    SECTION = {
        'Photography': {
            'short_name': 'p',
            'category': 'not_adult',
            'base_url': BASE_URL,
            'section_url': f'{BASE_URL}/p',
            'section_requests': [],
            'threads': [],
            'forbidden_words': [],
            'params': [
                {
                    'arg_name': None,
                    'arg_value': None,
                },
            ],
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'},
        },
        'Animals & Nature': {
            'short_name': 'an',
            'category': 'not_adult',
            'base_url': BASE_URL,
            'section_url': f'{BASE_URL}/an',
            'section_requests': [],
            'threads': [],
            'forbidden_words': [],
            'params': [
                {
                    'arg_name': None,
                    'arg_value': None,
                },
            ],
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'},
        },
        'Adult Gif': {
            'short_name': 'gif',
            'category': 'adult',
            'base_url': BASE_URL,
            'section_url': f'{BASE_URL}/gif',
            'section_requests': [],
            'threads': [],
            'forbidden_words': [
                'Gay',
                'Trans',
            ],
            'params': [
                {
                    'arg_name': 'data-cmd',
                    'arg_value': 'ok-disc',
                },
            ],
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1)'},
        },

    }
    THREAD = {}
    POST = {}
    MEDIA = {}
    # pages limit
    PAGES = [''] + [str(i) for i in range(2, 11)]

    def __init__(self, section='Photography'):
        try:
            self.section = self.SECTION[section]
        except Exception as error:
            logging.error(f"Could not find proper section, error: '{error}'.")
        # Property should be database, later as databases session create objects

    def find_sections_urls(self):
        # logging.info(f"Number of pages: {len(self.PAGES)}")
        self.section['section_requests'] = []
        for number_of_page in self.PAGES:
            url_to_page = f"{self.section['section_url']}/{number_of_page}"

            # logging.info(f"Checking url to sections page: {url_to_page}")
            if self.section['category'] == 'adult':
                arg_strings = []
                for param in self.section['params']:
                    if param["arg_name"] and param["arg_value"]:
                        arg_strings.append(f'{param["arg_name"]}={param["arg_value"]}')

                arg_string = '&'.join(arg_strings)
                url = f'{url_to_page}?{arg_string}'
            else:
                url = f'{url_to_page}'
            request = self.prepare_request_with_headers(url)
            # logging.info(f"request= {url}")
            (is_page_opened, page) = BaseScrapper.check_url(request)
            if is_page_opened:
                self.section['section_requests'].append(request)

    def find_thread_urls(self):
        pattern = f'/{self.section["short_name"]}/(thread)/(\d*)[/#]*(\S*)'
        all_a_elements_from_link_of_section_page = []
        for request_of_section_page in self.section['section_requests']:
            BaseScrapper.find_all_specific_elements_into_array(request_of_section_page, 'a',
                                                    all_a_elements_from_link_of_section_page)
        all_links = []
        BaseScrapper.find_all_links_from_list(all_a_elements_from_link_of_section_page,
                                              'href', all_links)
        for link in all_links:
            regex_check = re.match(pattern, link)
            if regex_check:
                thread_word = regex_check.groups()[0]
                thread_id = regex_check.groups()[1]
                link_to_thread = str(f'{self.section["section_url"]}/{thread_word}/{thread_id}')
                # logging.info(f"Link to thread: {link_to_thread}")
                if thread_id not in self.THREAD.keys():
                    request = self.prepare_request_with_headers(link_to_thread)
                    self.THREAD[thread_id] = {
                        'link_to_thread': link_to_thread,
                        'request': request,
                        'subject': None,
                        'op_posts': [],
                        'reply_posts': [],
                        'title': None,
                    }
                    self.section['threads'].append(self.THREAD[thread_id])
        logging.info(f"Found all links from pages of given section.")
        for thread in self.section['threads'][-5:]:
            logging.info(f"Link to thread: {thread['link_to_thread']}")

    def find_posts_from_thread(self):
        thread_number = 1
        for thread_id in self.THREAD.keys():
            if int(thread_number) % 10 == 0:
                logging.info(f"Checking {thread_number} thread")
            thread = self.THREAD[thread_id]
            # Open link
            page = urllib.request.urlopen(thread['request'])
            soup = BeautifulSoup(page, features="html.parser")

            # Set title for thread
            thread['title'] = soup.title.string

            self.get_media_and_posts(
                soup,
                thread,
                type_of_element='div',
                class_of_element='postContainer opContainer',
                class_of_inner_element='post op',
                type_of_inner_element='a',
                is_subject_to_be_set=True,
                is_op=True

            )

            self.get_media_and_posts(
                soup,
                thread,
                type_of_element='div',
                class_of_element='postContainer replyContainer',
                class_of_inner_element='post reply',
                type_of_inner_element='a',
                is_subject_to_be_set=False,
                is_op=False

            )

            thread_number = thread_number + 1

    def prepare_request_with_headers(self, url):
        arg_strings = []
        for param in self.section['params']:
            if param["arg_name"] and param["arg_value"]:
                arg_strings.append(f'{param["arg_name"]}={param["arg_value"]}')

        arg_string = '&'.join(arg_strings)
        link = f'{url}?{arg_string}'
        return urllib.request.Request(url=link, headers=self.section['headers'])

    def get_media_and_posts(self,
                            soup,
                            thread,
                            type_of_element='div',
                            class_of_element='postContainer replyContainer',
                            class_of_inner_element='post reply',
                            type_of_inner_element='a',
                            is_subject_to_be_set=False,
                            is_op=False
                            ):
        post_number = 0
        found_posts = 0
        for post in soup.find_all(type_of_element, class_=class_of_element):
            post_number = post_number + 1
            post_id = int(post.find(type_of_element, class_=class_of_inner_element).get('id').replace('p', ''))
            # Set threads subject.
            if is_subject_to_be_set:
                if not thread['subject']:
                    thread['subject'] = {post.find('span', class_='subject').string}
            post_text = post.find('blockquote').get_text()
            self.POST[post_id] = {
                'thread': thread,
                'text': post_text,
            }
            for link in post.find_all(type_of_inner_element):
                link_to_image = link.get('href')
                media_pattern = f'//i.4cdn.org/{self.section["short_name"]}/(\S+)[.]+(\S+)'
                second_media_pattern = f'//is2.4chan.org/{self.section["short_name"]}/(\S+)[.]+(\S+)'
                check_if_link_to_media = re.match(media_pattern, link_to_image) or re.match(second_media_pattern, link_to_image)
                if check_if_link_to_media:
                    found_posts = found_posts + 1
                    full_link_to_image = f'https:{link_to_image}'
                    file_name = check_if_link_to_media.groups()[0]
                    file_extension = check_if_link_to_media.groups()[1]
                    full_file_name = f'{file_name}.{file_extension}'
                    # logging.info(f"Link to media: {full_link_to_image}")
                    if full_link_to_image not in self.MEDIA.keys():
                        self.MEDIA[full_link_to_image] = {
                            'file_link': full_link_to_image,
                            'is_downloaded': False,
                            'is_online': True,
                            'file_extension': file_extension,
                            'file_name': full_file_name,
                            'post': self.POST[post_id]
                        }

            if is_op:
                thread['op_posts'].append(self.POST[post_id])
            else:
                thread['reply_posts'].append(self.POST[post_id])

    def prepare_links(self):
        pass

    def download(self):
        pass

    def map_objects(self):
        pass
