from distutils.core import setup

setup(
    name='johnhancock',
    version='0.1',
    description='Sign a PDF using a PNG image',
    author='Brandon Rhodes',
    author_email='brandon@rhodesmill.org',
    #url='',
    packages=['johnhancock'],
    install_requires=['Pillow', 'pyPdf', 'reportlab'],
    )
