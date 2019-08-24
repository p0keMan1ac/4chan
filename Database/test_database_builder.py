import logging
import os
import sys
import unittest
import uuid

# Set root path.
home_dir = '/home/msm/PycharmProjects/4chanWebScrapper'
sys.path.append(home_dir)

# Import local modules.
from Database.database_wrapper import DatabaseEngine
from Database.database_handler import *

separator = '*' * 80


class DatabaseBuilderTest(unittest.TestCase):
    def setUp(self):
        self.db_directory = '/home/msm/PycharmProjects/4chanWebScrapper/Database/Test'
        self.db_filename = f'{str(uuid.uuid4())}.sqlite'
        self.db_path = f'{self.db_directory}/{self.db_filename}'
        self.database_engine = DatabaseEngine(database_type='sqlite',
                                              path_to_database_file=self.db_path)
        self.database_engine.set_engine()
        self.database = DatabaseHandler(self.database_engine.get_engine())

    def tearDown(self):
        self.database = None
        os.remove(self.db_path)

    def test_list_created_tables(self):
        self.database.create_session()
        self.database.build()
        tables = [
            'response_code', 'system', 'browser', 'user_agent', 'param', 'section', 'section_x_param',
            'forbidden_word', 'section_x_forbidden_word', 'thread', 'post', 'media'
        ]
        for table in tables:
            self.assertIn(table, self.database_engine.get_all_tables(),
                          f"Not every table is created in database [table={table}].")

        self.assertEqual(len(tables), len(self.database_engine.get_all_tables()),
                         f"Quantity of created tables is not equal to {len(tables)}.")

    def test_check_response_code_dictionary_builder(self):
        self.database.create_session()
        self.database.build()

        self.database.build_response_code_dictionary()
        self.database.build_response_code_dictionary()
        response_codes_from_database = self.database.query_all_from_table_class(ResponseCode)
        self.assertEqual(len(response_codes_from_database), len(RESPONSE_DICT.keys()),
                         "Created response code records quantity is not equal to quantity of used dictionary.")
        ok_code = 200
        ok_response_code = self.database.get_session().query(ResponseCode).filter(ResponseCode.code == ok_code).first()
        self.assertTrue(ok_response_code.is_ok, f"Status of response code: {ok_code} should be True.")

    def test_system_dictionary_builder(self):
        self.database.create_session()
        self.database.build()
        self.database.build_system_dictionary()
        self.database.build_system_dictionary()
        systems = ['Windows', 'Mac OS', 'Linux', 'other']
        systems_from_database = self.database.query_all_from_table_class(System)
        self.assertEqual(len(systems_from_database), len(systems),
                         "Created systems records quantity is not equal to quantity of used dictionary.")
        for system in systems_from_database:
            self.assertIn(system.name, systems,
                          f"Not every system database exists in dictionary [system={system.name}].")

    def test_browser_dictionary_builder(self):
        self.database.create_session()
        self.database.build()
        self.database.build_browser_dictionary()
        self.database.build_browser_dictionary()
        browsers = ['Chrome', 'Firefox', 'Mozilla']
        browsers_from_database = self.database.query_all_from_table_class(Browser)
        self.assertEqual(len(browsers_from_database), len(browsers),
                         "Created browsers quantity is not equal to quantity of used dictionary.")
        for browser in browsers_from_database:
            self.assertIn(browser.name, browsers,
                          f"Not every browser database exists in dictionary [browser={browser.name}].")

    def test_user_agent_dictionary_builder(self):
        self.database.create_session()
        self.database.build()
        self.database.build_browser_dictionary()
        self.database.build_system_dictionary()
        self.database.build_user_agent_dictionary()
        self.database.build_user_agent_dictionary()
        user_agents_from_database = self.database.query_all_from_table_class(UserAgent)
        self.assertEqual(len(user_agents_from_database), len(USER_AGENT_DICT.keys()),
                         "Created user_agent quantity is not equal to quantity of used dictionary.")
        for user_agent in USER_AGENT_DICT.keys():
            self.assertIsNotNone(
                self.database.get_session().query(UserAgent).filter(UserAgent.value == user_agent).first(),
                f"Not every record from dictionary exists in database: [user_agent={user_agent}].")

    def test_param_dictionary_builder(self):
        self.database.create_session()
        self.database.build()
        self.database.build_param_dictionary()
        self.database.build_param_dictionary()
        params_from_database = self.database.query_all_from_table_class(Param)
        self.assertEqual(len(PARAMS), len(params_from_database))
        for param in PARAMS:
            self.assertIsNotNone(self.database.get_session().query(Param).filter(Param.value == param['value'],
                                                                                 Param.name == param['name']).first(),
                                 f"Not every record from dictionary exists in database: [param={param}].")

    def test_section_dictionary_builder(self):
        self.database.create_session()
        self.database.build()
        self.database.build_browser_dictionary()
        self.database.build_system_dictionary()
        self.database.build_user_agent_dictionary()
        self.database.build_param_dictionary()
        self.database.build_section_dictionary()
        for section in SECTION.keys():
            db_section = self.database.get_session().query(Section).filter(Section.name == section).first()
            self.assertIsNotNone(db_section, f"Not every section is added to database [section={section}].")
            db_section_x_forbidden_words = self.database.get_session().query(SectionXForbiddenWord).filter(
                SectionXForbiddenWord.section_id == db_section.id).all()
            self.assertEqual(len(FORBIDDEN_WORDS), len(db_section_x_forbidden_words),
                             f"Forbidden words are not set for section [section = {section}].")
            db_section_x_params = self.database.get_session().query(SectionXParam).filter(
                SectionXParam.section == db_section).all()
            section_params = []
            for param in SECTION[section]['params']:
                if param['arg_name'] and param['arg_value']:
                    section_params.append(param)
            self.assertEqual(len(section_params), len(db_section_x_params),
                             f"Params are not set for section: [section={section}].")

    def test_all_dictionaries_builder(self):
        self.database.create_session()
        self.database.build()
        self.database.build_all_dictionaries()
        self.database.build_all_dictionaries()
        for section in SECTION.keys():
            db_section = self.database.get_session().query(Section).filter(Section.name == section).first()
            self.assertIsNotNone(db_section, f"Not every section is added to database [section={section}].")
            db_section_x_forbidden_words = self.database.get_session().query(SectionXForbiddenWord).filter(
                SectionXForbiddenWord.section_id == db_section.id).all()
            self.assertEqual(len(FORBIDDEN_WORDS), len(db_section_x_forbidden_words),
                             f"Forbidden words are not set for section [section = {section}].")
            db_section_x_params = self.database.get_session().query(SectionXParam).filter(
                SectionXParam.section == db_section).all()
            section_params = []
            for param in SECTION[section]['params']:
                if param['arg_name'] and param['arg_value']:
                    section_params.append(param)
            self.assertEqual(len(section_params), len(db_section_x_params),
                             f"Params are not set for section: [section={section}].")


