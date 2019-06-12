# coding: utf-8
from __future__ import print_function
import sys
from optparse import OptionParser

try:
    from itertools import ifilter as filter
except ImportError:
    pass

from ip138.logger import logger
from ip138 import __version__

try:
    if sys.version_info < (3, 0, 0):
        import codecs
        import locale
        sys.stdout = codecs.getwriter(
            locale.getpreferredencoding())(sys.stdout)
        sys.stderr = codecs.getwriter(
            locale.getpreferredencoding())(sys.stderr)

except NameError:
    # python3
    pass


def banner():
    logger.info(u'''ip138 IP 地理信息查询 ver %s''' % __version__)


def cmd_parser():
    parser = OptionParser()
    parser.add_option('--ip', type='string', dest='ip',
                      action='store', help='ip address')

    try:
        sys.argv = list(map(lambda x: unicode(
            x.decode(sys.stdin.encoding)), sys.argv))
    except (NameError, TypeError):
        pass
    except UnicodeDecodeError:
        exit(0)

    args, _ = parser.parse_args(sys.argv[1:])

    return args
