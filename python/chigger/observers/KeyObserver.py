#pylint: disable=missing-docstring
#* This file is part of the MOOSE framework
#* https://www.mooseframework.org
#*
#* All rights reserved, see COPYRIGHT for full restrictions
#* https://github.com/idaholab/moose/blob/master/COPYRIGHT
#*
#* Licensed under LGPL 2.1, please see LICENSE for details
#* https://www.gnu.org/licenses/lgpl-2.1.html

from ChiggerObserver import ChiggerObserver
class KeyObserver(ChiggerObserver):
    """
    Class for creating key press observers to be passed in to RenderWindow object.
    """
    @staticmethod
    def getOptions():
        opt = ChiggerObserver.getOptions()
        return opt

    def __init__(self, **kwargs):
        super(KeyObserver, self).__init__(**kwargs)
        self._key = None

    def init(self, window):
        """
        Add the KeyPressEvent for this object.
        """
        super(KeyObserver, self).init(window)
        window.getVTKInteractor().AddObserver('KeyPressEvent', self._callback)

    def _callback(self, obj, event): #pylint: disable=unused-argument
        """
        The function to be called by the RenderWindow.

        Inputs:
            obj, event: Required by VTK.
        """
        self._key = obj.GetKeySym()
        self.update()
        self._key = None
