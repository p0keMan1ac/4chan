import logging
import os
import sys
import unittest
import urllib
import urllib.request
import uuid

# Set root path.
home_dir = '/home/msm/PycharmProjects/4chanWebScrapper'
sys.path.append(home_dir)

# Import local modules.
from Database.database_wrapper import DatabaseEngine
from Database.database_handler import *
from Downloader.database_scrapper import Scrapper4Chan
from Downloader.base_scrapper import BaseScrapper

separator = '*' * 80


class ExperimentalDatabaseBuilderTest(unittest.TestCase):
    def setUp(self):
        logging.info(separator)
        self.db_directory = '/home/msm/PycharmProjects/4chanWebScrapper/Database/Test'
        self.db_filename = f'test_all.sqlite'
        self.db_path = f'{self.db_directory}/{self.db_filename}'
        self.database_engine = DatabaseEngine(database_type='sqlite',
                                              path_to_database_file=self.db_path)
        self.database_engine.set_engine()
        self.database = DatabaseHandler(self.database_engine.get_engine())
        self.database.create_session()
        self.database.build()
        self.database.build_all_dictionaries()
        self.scrapper = Scrapper4Chan(self.database)

    def tearDown(self):
        self.scrapper = None
        self.database = None
        self.database_engine = None


class DatabaseBuilderTest(unittest.TestCase):
    def setUp(self):
        logging.info(separator)
        self.db_directory = '/home/msm/PycharmProjects/4chanWebScrapper/Database/Test'
        self.db_filename = f'{str(uuid.uuid4())}.sqlite'
        self.db_path = f'{self.db_directory}/{self.db_filename}'
        self.database_engine = DatabaseEngine(database_type='sqlite',
                                              path_to_database_file=self.db_path)
        self.database_engine.set_engine()
        self.database = DatabaseHandler(self.database_engine.get_engine())
        self.database.create_session()
        self.database.build()
        self.database.build_all_dictionaries()
        self.scrapper = Scrapper4Chan(self.database)

    def tearDown(self):
        self.scrapper = None
        self.database = None
        self.database_engine = None
        os.remove(self.db_path)

    def test_scrapper_set_section(self):
        logging.info("Test setting section.")
        self.scrapper.set_section('gif')
        self.scrapper.set_headers()
        section = self.scrapper.get_section()
        self.assertEqual(section.name, 'Adult Gif', f"Wrongly set section [section_name={section.name}].")

    def test_scrapper_set_section_requests(self):
        logging.info("Test setting section requests.")
        self.scrapper.set_section('gif')
        self.scrapper.set_headers()
        self.scrapper.set_section_requests()
        for section_request in self.scrapper.get_section_requests():
            self.assertIsInstance(section_request, urllib.request.Request,
                                  f"Not every instance of section requests is Request [request={section_request}].")

    def test_find_threads_urls(self):
        logging.info("Test find threads section.")
        self.scrapper.set_section('gif')
        self.scrapper.set_headers()
        self.scrapper.set_section_requests()
        threads_id = self.scrapper.find_and_create_threads_from_section_requests()
        logging.info(f"Found {len(threads_id)} links of thread.")
        threads = self.database.get_all_thread_links_of_section(self.scrapper.get_section())
        self.assertTrue(threads_id, "Could not find any thread url.")
        self.assertEqual(len(threads_id), len(threads), "Not every thread link exists into database.")
        pattern = f'{self.scrapper.get_section().section_url}/(thread)/(\d*)[/#]*(\S*)'
        for thread in threads:
            self.assertRegex(thread.link, pattern, f"Not every thread link matches regex [thread link={thread.link}].")

    def test_find_posts_from_thread(self):
        logging.info("Test finding posts from thread.")
        self.scrapper.set_section('gif')
        self.scrapper.set_headers()
        self.scrapper.set_section_requests()
        self.scrapper.find_and_create_threads_from_section_requests()
        threads = self.scrapper.get_section().threads
        thread = threads[1]
        self.scrapper.find_and_create_posts_and_media_from_thread(thread)
        all_posts = self.database.query_all_from_table_class(Post)
        self.assertTrue(len(all_posts), "There is no posts for given thread.")
        for post in all_posts:
            self.assertIsNotNone(post.thread, "Not every post is related to thread.")

    def test_find_posts_and_media_from_thread(self):
        logging.info("Test finding posts and media from thread..")
        self.scrapper.set_section('gif')
        self.scrapper.set_headers()
        self.scrapper.set_section_requests()
        self.scrapper.find_and_create_threads_from_section_requests()
        threads = self.scrapper.get_section().threads

        thread = threads[2]
        self.scrapper.find_and_create_posts_and_media_from_thread(thread)
        all_posts = self.database.query_all_from_table_class(Post)
        self.assertTrue(len(all_posts), "There is no posts for given thread.")
        self.assertTrue(len(thread.posts), f"There is no posts related to thread. [thread={thread}]")
        self.assertTrue(thread.title, f"Title is not set for this thread[{thread}].")


class BaseScrapperTest(unittest.TestCase):
    def setUp(self):
        logging.info(separator)
        self.db_directory = '/home/msm/PycharmProjects/4chanWebScrapper/Database/Test'
        self.db_filename = f'{str(uuid.uuid4())}.sqlite'
        self.db_path = f'{self.db_directory}/{self.db_filename}'
        self.database_engine = DatabaseEngine(database_type='sqlite',
                                              path_to_database_file=self.db_path)
        self.database_engine.set_engine()
        self.database = DatabaseHandler(self.database_engine.get_engine())
        self.database.create_session()
        self.database.build()
        self.database.build_all_dictionaries()
        self.scrapper = Scrapper4Chan(self.database)

    def tearDown(self):
        self.scrapper = None
        self.database = None
        self.database_engine = None
        os.remove(self.db_path)

    def test_base_find_posts_and_media_from_thread(self):
        logging.info("Test BaseScrapper.find_posts_and_media_from_thread.")
        # thread, headers)
        self.scrapper.set_section('gif')
        self.scrapper.set_headers()
        self.scrapper.set_section_requests()
        self.scrapper.find_and_create_threads_from_section_requests()
        thread = self.database.query_all_from_table_class(Thread)[1]
        logging.info(f"Checking thread: [{thread}].")
        POSTS, MEDIA = BaseScrapper.find_posts_and_media_from_thread(thread,
                                                                     self.scrapper.get_headers())
        self.assertIsNotNone(thread.title, "Could not set title of thread...")
        self.assertTrue(POSTS.keys(), "Could not find any post...")
        self.assertTrue((MEDIA.keys(), "Could not find any media..."))

    def test_find_posts_and_media_from_thread(self):
        logging.info("Test finding posts and media from thread..")
        self.scrapper.set_section('gif')
        self.scrapper.set_headers()
        self.scrapper.set_section_requests()
        self.scrapper.find_and_create_threads_from_section_requests()
        forbidden_words = self.database.get_forbidden_words_for_section(self.scrapper.get_section())
        threads = self.scrapper.get_section().threads

        for thread in threads:
            self.scrapper.find_and_create_posts_and_media_from_thread(thread)
            self.assertTrue(thread.title, f"Title is not set for this thread[{thread}].")
            for forbidden_word in forbidden_words:
                if thread.title.find(forbidden_word) > (-1):
                    self.assertTrue(thread.is_forbidden,
                                    f"Thread is not forbidden [thread_id={thread.id}, thread_title={thread.title}, founded forbidden word={forbidden_word}].")
            self.assertEqual(thread.title, thread.title.upper(),
                             f"Thread in database is not uppercased [Thread_id={thread.id}, Thread_title={thread.title}].")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
