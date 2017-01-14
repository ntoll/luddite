"""
Luddite - the anti-browser. :-)
"""
import os
import logging
from luddite import __version__
from luddite.browser import Browser


def setup_logging():
    """
    This could probably be more elegant.
    """
    home = os.path.expanduser('~')
    log_dir = os.path.join(home, 'luddite')
    log_file = os.path.join(log_dir, 'luddite.log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_fmt = '%(asctime)s - %(name)s(%(funcName)s) %(levelname)s: %(message)s'
    logging.basicConfig(filename=log_file, filemode='w', format=log_fmt,
                        level=logging.DEBUG)
    print('Logging to {}'.format(log_file))


def run(urls):
    setup_logging()
    logging.info('Starting Luddite {}'.format(__version__))
    logging.info(urls)
    browser = Browser()
    for url in urls:
        browser.create_tab(url)
    browser.mainloop()
