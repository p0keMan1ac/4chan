import logging
import os
from Downloader.base_scrapper import BaseScrapper


class Scrapper4Chan(BaseScrapper):
    def __init__(self, database):
        self.__database = database
        self.pages = [''] + [str(i) for i in range(2, 11)]
        self.__section_requests = []
        self.__section = None
        self.__headers = None
        self.__session = self.__database.start_new_session()

    def get_section(self):
        return self.__section

    def set_section(self, short_name):
        self.__section = self.__database.get_section_by_short_name(short_name)

    def set_headers(self):
        self.__headers = {
            'User-Agent': self.__section.user_agent.value}

    def get_headers(self):
        return self.__headers

    def set_section_requests(self):
        good_response_codes = self.__database.get_good_response_codes()
        for page in self.pages:
            url = self.__database.build_section_link_with_params(section=self.__section, page=page)
            # logging.info(f"Checking section url: [{url}].")
            request = BaseScrapper.create_request(link=url, headers=self.get_headers())
            (is_available, page) = BaseScrapper.check_request(request, good_response_codes)
            if is_available:
                # logging.info(f"Appended request for section url[{url}].")
                self.__section_requests.append(request)

    def get_section_requests(self):
        return self.__section_requests

    def get_section_threads(self):
        return self.get_section().threads

    def get_threads_to_check_for_new_posts(self):
        return self.__database.get_threads_to_check_for_new_posts(self.get_section())

    def find_and_create_threads_from_section_requests(self):
        pattern = f'thread/(\d*)[/#]*(\S*)'
        threads_id = []
        request_id = 1
        for request in self.get_section_requests():
            logging.info(f"Checking {request_id} request page...")
            BaseScrapper.find_threads_id_from_request_into_array(request=request, pattern=pattern,
                                                                 threads_id=threads_id)
            request_id += 1
        for thread_id in threads_id:
            self.__database.create_thread_record(thread_id, section=self.get_section())
        return threads_id

    def find_and_create_posts_and_media_from_thread(self, thread):
        forbidden_words = self.__database.get_forbidden_words_for_section(self.get_section())
        self.set_headers()
        post_dictionary, media_dictionary = BaseScrapper.find_posts_and_media_without_forbidden_from_thread(
            thread=thread,
            headers=self.get_headers(),
            forbidden_words=forbidden_words,
            good_response_codes = self.__database.get_good_response_codes())

        self.__database.get_session().commit()
        logging.info(f"HANDLING THREAD: [id={thread.id}, title={thread.title}].")
        self.__database.create_post_record_from_dictionary(post_dictionary)
        self.__database.get_session().commit()
        self.__database.create_media_record_from_dictionary(media_dictionary)
        thread.is_to_check = False
        self.__database.get_session().commit()

    def prepare_links(self):
        pass

    def download(self):
        medias = self.__database.get_medias_to_download()
        for media in medias:
            if media.file_extension not in ['gif']:
                if not media.is_downloaded:
                    media_directory = os.path.join(os.getcwd(), 'Media')
                    logging.info(
                        f"Downloading file from  Media:"
                        f"[file_name={media.file_name}, link={media.link}] "
                        f"into directory={media_directory}...")

                    if not os.path.exists(media_directory):
                        os.mkdir(media_directory)
                    file_path = os.path.join(media_directory, media.file_name)
                    is_online, is_downloaded = BaseScrapper.download_media(media.link, file_path)
                    # is_online, is_downloaded = True, True
                    media.is_downloaded = is_downloaded
                    media.is_online = is_online
            else:
                media.is_downloaded = False
                media.is_online = False
        self.__database.get_session().commit()
