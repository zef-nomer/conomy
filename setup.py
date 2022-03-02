import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='disnake_economy',  
     version='0.1',
     scripts=['disnake_economy'] ,
     author="Zef1rOK",
     author_email="evgehapavlov222@gmail.com",
     description="Economy module for disnake.py",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/zef-nomer/disnake-economy",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )