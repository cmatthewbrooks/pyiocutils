import os,sys

from .ioc import Ioc as Ioc

class IocFile:

    def __init__(self, file):

        self.file = file

        self.domains = set()
        self.ips = set()
        self.hashes = set()
        self.emails = set()

        self._parse_indicator_file(self.file)

    def all_indicators(self):
        
        return self.domains.union(
            self.ips,
            self.hashes,
            self.emails
        )

    # These methods are only meant to be called from inside this class.

    def _parse_indicator_file(self, file):

        try:

            with open(file, 'r') as f:
        
                for line in f.readlines():

                    line = line.strip('\n')

                    if Ioc.is_domain(line):
                        self.domains.add(Ioc.clean_indicator(line))
                    elif Ioc.is_ip(line):
                        self.ips.add(Ioc.clean_indicator(line))
                    elif Ioc.is_hash(line):
                        self.hashes.add(Ioc.clean_indicator(line))
                    elif Ioc.is_email(line):
                        self.emails.add(Ioc.clean_indicator(line))
                    else:
                        pass

        except:

            raise Exception('Could not parse indicator file')
