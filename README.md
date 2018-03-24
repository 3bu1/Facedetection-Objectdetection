# Facedetection-Objectdetection
Object detection using an IP camera. This project can take a video url (http://xxxxxxx.com)  as input and can predict the object/face/pattern. 


It is  a fork of darkflow project on github. So now I cloned:

<a href="https://github.com/thtrieu/darkflow">https://github.com/thtrieu/darkflow</a>

Installation:</br>
Clone <a href="https://github.com/thtrieu/darkflow">https://github.com/thtrieu/darkflow</a>

For installing i would be using conda package manager as it can create a customised environment for our project with different versioned python packages. Just to avoid package version conflict, which i faced a lot.

Create conda virtual env for the project</br>
<b>conda create -n py3.6 python=3.6</b>

Access new environment</br>
<b>source activate py3.6</b>

Install dependencies (no prob if they are already installed, conda will just skip them)
<b>conda install tensorflow cython numpy</b>

Add the repo with the magic opencv version</br>
<b>conda config --add channels conda-forge</b>

Install magic opencv</br>
<b>conda install opencv</b>

With a clean cloned repo run the setup (this was a problem, my previous attempts had left dirty lib files around so re-running the setup wouldn’t clean up beforehand and continued to use the dirty libs)</br>
<b>python3 setup.py build_ext --inplace</b>

Download both CFG and and WEIGHTS files of the model you’ll use and place them in their respective folders (create the bin/ folder for weights). If they don’t match you’ll get errors.
Everything should work now!!!




