from setuptools import setup, find_packages

setup(
    name='quantinar_world_cloud_search',
    version='0.0.0',
    url='https://github.com/BrunoSpilak/quantinar-word-cloud-search',
    author='Bruno Spilak',
    author_email='bruno.spilak@gmail.com',
    dependency_links=[],
    python_requires='~=3.9',
    install_requires=[
        "numpy>=1.22.3",
        "pandas>=1.4.1",
        "PyPDF2>=2.1.0"
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    zip_safe=False,
    packages=find_packages()
)
