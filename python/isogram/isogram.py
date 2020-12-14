def is_isogram(string):
    s = string.replace(' ', '').replace('-','').lower()
    mapp = {e: s.count(e) for e in s}
    if len(mapp.values()) == len(s):
        return True
    return False
#
#	if len(s) == len(set(s)):
#        return True
#    return False
#
