import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='siak-schedule-scrapper',  
     version='1.0',
     scripts=['siak-schedule-scrapper'] ,
     author="samuelmjn",
     author_email="smjn.samuel@gmail.com",
     description="Unofficial SIAKNG Scrapper",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/samuelmjn/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )