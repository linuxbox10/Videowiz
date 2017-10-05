# Embedded file name: /usr/lib/enigma2/python/Plugins/Extensions/vuplusvideoreset/plugin.py
#Original idea by ipad. thanks to them.
from . import _
import os
from Screens.Screen import Screen
from Plugins.Plugin import PluginDescriptor
from Components.Label import Label
from sys import modules
from Components.config import config, configfile

class vuplusvideoreset(Screen):
    skin = '\n\t\t<screen position="center,center" size="550,150" title="VUplus Video Reset">\n\t\t\t<widget name="Text" position="20,10" size="500,30" font="Regular; 22" halign="left" zPosition="2" transparent="0" />\n\t\t</screen>'

    def __init__(self, session, args = 0):
        self.session = session
        Screen.__init__(self, session)
        self['Text'] = Label(_('Video Wizard will run after reboot - Please wait'))
        config.misc.videowizardenabled.value = True
        config.save()
        configfile.save()
        os.system('reboot')


def main(session, **kwargs):
    session.open(vuplusvideoreset)


def Plugins(**kwargs):
    plist = [PluginDescriptor(name=_('VUplus Emergency Video Reset'), description=_('Video Wizard will run after reboot'), where=PluginDescriptor.WHERE_PLUGINMENU, icon='vuten.png', fnc=main)]
    return plist