# ターミナルで, python setup.py sdist と打てば,
# ファイルがパッケージ化されて配布できます.
from distutils.core import setup

setup(
    name='python_programming',
    version='1.0.0',
    packages=['package', 'package.talk', 'package.tools'],
    url='https://github.com/solareenlo/python_practice',
    license='Free',
    author='solareenlo',
    author_email='',
    description='Sample package'
    )
