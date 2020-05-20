from sys import exit
try:
    import setuptools
except:
    from sys import stdout
    stdout.write('''
setuptools not found. Please install it.

On linux, the package is often called python-setuptools\n''')
    exit(1)

exec(compile(open('safeout/safeout_version.py').read(), 'safeout/safeout_version.py', 'exec'))
long_description = open('README.md').read()

classifiers = [
'License :: OSI Approved :: MIT License',
'Operating System :: POSIX',
'Operating System :: OS Independent',
'Programming Language :: Python',
]

setuptools.setup(name = 'Safeout',
      version = __version__,
      description = 'Write out a file safely (atomically)',
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      author = 'Luis Pedro Coelho',
      author_email = 'luis@luispedro.org',
      license = 'MIT',
      platforms = ['Any'],
      classifiers = classifiers,
      packages = setuptools.find_packages(),
      test_suite = 'nose.collector',
      )


