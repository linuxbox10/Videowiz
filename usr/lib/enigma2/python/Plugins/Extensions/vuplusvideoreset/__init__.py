# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/vuplusvideoreset/__init__.py
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import os, gettext
PluginLanguageDomain = 'vuplusvideoreset'
PluginLanguagePath = 'Extensions/vuplusvideoreset/locale'

def localeInit():
    lang = language.getLanguage()[:2]
    os.environ['LANGUAGE'] = lang
    print '[' + PluginLanguageDomain + '] set language to ', lang
    gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
    t = gettext.dgettext(PluginLanguageDomain, txt)
    if t == txt:
        print '[' + PluginLanguageDomain + '] fallback to default translation for', txt
        t = txt
    return t


localeInit()
language.addCallback(localeInit)