from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pynput"]

setup(
    name="2_keys_for_equipement_launcher",
    version="1",
    author="Pedro-Beirao",
    author_email="pedrocbeirao@gmail.com",
    description="A 'mod' to have seperate keys for each grenade in Doom Eternal",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="doom eternal python3 mod",
    url="https://github.com/Pedro-Beirao/2_keys_for_equipement_launcher/",
    scripts=["doomhack.py"],
    packages=[],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
