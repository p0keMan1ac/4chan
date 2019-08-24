from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import logging
import socket
import re
import urllib
import urllib.request

from Downloader.request_variables import GOOD_RESPONSE_CODES, BAD_RESPONSE_CODES, RESPONSE_DICT

socket.setdefaulttimeout(60)


class BaseScrapper(ABC):
    @abstractmethod
    def download(self):
        pass

    @abstractmethod
    def prepare_links(self):
        pass

    # To be deleted!
    @staticmethod
    def check_url(request):
        try:
            page = urllib.request.urlopen(request)
            response_code = page.getcode()
            if response_code in GOOD_RESPONSE_CODES:
                return True, page
            else:
                return False, None
        except Exception as error:
            logging.info(f"Could not open request[link={request}]... ")
            return False, None

    @staticmethod
    def check_request(request, good_response_codes):
        try:

            page = urllib.request.urlopen(request)
            response_code = page.getcode()

            if response_code in good_response_codes:
                return True, page
            else:
                return False, None
        except Exception as error:
            logging.info(f"Could not open request[request={request}]. ERROR: [{repr(error)}].")
            return False, None

    @staticmethod
    def create_request(link, headers):
        return urllib.request.Request(url=link, headers=headers)

    @staticmethod
    def find_all_specific_elements_into_array(request, find_element, array):
        try:
            is_page_available, page = BaseScrapper.check_url(request)
            soup = BeautifulSoup(page, 'html.parser')
            for element in soup.find_all(find_element):
                array.append(element)
        except Exception as error:
            logging.error(f"Given request: {request} could not be reached.\n\t\t[ERROR: {error}].")

    @staticmethod
    def find_all_specific_elements(request, find_element):
        all_elements = []
        try:
            is_page_available, page = BaseScrapper.check_url(request)
            soup = BeautifulSoup(page, 'html.parser')
            for element in soup.find_all(find_element):
                all_elements.append(element)
        except Exception as error:
            logging.error(f"Given request: {request} could not be reached.\n\t\t[ERROR: {error}].")
        return all_elements

    @staticmethod
    def find_threads_id_from_request_into_array(request, pattern, threads_id):
        # logging.info("Finding all specific elements...")
        all_a_elements_from_link_of_section_page = \
            BaseScrapper.find_all_specific_elements(request=request,
                                                    find_element='a')

        all_links = []

        BaseScrapper.find_all_links_from_list(all_a_elements_from_link_of_section_page, 'href', all_links)

        for link in all_links:
            regex_check = re.match(pattern, link)
            if regex_check:

                thread_id = regex_check.groups()[0]
                if thread_id not in threads_id:
                    threads_id.append(thread_id)

    @staticmethod
    def find_all_links_from_list(elements, element_type, all_links):
        for element in elements:
            all_links.append(element.get(element_type))

    @staticmethod
    def find_posts_and_media_from_thread(thread, headers):

        request = BaseScrapper.create_request(link=thread.link, headers=headers)
        page = urllib.request.urlopen(request)
        soup = BeautifulSoup(page, features="html.parser")
        thread.title = soup.title.string

        (OP_POST, OP_MEDIA) = BaseScrapper.get_media_and_posts(
            soup,
            thread,
            type_of_element='div',
            class_of_element='postContainer opContainer',
            class_of_inner_element='post op',
            type_of_inner_element='a',
            is_subject_to_be_set=True,
            is_op=True

        )

        (REPLY_POST, REPLY_MEDIA) = BaseScrapper.get_media_and_posts(
            soup,
            thread,
            type_of_element='div',
            class_of_element='postContainer replyContainer',
            class_of_inner_element='post reply',
            type_of_inner_element='a',
            is_subject_to_be_set=False,
            is_op=False

        )

        POST = {**OP_POST, **REPLY_POST}
        MEDIA = {**OP_MEDIA, **REPLY_MEDIA}

        return POST, MEDIA

    @staticmethod
    def find_posts_and_media_without_forbidden_from_thread(thread, headers, forbidden_words, good_response_codes):
        soup = None
        request = BaseScrapper.create_request(link=thread.link, headers=headers)
        logging.warning(f"Checking thread... Thread[title = {thread.title}, link={thread.link}].")
        logging.info(
            f"Thread: [Forbidden={thread.is_forbidden}, IsOnline={thread.is_online}, IsChecked={thread.is_to_check}]")
        if thread.is_online:
            try:
                is_online, page = BaseScrapper.check_request(request, good_response_codes)
                if page:
                    soup = BeautifulSoup(page, features="html.parser")
                    thread.title = str(soup.title.string).upper()
                else:
                    thread.is_online = False
                    thread.is_to_check = False
            except Exception as error:
                error_msg = repr(error)
                logging.warning(f"Could not open url of thread. Thread is probably offline."
                                f"Thread = [id={thread.id}, link={thread.link}]."
                                f"ERROR: {error_msg}")
                thread.is_online = False
                return {}, {}
        else:
            logging.warning(f"Thread is offline. Thread[title = {thread.title}, link={thread.link}].")
            return {}, {}

        # Forbidden handle.
        for forbidden_word in forbidden_words:
            if thread.title:
                if thread.title.find(forbidden_word) > (-1):
                    thread.is_forbidden = True
        if thread.is_forbidden:
            logging.warning(f"Thread has forbidden words. Thread:[title = {thread.title}, link={thread.link}].")
            return {}, {}
        if soup:
            (OP_POST, OP_MEDIA) = BaseScrapper.get_media_and_posts(
                soup,
                thread,
                type_of_element='div',
                class_of_element='postContainer opContainer',
                class_of_inner_element='post op',
                type_of_inner_element='a',
                is_subject_to_be_set=True,
                is_op=True

            )

            (REPLY_POST, REPLY_MEDIA) = BaseScrapper.get_media_and_posts(
                soup,
                thread,
                type_of_element='div',
                class_of_element='postContainer replyContainer',
                class_of_inner_element='post reply',
                type_of_inner_element='a',
                is_subject_to_be_set=False,
                is_op=False

            )
            thread.is_to_check = False
            POST = {**OP_POST, **REPLY_POST}
            MEDIA = {**OP_MEDIA, **REPLY_MEDIA}
            logging.info(f"Thread is checked. Thread[title = {thread.title}, link={thread.link}].")
            return POST, MEDIA
        else:
            return {}, {}

    @staticmethod
    def get_media_and_posts(soup,
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
        POST = {}
        MEDIA = {}
        for post in soup.find_all(type_of_element, class_=class_of_element):
            post_number = post_number + 1
            # Set posts_id
            post_id = int(post.find(type_of_element, class_=class_of_inner_element).get('id').replace('p', ''))
            # Set threads subject.
            if is_subject_to_be_set:
                thread.subject = post.find('span', class_='subject').string
            post_text = post.find('blockquote').get_text()
            POST[post_id] = {
                '4chan_id': post_id,
                'thread': thread,
                'text': post_text,
                'is_op': is_op
            }
            for link in post.find_all(type_of_inner_element):
                link_to_image = link.get('href')
                media_pattern = f'//i.4cdn.org/{thread.section.short_name}/(\S+)[.]+(\S+)'
                second_media_pattern = f'//is2.4chan.org/{thread.section.short_name}/(\S+)[.]+(\S+)'
                check_if_link_to_media = re.match(media_pattern, link_to_image) or re.match(second_media_pattern,
                                                                                            link_to_image)

                if check_if_link_to_media:
                    found_posts = found_posts + 1
                    full_link_to_image = f'https:{link_to_image}'
                    file_name = check_if_link_to_media.groups()[0]
                    file_extension = check_if_link_to_media.groups()[1]
                    full_file_name = f'{file_name}.{file_extension}'
                    # logging.info(f"Link to media: {full_link_to_image}")
                    if full_link_to_image not in MEDIA.keys():
                        MEDIA[full_link_to_image] = {
                            'link': full_link_to_image,
                            'file_extension': file_extension,
                            'file_name': full_file_name,
                            'post': POST[post_id]
                        }
        return POST, MEDIA

    @staticmethod
    def download_media(link, file_path):
        try:
            urllib.request.urlretrieve(link, file_path)
            is_online = True
            is_downloaded = True
        except Exception as error:
            error_msg = repr(error)
            logging.warning(f"Could not open url of media. Media is probably offline."
                            f"Media link = {link}]. ERROR: {error_msg}")
            is_online = False
            is_downloaded = False
        return is_online, is_downloaded
