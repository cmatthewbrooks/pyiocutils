TEST_DOMAINS_GOOD = [
    'cmatthewbrooks.com',
    'cmatthewbrooks[.]com',
    'google.com',
    'www.badguy.com',
    'www.badguy.xyz'
]

TEST_DOMAINS_BAD = [
    'asdfasdfasdfasdf',
    'a',
    ';klj23;4lkj2;3k4j;k'
]

TEST_IPS_GOOD = [
    '1.1.1.1',
    '8.8.8.8',
    '123.123.123.123',
    '123.123.123[.]123',
    '123[.]123[.]123[.]123',
    '123,123,123,123',
    '123.123,123.123'
]

TEST_IPS_BAD = [
    '999',
    '999.999.999.999',
    '123.123.123'
]

TEST_MD5_GOOD = [
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    '931606baaa7a2b4ef61198406f8fc3f4',
    '931606BAAA7A2B4EF61198406F8FC3F4'
]

TEST_MD5_BAD = [
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    '9999999999999999999999999999999999999999'
    'zxczxczxczxczxczxczxczxczxczxczxc'
]

TEST_SHA1_GOOD = [
    'd3a21675a8f19518d8b8f3cef0f6a21de1da6cc7',
    'D3A21675A8F19518D8B8F3CEF0F6A21DE1DA6CC7',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    '9999999999999999999999999999999999999999'
]

TEST_SHA1_BAD = [
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz',
    'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
]

TEST_SHA256_GOOD = [
    '0d06f9724af41b13cdacea133530b9129a48450230feef9632d53d5bbb837c8c',
    '0D06F9724AF41B13CDACEA133530B9129A48450230FEEF9632D53D5BBB837C8C',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    '9999999999999999999999999999999999999999999999999999999999999999'
]

TEST_SHA256_BAD = [
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
    'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz',
    'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
]

TEST_EMAILS_GOOD = [
    'me@cmatthewbrooks.com',
    'hilaryclinton@privatemailserver.com',
    'badguy@baguyserver.xyz'
]

TEST_EMAILS_BAD = [
    'cmatthewbrooks.com',
    'me@cmatthewbrooks'
]

TEST_NEUTERED_INDICATORS = [
    'cmatthewbrooks[.]com',
    'me[@]cmatthewbrooks[.]com',
    'me[@]cmatthewbrooks.com'
]


ALL_INDICATORS_GOOD = (
    TEST_DOMAINS_GOOD + 
    TEST_IPS_GOOD + 
    TEST_MD5_GOOD + 
    TEST_SHA1_GOOD +
    TEST_SHA256_GOOD + 
    TEST_EMAILS_GOOD
)

ALL_INDICATORS_BAD = (
    TEST_DOMAINS_BAD + 
    TEST_IPS_BAD + 
    TEST_MD5_BAD + 
    TEST_SHA1_BAD +
    TEST_SHA256_BAD + 
    TEST_EMAILS_BAD
)
