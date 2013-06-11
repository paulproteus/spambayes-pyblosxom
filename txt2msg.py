from lxml import etree
import calendar
import time
import email.utils

import codecs
import sys
utf8_stdout = codecs.getwriter('utf8')(sys.stdout)


### FIXME: content encoding utf8

def _get_tag(data, tag_name):
    out = data.xpath('//' + tag_name)
    if out:
        return out[0].text
    return None

def split_headers_from_body():
    return '\r\n'

def get_date(data):
    w3cdate = _get_tag(data, 'w3cdate')
    assert (w3cdate is not None)

    # Silly hack.
    msg_time = time.strptime(w3cdate,
        "%Y-%m-%dT%H:%M:%SZ")
    out = email.utils.formatdate(calendar.timegm(msg_time))
    return ("Date: " + out + "\r\n")

def get_received(data):
    ipaddress = _get_tag(data, 'ipaddress')
    assert (ipaddress is not None)

    return "Received: from %s" % (ipaddress,) + "\r\n"

def get_from(data):
    from_data = []

    author = _get_tag(data, 'author')
    assert (author is not None)
    from_data.append(author)

    email_addr = _get_tag(data, 'email')
    if email_addr:
        from_data.append(email_addr)

    if len(from_data) > 1:
        as_string = email.utils.formataddr(from_data)
    else:
        as_string = from_data[0]

    return "From: " + as_string + '\r\n'


def get_subject(data):
    value = _get_tag(data, 'title')
    assert (value is not None)

    return "Subject: " + value + "\r\n"

def get_body(data):
    body = _get_tag(data, 'description')
    out = ''
    for line in body.split('\n'):
        if not line.endswith('\r'):
            line += '\r'
        out += line + '\n'
    return out + '\r\n'

def get_homepage(data):
    value = _get_tag(data, 'link')
    if value:
        return "Homepage: %s\r\n" % (
            value,)
    return ''

def main(filename):
    file_contents = open(filename).read().replace('\0', '')
    data = etree.fromstring(file_contents)

    out = ''
    out += get_date(data)
    out += get_received(data)
    out += get_from(data)
    out += get_subject(data)
    out += split_headers_from_body()
    out += get_body(data)
    out += get_homepage(data)
    return out

if __name__ == '__main__':
    utf8_stdout.write(main(sys.argv[1]))
