from distutils.core import setup,Extension
from Cython.Build import cythonize

sourcefiles = ['src/spde/spde.pyx', 'src/spde/TurboOptimizer.cpp']

extensions = [Extension("spde", sourcefiles,language='c++')]


setup(name="spde",
	  version="0.0.1",
		author = 'Nicolas Desassis and Didier Renard',
		author_email = 'nicolas.desassis@gmail.com',
		url = 'https://github.com/NDesassis/spde', 
    ext_modules = cythonize(extensions)
)

