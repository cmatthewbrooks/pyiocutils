import argparse

#####################################
#
# Import from the pyiocutils package
#
#####################################

from pyiocutils.ioc import Ioc as Ioc
from pyiocutils.iocargs import IocArgs as IocArgs



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    
    #################################################################
    #
    # Add an indicators argument that can take multiple elements
    #
    #################################################################
    
    parser.add_argument(
        '-i','--indicators', nargs='*', dest='indicators', default=[]
    )

    args = parser.parse_args()



    ################################################################
    #
    # Use the IocArgs module that has different options
    #
    ################################################################

    indicators = IocArgs.args_to_set(args.indicators)



    ################################################################
    #
    # And check and see how things were parsed!
    #
    ###############################################################
    
    for indicator in indicators:
        print indicator + ' is ' + Ioc.get_indicator_type(indicator)
