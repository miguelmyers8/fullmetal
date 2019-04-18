from distutils.core import setup
from Cython.Build import cythonize

setup(name='fullmetal',
      version='0.1',
      description='neural network library',
      url='https://github.com/miguelmyers8/fullmetal',
      author='Miguel Myers',
      author_email='miguelmyers8@gmail.com',
      license='MIT',
      packages=['fullmetal'],
      ext_modules=cythonize('fullmetal/utils/*.pyx')
      )
