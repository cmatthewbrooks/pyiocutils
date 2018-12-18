import re

class Ioc:

    DOMAIN = 'domain'
    IP = 'ip'
    MD5 = 'md5'
    SHA1 = 'sha1'
    SHA256 = 'sha256'
    EMAIL = 'email'

    @staticmethod
    def is_domain(domain):

        pattern = r'\A([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\Z'

        domain = Ioc.clean_indicator(domain)

        if re.search(pattern,domain):
            return True

        return False

    @staticmethod
    def is_ip(ip):

        pattern = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

        ip = Ioc.clean_indicator(ip)

        if re.search(pattern,ip):
            return True

        return False

    @staticmethod
    def is_md5(hash):

        pattern = r'(?=(\b[A-Fa-f0-9]{32}\b))'

        if re.search(pattern,hash):
            return True

        return False

    @staticmethod
    def is_sha1(hash):

        pattern = r'(?=(\b[A-Fa-f0-9]{40}\b))'

        if re.search(pattern,hash):
            return True

        return False

    @staticmethod
    def is_sha256(hash):

        pattern = r'(?=(\b[A-Fa-f0-9]{64}\b))'

        if re.search(pattern,hash):
            return True

        return False
    
    @staticmethod
    def is_hash(hash):

        if Ioc.is_md5(hash):
            return True
        elif Ioc.is_sha1(hash):
            return True
        elif Ioc.is_sha256(hash):
            return True
        else:
            return False

    @staticmethod
    def is_email(email):

        pattern = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'

        email = Ioc.clean_indicator(email)

        if re.search(pattern, email):
            return True

        return False

    @staticmethod
    def is_indicator(indicator):

        indicator = Ioc.clean_indicator(indicator)

        if Ioc.is_domain(indicator) or \
            Ioc.is_ip(indicator) or \
            Ioc.is_hash(indicator) or \
            Ioc.is_email(indicator):
            return True

        return False

    @staticmethod
    def get_indicator_type(indicator):

        indicator = Ioc.clean_indicator(indicator)

        if Ioc.is_domain(indicator):
            return Ioc.DOMAIN
        elif Ioc.is_ip(indicator):
            return Ioc.IP
        elif Ioc.is_md5(indicator):
            return Ioc.MD5
        elif Ioc.is_sha1(indicator):
            return Ioc.SHA1
        elif Ioc.is_sha256(indicator):
            return Ioc.SHA256
        elif Ioc.is_email(indicator):
            return Ioc.EMAIL
        else:
            return None

    @staticmethod
    def clean_indicator(indicator):

        clean_indicator = indicator

        clean_indicator = clean_indicator.replace('[.]','.')
        clean_indicator = clean_indicator.replace(',','.')
        clean_indicator = clean_indicator.replace('[@]','@')

        return clean_indicator
