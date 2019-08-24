import logging
import os
import re
import sys
import unittest
import urllib.request

home_dir = '/home/msm/PycharmProjects/4chanWebScrapper'
sys.path.append(home_dir)
separator = '*' * 80
from Downloader.scrapper_4_chan import Scrapper4Chan
from Downloader.base_scrapper import BaseScrapper


class ScrapperTest(unittest.TestCase):
    def setUp(self):
        self.section_name = 'Adult Gif'
        logging.info(f"Set up params: <section_name={self.section_name}>")
        self.empty_page_number = ''
        self.page_number = '2'
        self.scrapper = Scrapper4Chan(section=self.section_name)
        self.scrapper.PAGES = ['', 2, 3]

    def tearDown(self):
        del self.scrapper

    def test_init(self):
        logging.info(separator)
        logging.info("Testing if you can create instance with given section_name")
        self.assertIsInstance(self.scrapper, Scrapper4Chan,
                              f'created object: {self.scrapper} is not instance of class: {Scrapper4Chan}')
        logging.info("Test is OK.")

    def test_prepare_request_with_empty_page_number_with_headers_without_parameters(self):
        logging.info(separator)
        logging.info(
            "Testing if you can create instance with given section_name without page number and request arguments...")
        url_to_page = f"{self.scrapper.section['section_url']}/{self.empty_page_number}"
        request = self.scrapper.prepare_request_with_headers(url_to_page)
        self.assertIsInstance(request, urllib.request.Request,
                              f"[Request:{request} is not instance of class: {urllib.request.Request}")
        logging.info("Test is OK.")

    def test_prepare_request_with_page_number_with_headers_without_parameters(self):
        logging.info(separator)
        logging.info(
            "Testing if you can create instance with given section_name with page number and request arguments...")
        url_to_page = f"{self.scrapper.section['section_url']}/{self.page_number}"
        request = self.scrapper.prepare_request_with_headers(url_to_page)
        self.assertIsInstance(request, urllib.request.Request,
                              f"[Request:{request} is not instance of class: {urllib.request.Request}")
        logging.info("Test is OK.")

    def test_check_url_method(self):
        logging.info(separator)
        logging.info("Testing check_url_method for request...")

        url_to_page = f"{self.scrapper.section['section_url']}/{self.page_number}"
        request = self.scrapper.prepare_request_with_headers(url_to_page)
        logging.info("Checking method 'BaseScrapper.check_url'...")
        response_code, page = BaseScrapper.check_url(request)
        self.assertTrue(response_code,
                        "Response code of request is not in Good response codes.")
        logging.info("Test is OK.")

    def test_find_sections_urls_quantity(self):
        logging.info(separator)
        logging.info(f"Testing if you can find {len(self.scrapper.PAGES)} section urls")

        self.scrapper.find_sections_urls()
        self.assertEqual(len(self.scrapper.PAGES), len(self.scrapper.section['section_requests']),
                         f'There is not found {len(self.scrapper.PAGES)} pages of this section')
        logging.info("Test is OK.")

    def test_find_threads_urls(self):
        logging.info(separator)
        logging.info("Testing if you all section urls match regex")
        self.scrapper.find_sections_urls()
        self.scrapper.find_thread_urls()
        logging.info(f"Threads found: {len(self.scrapper.section['threads'])}")
        self.assertGreater(len(self.scrapper.section['threads']), 0, 'There is not any thread found in this section')
        pattern = f"{self.scrapper.section['section_url']}/thread/\S+"
        for thread in self.scrapper.section['threads']:
            regex_of_link = re.match(pattern, thread['link_to_thread'])
            self.assertTrue(regex_of_link, f"Link of thread does not match regex.[Link: {thread['link_to_thread']}")
            self.assertIsInstance(thread['request'], urllib.request.Request,
                                  f"Threads request is not Request type [Request={thread['request']}, "
                                  f"Link={thread['link_to_thread']}")
        logging.info("Each request is Request type")
        logging.info("Test is OK.")

    def test_find_posts_from_thread(self):
        logging.info(separator)
        logging.info("Testing if there are posts for each thread...")
        self.scrapper.find_sections_urls()
        self.scrapper.find_thread_urls()
        logging.info(f"Found: {len(self.scrapper.section['threads'])} threads.")
        self.scrapper.find_posts_from_thread()
        self.assertGreater(len(self.scrapper.POST.keys()), 0, 'There is not any post found in threads.')
        for thread_id in self.scrapper.THREAD.keys():
            thread = self.scrapper.THREAD[thread_id]
            self.assertIsNotNone(thread['subject'],
                                 f"Not every thread's subject is set ["
                                 f"Link to thread: {thread['link_to_thread']}, "
                                 f"Subject: {thread['subject']}]")
            self.assertIsNotNone(thread['title'],
                                 f"Not every thread's topic is set ["
                                 f"Link to thread: {thread['link_to_thread']}, "
                                 f"Title: {thread['title']}]")
        logging.info(
            f"Found {len(self.scrapper.MEDIA.keys())} Media to download from {len(self.scrapper.POST.keys())} posts.")
        for media_link in self.scrapper.MEDIA.keys():
            link = self.scrapper.MEDIA[media_link]['file_link']
            pattern = f"https://i.4cdn.org/gif/\S+[.]+\S+"
            self.assertRegex(link, pattern, "Link to media does not match pattern")
        logging.info("Test is OK.")

    def test_base_download_link(self):
        link = 'http://i.4cdn.org/gif/1553875326730.webm'
        filename = '1553782270420.webm'
        media_directory = os.path.join(os.getcwd(), 'Test')
        if not os.path.exists(media_directory):
            os.mkdir(media_directory)
        file_path = os.path.join(media_directory, filename)
        logging.info(f"FILE PATH: {file_path}")
        is_d, is_o = BaseScrapper.download_media(link, file_path)
        self.assertTrue(os.path.exists(file_path), f"Media is not downloaded. [File path={file_path}].")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
