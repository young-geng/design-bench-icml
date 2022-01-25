from setuptools import find_packages
from setuptools import setup


F = 'README.md'
with open(F, 'r') as readme:
    LONG_DESCRIPTION = readme.read()


setup(name='design-bench', version='2.0.20', license='MIT',
      packages=find_packages(incluBde=['design_bench', 'design_bench.*']),
      description='Design-Bench: Benchmarks for '
                  'Data-Driven Offline Model-Based Optimization',
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      author='Design Bench Authors',
      author_email='',
      keywords=['Deep Learning', 'Neural Networks',
                'Benchmark', 'Model-ased Optimization'],
      extras_require={'all': ['gym[mujoco]'], 'cma': ['cma']},
      install_requires=['pandas', 'requests', 'scikit-learn',
                        'torch', 'torchvision', 'numpy',
                        'tensorflow>=2.2', 'transformers',
                        'tokenizers', 'deepchem'],
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8'])