class DatabaseTest(unittest.TestCase):
    def setUp(self):
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

    def tearDown(self):
        self.database = None
        self.database_engine = None
        os.remove(self.db_path)

    def test_section_link_with_params(self):
        pages = [''] + [str(i) for i in range(2, 11)]
        section = self.database.query_all_from_table_class(Section)[0]
        pattern = f"{section.section_url}/(\d*)?(\S*)"
        for page in pages:
            link = self.database.build_section_link_with_params(section, page)
            logging.info(f"Link={link}")
            self.assertRegex(link, pattern, f"Not every link matches pattern: [link={link}, page={page}].")

    def test_adult_section_link_with_params(self):
        pages = [''] + [str(i) for i in range(2, 11)]
        section = self.database.get_session().query(Section).filter(Section.short_name == 'hc').first()
        pattern = f"{section.section_url}/(\d*)?(\S*)"
        for page in pages:
            link = self.database.build_section_link_with_params(section, page)
            logging.info(f"Link={link}")
            self.assertRegex(link, pattern, f"Not every link matches pattern: [link={link}, page={page}].")

    def test_get_section_by_short_name(self):
        section = self.database.get_section_by_short_name('gif')
        self.assertEqual('Adult Gif', section.name,
                         f"Section's name does not match demanded value [section={section}].")

    def test_get_forbidden_words_for_section(self):
        section = self.database.get_section_by_short_name('gif')
        forbidden_words = self.database.get_forbidden_words_for_section(section)
        self.assertEqual('Adult Gif', section.name,
                         f"Section's name does not match demanded value [section={section}].")

    def test_create_thread_record(self):
        section = self.database.get_section_by_short_name('b')
        thread_id = 796031886
        self.database.create_thread_record(thread_id=thread_id, section=section)
        self.database.create_thread_record(thread_id=thread_id, section=section)
        thread = self.database.get_thread_by_4chan_thread_id(thread_id)
        self.assertTrue(thread, "Could not find record of created thread in database.")
        self.assertEqual(1, len(
            self.database.get_session().query(Thread).filter(Thread.thread_4chan_id == thread_id).all()),
                         f"Created more than 1 record for same threads.")

    def test_create_post_record_from_dictionary(self):
        section = self.database.get_section_by_short_name('b')
        thread_id = 796031886
        self.database.create_thread_record(thread_id=thread_id, section=section)
        thread = self.database.get_thread_by_4chan_thread_id(thread_id)
        post_dictionary = {
            'p1231515': {
                '4chan_id': 'p1231515',
                'thread': thread,
                'text': 'This is a text...',
                'is_op': True
            },
        }
        self.database.create_post_record_from_dictionary(post_dictionary)
        post = self.database.get_post_by_4chan_id(post_dictionary['p1231515']['4chan_id'])
        self.assertTrue(post, "Could not find record of created post in database.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
