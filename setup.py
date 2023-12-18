from setuptools import setup, find_packages

if __name__ == '__main__':
  setup( name='my_package',
        description='My package',
          version='0.1',
          packages=find_packages(),
          install_requires=['numpy', 'scipy', 'matplotlib'],
          author='Deyviss Jesús Oroya-Villalta',
          license='MIT',
          url='https://github.com/djoroya/pip_prueba_import',
          classifiers=[
              'Development Status :: 1 - Planning',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: MIT License',
              'Programming Language :: Python :: 3.6',
              'Topic :: Scientific/Engineering :: Atmospheric Science',
              'Topic :: Scientific/Engineering :: Physics',
              'Topic :: Scientific/Engineering :: Visualization',
              'Topic :: Software Development :: Libraries :: Python Modules',
          ],
          keywords='my_package',
          )