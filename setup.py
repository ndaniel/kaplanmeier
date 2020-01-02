import setuptools
import versioneer
new_version='0.1.1'
# conda install pytorch torchvision
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     install_requires=['matplotlib','numpy','pandas','seaborn','lifelines'],
     python_requires='>=3',
     name='kaplanmeier',
     version=new_version,
#     version=versioneer.get_version(),    # VERSION CONTROL
#     cmdclass=versioneer.get_cmdclass(),  # VERSION CONTROL
     author="Erdogan Taskesen",
     author_email="erdogant@gmail.com",
     description="Create survival curves using kaplanmeier, the log-rank test and making plots.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/erdogant/kaplanmeier",
	 download_url = 'https://github.com/erdogant/kaplanmeier/archive/'+new_version+'.tar.gz',
     packages=setuptools.find_packages(), # Searches throughout all dirs for files to include
     include_package_data=True, # Must be true to include files depicted in MANIFEST.in
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
