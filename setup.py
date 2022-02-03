from distutils.core import setup

setup(
  name = 'CombiParser',
  packages = ['CombiParser'],
  version = '0.2',
  license='MIT',
  description = 'A simple combinator parser.',
  author = 'Sam Harding',
  author_email = 'samueljames.harding@icloud.com',
  url = 'https://github.com/sam-james-harding/CombiParser',
  download_url = 'https://github.com/sam-james-harding/CombiParser/archive/v_02.tar.gz',
  keywords = ['Combinator Parser', 'Parser', 'Declarative'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
  ],
)