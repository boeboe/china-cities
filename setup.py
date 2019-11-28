"""Package setup """
from setuptools import setup

def readme():
    """Readme """
    with open('README.md') as readme_file:
        return readme_file.read()

setup(name='china_cities',
      version="0.0.1",
      description='Python package to get the names of Chinese cities and provinces',
      long_description=readme(),
      author="Bart Van Bos",
      author_email='bartvanbos@gmail.com',
      license='MIT',
      url='https://github.com/boeboe/china-cities',
      packages=['china_cities'],
      keywords='china chinese cities provinces',
      zip_safe=False,
      classifiers=[
                    'Development Status :: 5 - Production/Stable',
                    'Intended Audience :: Developers',
                    'Natural Language :: English',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.5',
                    'Programming Language :: Python :: 3.6',
                    'Programming Language :: Python :: 3.7',
                    'Programming Language :: Python :: 3 :: Only',
                    'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      test_suite='tests',
      tests_require=['unittest']
      )
