#!/usr/bin/env python2
#from distutils.core import setup
from setuptools import setup
from pdfminer import __version__
import subprocess

from distutils.command.bdist import bdist 

class PdfMinerInstall(bdist):
    def run(bdist):
        self.do_make()
        Command.run(self)

    def do_make(self):
        subprocess.call(["make","cmap"])

setup(
    name='pdfminer',
    version=__version__ + "-vayana",
    description='PDF parser and analyzer',
    long_description='''PDFMiner is a tool for extracting information from PDF documents.
Unlike other PDF-related tools, it focuses entirely on getting 
and analyzing text data. PDFMiner allows to obtain
the exact location of texts in a page, as well as 
other information such as fonts or lines.
It includes a PDF converter that can transform PDF files
into other text formats (such as HTML). It has an extensible
PDF parser that can be used for other purposes instead of text analysis.''',
    license='MIT/X',
    author='Yusuke Shinyama',
    author_email='yusuke at cs dot nyu dot edu',
    url='http://www.unixuser.org/~euske/python/pdfminer/index.html',
    cmdclass={'bdist': PdfMinerInstall},
    packages=[
    'pdfminer',
    'pdfminer.cmap',
    ],
    package_data={
    'pdfminer.cmap': ['*.pickle.gz'],
    },
    scripts=[
    'tools/pdf2txt.py',
    'tools/dumppdf.py',
    'tools/latin2ascii.py',
    ],
    keywords=['pdf parser', 'pdf converter', 'layout analysis', 'text mining'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Topic :: Text Processing',
    ],
    )
