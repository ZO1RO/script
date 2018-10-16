#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer
import sys
class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
    # Override method
    # Take secret_key instead of an instance of a Flask app
    def get_signing_serializer(self, secret_key):
        if not secret_key:
            return None
        signer_kwargs = dict(
            key_derivation=self.key_derivation,
            digest_method=self.digest_method
        )
        return URLSafeTimedSerializer(secret_key, salt=self.salt,
                                      serializer=self.serializer,
                                      signer_kwargs=signer_kwargs)
def decodeFlaskCookie(secret_key, cookieValue):
    sscsi = SimpleSecureCookieSessionInterface()
    signingSerializer = sscsi.get_signing_serializer(secret_key)
    return signingSerializer.loads(cookieValue)
# Keep in mind that flask uses unicode strings for the
# dictionary keys
def encodeFlaskCookie(secret_key, cookieDict):
    sscsi = SimpleSecureCookieSessionInterface()
    signingSerializer = sscsi.get_signing_serializer(secret_key)
    return signingSerializer.dumps(cookieDict)

sk = '385c16dd09098b011d0086f9e218a0a2'
#sessionDict = {u'user_id':sys.argv[1]}
#cookie = encodeFlaskCookie(sk, sessionDict)
#通过密钥进行加密解密
decodedDict = decodeFlaskCookie(sk, ".eJwlj0tOBTEMwO7S9Vvk1zZ5lxklbSIQCKQZWCHuzkgcwJb9044683ppz_L3Kx_teN3t2cw7aS-tAJRUrb4MGZWCS61IPZd1Zp4dSaZiuayp27DnDmYZxknIAMPQhcFj1q3xwZwuQGHTl9CAiT4Sg3FiBxKDcAhsj7aus46vz7f8uHvIVx-2KYgVR0KEWXhZWaIsCtetA5bd3PeV5_-Ett8_-MA9tQ.DqbcHQ.-7UkG_YaeIg89ziNDxCTkTILaDs")
decodedDict[u'user_id']=u'1'
cookie=encodeFlaskCookie('385c16dd09098b011d0086f9e218a0a2',
                          decodedDict)
print cookie,decodedDict



from flask.sessions import SecureCookieSessionInterface
from itsdangerous import URLSafeTimedSerializer

class SimpleSecureCookieSessionInterface(SecureCookieSessionInterface):
    # Override method
    # Take secret_key instead of an instance of a Flask app
    def get_signing_serializer(self, secret_key):
        if not secret_key:
            return None
        signer_kwargs = dict(
            key_derivation=self.key_derivation,
            digest_method=self.digest_method
        )
        return URLSafeTimedSerializer(secret_key, salt=self.salt,
                                      serializer=self.serializer,
                                      signer_kwargs=signer_kwargs)


def decodeFlaskCookie(secret_key, cookieValue):
    sscsi = SimpleSecureCookieSessionInterface()
    signingSerializer = sscsi.get_signing_serializer(secret_key)
    return signingSerializer.loads(cookieValue)

# Keep in mind that flask uses unicode strings for the
# dictionary keys


def encodeFlaskCookie(secret_key, cookieDict):
    sscsi = SimpleSecureCookieSessionInterface()
    signingSerializer = sscsi.get_signing_serializer(secret_key)
    return signingSerializer.dumps(cookieDict)

cookie = decodeFlaskCookie('385c16dd09098b011d0086f9e218a0a2',
                          '.eJwlj0tOBTEMwO7S9Vvk1zZ5lxklbSIQCKQZWCHuzkgcwJb9044683ppz_L3Kx_teN3t2cw7aS-tAJRUrb4MGZWCS61IPZd1Zp4dSaZiuayp27DnDmYZxknIAMPQhcFj1q3xwZwuQGHTl9CAiT4Sg3FiBxKDcAhsj7aus46vz7f8uHvIVx-2KYgVR0KEWXhZWaIsCtetA5bd3PeV5_-Ett8_-MA9tQ.DqbcHQ.-7UkG_YaeIg89ziNDxCTkTILaDs')

cookie[u'user_id'] = u'1'

print encodeFlaskCookie('385c16dd09098b011d0086f9e218a0a2',
                          cookie),cookie