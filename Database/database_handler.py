from datetime import datetime
import logging
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.sql import func
from Database.database_dictionaries import *

Base = declarative_base()


# Dictionaries.
class ResponseCode(Base):
    __tablename__ = 'response_code'
    id = Column(Integer, primary_key=True)
    code = Column(Integer, nullable=False, unique=True)
    description = Column(String(250), nullable=False)
    is_ok = Column(Boolean, default=True)

    def __repr__(self):
        return f'<ResponseCode=(id={self.id}, code={self.code}'


class System(Base):
    __tablename__ = 'system'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)

    def __repr__(self):
        return f'<System=(id={self.id}, name={self.name})>'


class Browser(Base):
    __tablename__ = 'browser'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)

    def __repr__(self):
        return f'<Browser=(id={self.id}, name={self.name})>'


class UserAgent(Base):
    __tablename__ = 'user_agent'
    id = Column(Integer, primary_key=True)
    value = Column(String(250), nullable=False)
    is_default = Column(Boolean, default=False)
    browser_id = Column(Integer, ForeignKey('browser.id'))
    browser = relationship(Browser)
    system_id = Column(Integer, ForeignKey('system.id'))
    system = relationship(System)

    def __repr__(self):
        return f'<UserAgent=(id={self.id}, value={self.value}, is_default={self.is_default})>'


class Param(Base):
    __tablename__ = 'param'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    value = Column(String(250), nullable=False)

    def __repr__(self):
        return f'<Param(id={self.id}, arg_name={self.name}, arg_value={self.value})>'


class Section(Base):
    __tablename__ = 'section'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    short_name = Column(String(10), unique=True, nullable=False)
    is_adult = Column(Boolean, default=False)
    base_url = Column(String(250), nullable=False)
    section_url = Column(String(250), unique=True, nullable=False)
    user_agent_id = Column(Integer, ForeignKey('user_agent.id'))
    user_agent = relationship(UserAgent)

    def __repr__(self):
        return f'Section<(id={self.id}, name={self.name}, short_name={self.short_name})>'


class SectionXParam(Base):
    __tablename__ = 'section_x_param'
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('section.id'))
    section = relationship(Section)
    param_id = Column(Integer, ForeignKey('param.id'))
    param = relationship(Param)

    def __repr__(self):
        return f'<SectionXParam(id={self.id}, section={self.section}, param={self.param}>'


class ForbiddenWord(Base):
    __tablename__ = 'forbidden_word'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)

    def __repr__(self):
        return f'<ForbiddenWord(id={self.id}, name={self.name})>'


class SectionXForbiddenWord(Base):
    __tablename__ = 'section_x_forbidden_word'
    id = Column(Integer, primary_key=True)
    section_id = Column(Integer, ForeignKey('section.id'))
    section = relationship(Section, backref=backref('sections_x_forbidden_words'))
    forbidden_word_id = Column(Integer, ForeignKey('forbidden_word.id'))
    forbidden_word = relationship(ForbiddenWord, backref=backref('sections_x_forbidden_words'))

    def __repr__(self):
        return f'<SectionXForbiddenWord(id={self.id}, section={self.section}, forbidden_word={self.forbidden_word})>'


class Thread(Base):
    __tablename__ = 'thread'
    id = Column(Integer, primary_key=True)
    link = Column(String(250), nullable=False)
    thread_4chan_id = Column(Integer, nullable=False, default=None)
    subject = Column(String(250), nullable=True)
    title = Column(String(250), nullable=True)
    section_id = Column(Integer, ForeignKey('section.id'))
    section = relationship(Section, backref=backref('threads'))
    time_created = Column(DateTime(timezone=False), server_default=func.now())
    time_updated = Column(DateTime(timezone=False), onupdate=func.now())
    is_online = Column(Boolean, default=True)
    is_to_check = Column(Boolean, default=True)
    is_forbidden = Column(Boolean, default=False)
    thread_4chan_id_section_unique = UniqueConstraint(thread_4chan_id, section_id)

    def __repr__(self):
        return f'<Thread(id={self.id}, link={self.link}, section={self.section})>'


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    thread_id = Column(Integer, ForeignKey('thread.id'), nullable=False)
    thread = relationship(Thread, backref=backref('posts'))
    post_4chan_id = Column(String(50), nullable=False)
    time_created = Column(DateTime(timezone=False), server_default=func.now())
    time_updated = Column(DateTime(timezone=False), onupdate=func.now())
    is_op = Column(Boolean, default=False)
    text = Column(String, nullable=True)

    def __repr__(self):
        return f'<Post(id={self.id}, thread={self.thread})>'


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    link = Column(String(250), nullable=False)
    is_downloaded = Column(Boolean, default=False)
    is_online = Column(Boolean, default=True)
    file_extension = Column(String(50), nullable=False)
    file_name = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    time_created = Column(DateTime(timezone=False), server_default=func.now())
    time_updated = Column(DateTime(timezone=False), onupdate=func.now())

    def __repr__(self):
        return f'<Media(id={self.id}, file={self.file_name}.{self.file_extension}, link={self.link})>'


