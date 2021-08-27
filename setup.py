from setuptools import find_packages
from setuptools import setup

setup(
    name="Bassline",
    version="0.0.1",
    url="https://github.com/bassline/bassline",
    author="Adrian Griffin",
    description="Use your Raspberry Pi as a browser-based KVM.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["eventlet", "Flask", "Flask-SocketIO", "Flask-WTF"],
    entry_points={"console_scripts": ["bassline = app.main:main"]},
)
