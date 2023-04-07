from setuptools import setup, find_packages
import lablegen
setup(
	name="lablegen",
	version=lablegen.__version__,
	description="Generate LaTeX format table from array data.",
	url="https://github.com/Social-Mean/LableGen",
	author=lablegen.__author__,
	author_email="Social_Mean@126.com",
	license='GNU 3.0',
	py_modules = [ 'lablegen' ],
	scripts=['lablegen.py'],
  	classifiers=[
	  "Programming Language :: Python :: 3",
	  "License :: OSI Approved :: GNU Affero General Public License v3",
	  "Operating System :: OS Independent",
	  ],
	install_requires=['pyperclip',
                      'numpy',                     
                      ],
	)