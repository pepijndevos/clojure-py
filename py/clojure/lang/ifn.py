from py.clojure.lang.cljexceptions import AbstractMethodCall

class IFn(object):
    def __call__(self, *args):
        raise AbstractMethodCall()