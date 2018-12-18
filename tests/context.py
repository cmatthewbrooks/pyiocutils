# This idea was taken from:
# https://docs.python-guide.org/writing/structure/ 

import os,sys

sys.path.append( 
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from pyiocutils.ioc import Ioc as Ioc
from pyiocutils.iocfile import IocFile as IocFile
from pyiocutils.iocargs import IocArgs as IocArgs
