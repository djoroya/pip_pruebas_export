from setuptools import setup, find_packages

if __name__ == '__main__':
  setup( name='my_package_export',
        description='My package export',
          version='0.1',
          packages=find_packages(),
          install_requires=['numpy', 'scipy', 'matplotlib',
                            "my_package @ git+https://github.com/djoroya/pip_prueba.git"],
          author='Deyviss Jesús Oroya-Villalta',
          license='MIT',
          url='https://github.com/djoroya/pip_pruebas_export',
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