class DatabaseHandler:
    def __init__(self, engine):
        self.database_engine = engine
        self.database_schema_builder = Base
        self.__session = None

    def __enter__(self):
        self.start_new_session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.close_session()
            logging.error(f'There was error during database handler. Exception[{exc_val}].')
            raise Exception('There was error during database handler.')
        else:
            self.close_session()

    def build(self):
        self.database_schema_builder.metadata.create_all(self.database_engine)

    def create_session(self):
        session_factory = sessionmaker(bind=self.database_engine)
        self.__session = session_factory()

    def get_session(self):
        return self.__session

    def close_session(self):
        self.__session.close()

    def start_new_session(self):
        self.build()
        self.create_session()
        return self.get_session()

    def get_all_tables(self):
        return self.database_schema_builder.metadata.table_names()

    def build_response_code_dictionary(self):
        codes_to_insert = []
        for code in RESPONSE_DICT.keys():
            if int(code) in GOOD_RESPONSE_CODES:
                is_ok = True
            else:
                is_ok = False
            filtered_response_code = self.get_session().query(ResponseCode).filter(ResponseCode.code == code).first()
            if not filtered_response_code:

                code_to_insert = ResponseCode(code=code, description=RESPONSE_DICT[code], is_ok=is_ok)
                codes_to_insert.append(code_to_insert)
            else:
                logging.warning(f"Code {code} already exists in database. Omitting code={code}...")
        if codes_to_insert:
            self.get_session().bulk_save_objects(codes_to_insert)
            self.get_session().commit()

    def build_system_dictionary(self):
        systems = ['Windows', 'Mac OS', 'Linux', 'other']
        systems_to_insert = []
        for system in systems:

            filtered_system = self.get_session().query(System).filter(System.name == system).first()
            if not filtered_system:
                system_to_insert = System(name=system)
                systems_to_insert.append(system_to_insert)
            else:
                logging.warning(f"System {system} already exists in database. Omitting system={system}...")
        if systems_to_insert:
            self.get_session().bulk_save_objects(systems_to_insert)
            self.get_session().commit()

    def build_browser_dictionary(self):
        browsers = ['Chrome', 'Firefox', "Mozilla"]
        browsers_to_insert = []
        for browser in browsers:
            filtered_browser = self.get_session().query(Browser).filter(Browser.name == browser).first()
            if not filtered_browser:
                browser_to_insert = Browser(name=browser)
                browsers_to_insert.append(browser_to_insert)

            else:
                logging.warning(f"Browser {browser} already exists in database. Omitting browser={browser}...")
        if browsers_to_insert:
            self.get_session().bulk_save_objects(browsers_to_insert)
            self.get_session().commit()

    def build_user_agent_dictionary(self):
        user_agents_to_insert = []
        for user_agent_key in USER_AGENT_DICT.keys():
            user_agent = USER_AGENT_DICT[user_agent_key]
            filtered_user_agent = self.get_session().query(UserAgent).filter(UserAgent.value == user_agent_key).first()
            if not filtered_user_agent:
                browser = self.get_session().query(Browser).filter(
                    Browser.name == user_agent['browser']).first()
                system = self.get_session().query(System).filter(
                    System.name == user_agent['system']).first()
                is_default = user_agent['is_default']
                user_agent_to_insert = UserAgent(value=user_agent_key, browser_id=browser.id, system_id=system.id,
                                                 is_default=is_default)
                user_agents_to_insert.append(user_agent_to_insert)

            else:
                logging.warning(f"UserAgent: {user_agent_key}={user_agent} already exists in database. Omitting ...")
        if user_agents_to_insert:
            self.get_session().bulk_save_objects(user_agents_to_insert)
            self.get_session().commit()

    def build_param_dictionary(self):
        params_to_insert = []
        for param in PARAMS:
            filtered_param = self.get_session().query(Param).filter(Param.name == param['name'],
                                                                    Param.value == param['value']).first()
            if not filtered_param:
                param_to_insert = Param(name=param['name'], value=param['value'])
                params_to_insert.append(param_to_insert)
            else:
                logging.warning(f"Param [name={param['name']}, "
                                f"value={param['value']}] already exists in database. Omitting param...")
        if params_to_insert:
            self.get_session().bulk_save_objects(params_to_insert)
            self.get_session().commit()

    def build_section_dictionary(self):
        self.get_session().query(SectionXForbiddenWord).delete()
        self.get_session().query(Section).delete()
        self.get_session().query(SectionXParam).delete()
        user_agent = self.get_session().query(UserAgent).filter(UserAgent.is_default == True).first()

        for section_key in SECTION.keys():
            section = SECTION[section_key]
            # Get simple values from dictionary of section
            if section['category'] == 'adult':
                is_adult = True
            else:
                is_adult = False
            new_forbidden_words = []
            forbidden_words = []
            new_params = []
            params = []
            for forbidden_word in FORBIDDEN_WORDS:
                forbidden_word = forbidden_word.upper()
                db_forbidden_word = self.get_session().query(ForbiddenWord).filter(
                    ForbiddenWord.name == forbidden_word).first()
                if not db_forbidden_word:
                    new_forbidden_word = ForbiddenWord(name=forbidden_word)
                    new_forbidden_words.append(new_forbidden_word)
                else:
                    forbidden_words.append(db_forbidden_word)
            for param in section['params']:
                if param['arg_name'] and param['arg_value']:
                    db_param = self.get_session().query(Param).filter(Param.name == param['arg_name'],
                                                                      Param.value == param['arg_value']).first()
                    if not db_param:
                        new_param = Param(name=param['arg_value'], value=param['arg_value'])
                        new_params.append(new_param)
                    else:
                        params.append(db_param)

            db_section = Section(name=section_key, user_agent=user_agent, short_name=section['short_name'],
                                 is_adult=is_adult,
                                 base_url=section['base_url'], section_url=section['section_url'])
            self.get_session().add(db_section)
            if new_forbidden_words:
                for forbidden_word in new_forbidden_words:
                    self.get_session().add(forbidden_word)
                    section_x_forbidden_word = SectionXForbiddenWord(section=db_section, forbidden_word=forbidden_word)
                    self.get_session().add(section_x_forbidden_word)

            if new_params:
                for param in new_params:
                    self.get_session().add(param)
                    section_param = SectionXParam(section=db_section, param=param)
                    self.get_session().add(section_param)
            if params:
                for param in params:
                    section_param = SectionXParam(section=db_section, param=param)
                    self.get_session().add(section_param)
            if forbidden_words:
                for forbidden_word in forbidden_words:
                    section_x_forbidden_word = SectionXForbiddenWord(section=db_section, forbidden_word=forbidden_word)
                    self.get_session().add(section_x_forbidden_word)
            self.get_session().commit()

    def build_all_dictionaries(self):
        if not self.query_all_from_table_class(ResponseCode):
            self.build_response_code_dictionary()
        if not self.query_all_from_table_class(Browser):
            self.build_browser_dictionary()
        if not self.query_all_from_table_class(System):
            self.build_system_dictionary()
        if not self.query_all_from_table_class(UserAgent):
            self.build_user_agent_dictionary()
        if not self.query_all_from_table_class(Param):
            self.build_param_dictionary()
        if not self.query_all_from_table_class(Section):
            self.build_section_dictionary()

    def build_section_link_with_params(self, section, page):
        section_params = self.get_session().query(SectionXParam).filter(SectionXParam.section == section).all()
        arg_strings = []
        for section_param in section_params:
            arg_strings.append(f'{section_param.param.name}={section_param.param.value}')
        arg_string = '&'.join(arg_strings)
        return f'{section.section_url}/{page}?{arg_string}'

    def query_all_from_table_class(self, table_class):
        return self.get_session().query(table_class).all()

    def get_section_by_short_name(self, short_name):
        return self.get_session().query(Section).filter(Section.short_name == short_name).first()
        pass

    def get_good_response_codes(self):
        good_response_codes_from_db = self.get_session().query(ResponseCode.code).filter(ResponseCode.is_ok == True)
        good_response_codes = [response_code.code for response_code in good_response_codes_from_db]
        return good_response_codes

    def get_thread_by_4chan_thread_id(self, thread_id):
        return self.get_session().query(Thread).filter(Thread.thread_4chan_id == thread_id).first()

    def get_all_thread_links_of_section(self, section):
        return self.get_session().query(Thread.link).filter(Thread.section == section).all()

    def create_thread_record(self, thread_id, section):
        # logging.info(f"HANDLING THREAD: [id={thread_id}, Section={section.name}]...")
        thread, thread_from_db = None, None

        link_to_thread = str(f'{section.section_url}/thread/{thread_id}')
        thread_from_db = self.get_session().query(Thread).filter(Thread.thread_4chan_id == int(thread_id),
                                                                 Thread.section_id == section.id).first()
        if not thread_from_db:
            try:
                thread = Thread(thread_4chan_id=thread_id, link=link_to_thread, subject=None, section_id=section.id)
                self.get_session().add(thread)
                logging.info(f"Created thread: [id={thread_id}, link={link_to_thread}, Section={section.name}]...")
            except Exception as error:
                error_msg = repr(error)
                logging.warning(
                    f"Could not create thread. Thread:[link={thread.link}, thread_4chan_id = {thread.thread_4chan_id}].")
        else:
            logging.info(
                f"Thread already exists. Updating thread: [id={thread_id}, link={link_to_thread}, Section={section.name}]...")
            thread_from_db.is_online = True
            thread_from_db.is_to_check = True
        self.get_session().commit()
        return thread_from_db if thread_from_db else thread

    def create_post_record_from_dictionary(self, post_dictionary):
        count = 0
        posts_to_insert = []
        for post_id in post_dictionary.keys():
            post = post_dictionary[post_id]
            post_from_db = self.get_session().query(Post).filter(Post.post_4chan_id == post_id).first()
            if not post_from_db:
                count += 1
                posts_to_insert.append(
                    Post(thread_id=post['thread'].id, post_4chan_id=post['4chan_id'], is_op=post['is_op'],
                         text=post['text']))
            else:
                pass
        if posts_to_insert:
            logging.info(f"Creating {count} new posts...")
            self.get_session().bulk_save_objects(posts_to_insert)
        else:
            logging.info("No new posts to create.")
        self.get_session().commit()
        # logging.info(f"Created all new posts.")

    def create_media_record_from_dictionary(self, media_dictionary):
        medias_to_insert = []
        count = 0
        for media_link in media_dictionary.keys():
            media = media_dictionary[media_link]
            media_from_db = self.get_session().query(Media).filter(Media.link == media['link']).first()
            if not media_from_db:
                post = self.get_post_by_4chan_id(media['post']['4chan_id'])
                count += 1
                medias_to_insert.append(Media(link=media_link, file_extension=media['file_extension'],
                                              file_name=media['file_name'], post_id=post.id))
            else:
                # logging.warning(f"Media already in database. Media:[link={media['link']}]. Omitting...")
                pass
        if medias_to_insert:
            logging.info(f"Creating {count} new medias...")
            self.get_session().bulk_save_objects(medias_to_insert)
        else:
            logging.info("No new medias to create.")
        self.get_session().commit()
        # logging.info(f"Created all new medias.")

    def get_post_by_4chan_id(self, post_4chan_id):
        return self.get_session().query(Post).filter(Post.post_4chan_id == post_4chan_id).first()

    def get_forbidden_words_for_section(self, section):
        query = self.get_session().query(ForbiddenWord.name)
        query = query.join(SectionXForbiddenWord)
        forbidden_words = []
        forbidden_words_from_db = query.filter(SectionXForbiddenWord.section_id == section.id).all()
        for forbidden_word in forbidden_words_from_db:
            forbidden_words.append(forbidden_word[0])
        # logging.info(f"FORBIDDEN WORD = {forbidden_words}")
        return forbidden_words

    def commit(self):
        self.get_session().commit()

    def get_medias_to_download(self):
        return self.get_session().query(Media).filter(Media.is_downloaded == False).all()

    def get_threads_to_check_for_new_posts(self, section):
        return self.get_session().query(Thread).filter(Thread.section_id == section.id, Thread.is_online == True,
                                                       Thread.is_to_check == True, Thread.is_forbidden == False).all()



    # def get_posts_of_threads_online_and_forbidden(self, is_online=True, is_forbidden=False):
    #     query = self.get_session().query(Post).filter(Post.thread_id==thread.id, )
    #     query = query.join(SectionXForbiddenWord)
    #     forbidden_words = []
    #     forbidden_words_from_db = query.filter(SectionXForbiddenWord.section_id == section.id).all()
    #     for forbidden_word in forbidden_words_from_db:
    #         forbidden_words.append(forbidden_word[0])
    #     # logging.info(f"FORBIDDEN WORD = {forbidden_words}")
    #     return forbidden_words

    # def update_thread(self, thread, updated_thread):
    #     logging.info(f"Updating thread={thread}.")
    #     thread.subject = updated_thread.subject
    #     thread.title = updated_thread.title
    #     updated_thread = None
    #     self.get_session().commit()
