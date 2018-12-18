import os

from .ioc import Ioc as Ioc
from .iocfile import IocFile as IocFile

class IocArgs:

    @staticmethod
    def args_to_set(args):

        indicators = []



        if len(args) == 1 and os.path.isfile(args[0]):

            indicator_file = IocFile(args[0])
            indicators = indicator_file.all_indicators()

        elif len(args) == 1 and ',' in args[0]:

            indicators = args[0].split(',')

        elif isinstance(args, list):

            indicators = args

        else:

            raise Exception("Cannot parse indicators from args")



        return sorted(set(indicators))
