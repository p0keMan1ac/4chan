from abc import ABCMeta, abstractmethod
import logging
from Downloader.database_scrapper import Scrapper4Chan

# Global variables.
separator = "*" * 80


class Executor(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, short_names):
        pass

    def __init__(self, database_handler):
        self.__scrappers = []
        self.database_handler = database_handler
        self.database_handler.create_session()
        self.database_handler.build()
        self.tasks = []

    def set_section_and_add_new_scrapper(self, scrapper, short_name_of_section):
        scrapper.set_section(short_name_of_section)
        self.add_new_scrapper(scrapper)

    def add_new_scrapper(self, scrapper):
        self.__scrappers.append(scrapper)

    def add_new_scrappers(self, scrappers):
        for scrapper in scrappers:
            self.__scrappers.append(scrapper)

    def find_threads_all(self):
        logging.info("Finding all threads...")
        for scrapper in self.__scrappers:
            logging.info(
                f"Finding threads for scrapper: "
                f"[Section={scrapper.get_section().name}, link={scrapper.get_section().section_url}].")
            scrapper.set_headers()
            scrapper.set_section_requests()
            scrapper.find_and_create_threads_from_section_requests()
        logging.info("All threads found.")

    def find_and_create_posts_and_medias_all(self):
        logging.info("Finding all posts...")
        for scrapper in self.__scrappers:
            for thread in scrapper.get_threads_to_check_for_new_posts():
                logging.info(
                    f"Finding posts for "
                    f"Thread: [4chan_id = {thread.thread_4chan_id}, Link={thread.link}], "
                    f"Section:[{scrapper.get_section().name}].")

                scrapper.find_and_create_posts_and_media_from_thread(thread)
        logging.info("All posts found.")

    def download_all(self):
        logging.info("Downloading medias...")
        for scrapper in self.__scrappers:
            scrapper.download()
        logging.info("All medias downloaded...")


class CommonExecutor(Executor):
    def execute(self, short_names):
        for short_name in short_names:
            self.set_section_and_add_new_scrapper(Scrapper4Chan(self.database_handler),
                                                  short_name)
        self.find_threads_all()
        self.find_and_create_posts_and_medias_all()
        self.download_all()


class DownloadExecutor(Executor):
    def execute(self, short_names):
        for short_name in short_names:
            self.set_section_and_add_new_scrapper(Scrapper4Chan(self.database_handler),
                                                  short_name)
        self.download_all()


class FindNewThreadsExecutor(Executor):
    def execute(self, short_names):
        for short_name in short_names:
            self.set_section_and_add_new_scrapper(Scrapper4Chan(self.database_handler),
                                                  short_name)
        self.find_threads_all()


class FindNewPostsAndMediasExecutor(Executor):
    def execute(self, short_names):
        for short_name in short_names:
            self.set_section_and_add_new_scrapper(Scrapper4Chan(self.database_handler),
                                                  short_name)
        self.find_and_create_posts_and_medias_all()


## Executor defined.
class ExecutorFactory(metaclass=ABCMeta):
    def do_job(self, object_type, database_handler, short_names):
        eval(object_type)(database_handler).execute(short_names)
