"""
author: meiqihezi
Core components for emoji.
"""

import re
from emojiswitch import unicode_codes

__all__ = ["emojize", "demojize", "get_emoji_regexp"]
_DEFAULT_DELIMITER = ":"
_EMOJI_REGEXP = None


def emojize(string,  delimiters=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER), lang="zh"):
    """
    Replace emoji names in a string with unicode codes
    :param string: String contains emoji names
    :param delimiters: (optional) Use delimiters other than _DEFAULT_DELIMITER
    :param lang: Language(default Chinese)
    :return: String after emojize
    """
    if lang == "zh":
        pattern = re.compile(u"(%s[\u4e00-\u9fa5]+%s)" % delimiters)
    else:
        pattern = re.compile(u'(%s[a-zA-Z0-9\\+\\-_&.ô’Åéãíç()!#*]+%s)' % delimiters)

    def replace(match):
        mg = match.group(1).replace(delimiters[0], _DEFAULT_DELIMITER).replace(delimiters[1], _DEFAULT_DELIMITER)
        if lang not in unicode_codes.LANG_EMOJI.keys():
            raise ValueError("invalid language: {}".format(lang))
        emj = unicode_codes.LANG_EMOJI[lang].get(mg, mg)
        return emj

    return pattern.sub(replace, string)


def demojize(string, delimiters=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER), lang="zh"):
    """
    Replace unicode emoji in a string with emoji shortcodes. Useful for storage
    :param string: String contains unicode characters. MUST BE UNICODE
    :param delimiters: (optional) Return emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``
    :param lang: lang: Language(default Chinese)
    :return: String after demojize
    """
    def replace(match):
        if lang not in unicode_codes.EMOJI_LANG.keys():
            raise ValueError("invalid language: {}".format(lang))
        codes_dict = unicode_codes.EMOJI_LANG[lang]
        val = codes_dict.get(match.group(0), match.group(0))
        return delimiters[0] + val[1:-1] + delimiters[1]

    return re.sub(u'\ufe0f', '', (get_emoji_regexp().sub(replace, string)))


def get_emoji_regexp():

    """Returns compiled regular expression that matches emojis defined in
    ``unicode_codes.EN_EMOJI``. The regular expression is only compiled once.
    """

    global _EMOJI_REGEXP
    # Build emoji regexp once
    if _EMOJI_REGEXP is None:
        # Sort emojis by length to make sure multi-character emojis are
        # matched first
        emojis = sorted(unicode_codes.LANG_EMOJI["en"].values(), key=len,
                        reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        _EMOJI_REGEXP = re.compile(pattern)
    return _EMOJI_REGEXP
