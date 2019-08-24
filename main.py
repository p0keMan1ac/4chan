from argparse import ArgumentParser
import datetime
import logging
import os
import time

from base_executor import ExecutorFactory
from Database.database_wrapper import DatabaseEngine
from Database.database_handler import DatabaseHandler

# Global variables.
separator = "*" * 80


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-d", "--db_file", dest="database_filename", default='basicDB.sqlite',
                        help="Relative path to database file.", metavar="DATABASE_FILE")
    parser.add_argument("-t", "--db_type", dest="database_type", default='sqlite',
                        help="Type of used database.", metavar="DATABASE_TYPE")
    parser.add_argument("-b", "--build_directories", type=bool, dest="do_build_dictionaries",
                        default=True, help="Create database dictionaries.", metavar="[True/False]")
    parser.add_argument("-s", "--short_names", metavar="[SHORT_NAMES]", default=['b'], dest='short_names',
                        type=str, nargs='+', help="Pass table of short names of categories")
    parser.add_argument("-c", "--executor_class", dest="executor_class", default='CommonExecutor',
                        help="Set kind of executor. "
                             "[CommonExecutor, "
                             "DownloadExecutor, "
                             "FindNewThreadsExecutor, "
                             "FindNewPostsAndMediasExecutor]",
                        metavar="KIND_EXECUTOR")
    parser.add_argument("-w", "--wait_time", dest="wait_time", default=5, type=int,
                        help="Time to wait between checks.", metavar="5")
    return parser.parse_args()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    logging.info(separator)
    logging.info(f"Starting program at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
    # Parsed values.
    logging.info("Parsing arguments...")
    args = parse_args()
    db_filename = args.database_filename
    logging.info(f"db_filename = {db_filename}")
    db_directory = os.path.join(os.getcwd(), 'Database')
    db_path = f'{db_directory}/{db_filename}'
    logging.info(f"db_path = {db_path}")
    database_type = args.database_type
    logging.info(f"database_type = {database_type}")
    do_build_dictionaries = args.do_build_dictionaries
    logging.info(f"do_build_dictionaries = {do_build_dictionaries}")
    short_names = args.short_names
    logging.info(f"short_names = {short_names}")
    executor_class = args.executor_class
    logging.info(f"executor_class = {args.executor_class}")
    wait_time = args.wait_time
    logging.info(f"wait_time = {args.wait_time}")
    logging.info("Arguments parsed.")

    # Executor Factory
    executorFactory = ExecutorFactory()

    with(DatabaseEngine(database_type='sqlite', path_to_database_file=db_path)) as database_engine:
        if do_build_dictionaries:
            logging.info("Creating all dictionaries for database...")
            with DatabaseHandler(database_engine.get_engine()) as database_session:
                database_session.build_all_dictionaries()
            logging.info("All dictionaries for database created.")
            try:

                while True:
                    executorFactory.do_job(executor_class, DatabaseHandler(database_engine.get_engine()), short_names)
                    logging.info("Finished check...")
                    logging.info("New check starting in 5 seconds...")
                    time.sleep(wait_time)
            except KeyboardInterrupt:
                logging.info("Finishing program after CTRL+C...")
            finally:
                logging.info(separator)
                logging.info(f"Finished working at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")
                logging.info(separator)
