
"""
    Copyright (C) <2010>  Autin L. TSRI
    
    This file git_upy/setup.py is part of upy.

    upy is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    upy is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with upy.  If not, see <http://www.gnu.org/licenses/gpl-3.0.html>.
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:16:58 2011

@author: Ludovic Autin
"""

from distutils.core import setup

import sys

packages=['upy',  'upy.blender', 'upy.dejavuTk',
          'pythonUI']

# Check for Python2
if sys.version_info[0] == 2:
    packages.extend(['upy.autodeskmaya', 'upy.blender.v249','upy.cinema4d', 'houdini'])
elif sys.version_info[0] == 3:
    packages.extend(['upy.blender.v257', 'upy.blender.v262'])

setup(name='upy',
      version='1.0',
      description='uibiquitist UI',
      author='Ludovic Autin',
      author_email='autin@scripps.edu',
      url='https://github.com/corredD/pyubic',
      packages=packages,
      # 'upy.autodeskmaya',],
      package_dir={'upy': '.'},
     )
