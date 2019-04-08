from setuptools import setup


requirements = ['pyglet',]

setup(
    name='minecraft',
    author='Tihran Katolikian (core by Michael Fogleman)',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'run_minecraft=minecraft.main:main'
        ]
    }
)
