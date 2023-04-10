"""Package setup """
from setuptools import setup
from china_cities import __version__

def readme():
    """Readme """
    with open('README.md') as readme_file:
        return readme_file.read()

setup(name='china_cities',
      version=__version__,
      description='Python package to get the names of Chinese cities and provinces',
      long_description=readme(),
      long_description_content_type='text/markdown',
      author="Bart Van Bos",
      author_email='bartvanbos@gmail.com',
      license='MIT',
      url='https://github.com/boeboe/china-cities',
      packages=['china_cities'],
      keywords='china chinese cities provinces',
      include_package_data=True,
      zip_safe=False,
      classifiers=[
                    'Development Status :: 5 - Production/Stable',
                    'Intended Audience :: Developers',
                    'Natural Language :: English',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 3',
                    "Topic :: Software Development :: Libraries :: Python Modules",
                    "Topic :: System :: Software Distribution"
      ],
      test_suite='tests',
      tests_require=['unittest']
      )
