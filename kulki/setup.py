from distutils.core import setup
import py2exe, pygame, sys, os
from modulefinder import Module

origIsSystemDLL = py2exe.build_exe.isSystemDLL # save the orginal before we edit it
def isSystemDLL(pathname):
    # checks if the freetype and ogg dll files are being included
    if os.path.basename(pathname).lower() in ("libfreetype-6.dll", "libogg-0.dll","sdl_ttf.dll"): # "sdl_ttf.dll" added by arit.
            return 0
    return origIsSystemDLL(pathname) # return the orginal function
py2exe.build_exe.isSystemDLL = isSystemDLL # override the default function with this one
 
class pygame2exe(py2exe.build_exe.py2exe): #This hack make sure that pygame default font is copied: no need to modify code for specifying default font
    def copy_extensions(self, extensions):
        #Get pygame default font
        pygamedir = os.path.split(pygame.base.__file__)[0]
        pygame_default_font = os.path.join(pygamedir, pygame.font.get_default_font())
 
        #Add font to list of extension to be copied
        extensions.append(Module("pygame.font", pygame_default_font))
        py2exe.build_exe.py2exe.copy_extensions(self, extensions)

setup(name='Kulki',
      windows=[{'script': "Kulki.py",
                'icon_resources': [(0, 'ikona.ico')]
                }],
      data_files = ['czerwona.png', 'zielona.png', 'niebieska.png', 'zolta.png',
                    'pomaranczowa.png', 'biala.png', 'rozowa.png',
                    'podswietl.png', 'zgas.png', 'pusta.png', 'siatka.png',
                    'nick.png', 'wynik.txt', 'wyniki.png'
                    ]
      )
