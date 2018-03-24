# Facedetection-Objectdetection
Object detection using an IP camera. This project can take a video url (http://xxxxxxx.com)  as input and can predict the object/face/pattern.

<h3>Dependencies</h3>
Python3, tensorflow , numpy, opencv 3, darkflow


It is  a fork of darkflow project on github,Read more about YOLO (in darknet/darkflow) and download weight files <a href="https://pjreddie.com/darknet/yolo/">here</a>. So now I cloned:

<a href="https://github.com/thtrieu/darkflow">https://github.com/thtrieu/darkflow</a>

Installation:</br>
<b>Clone</b> <a href="https://github.com/thtrieu/darkflow">https://github.com/thtrieu/darkflow</a>

For installing i would be using conda package manager as it can create a customised environment for our project with different versioned python packages. Just to avoid package version conflict, which i faced a lot.

Create conda virtual env for the project</br>
<b>conda create -n py3.6 python=3.6</b>

Access new environment</br>
<b>source activate py3.6</b>

Install dependencies (no prob if they are already installed, conda will just skip them)</br>
<b>conda install tensorflow cython numpy</b>

Add the repo with the magic opencv version</br>
<b>conda config --add channels conda-forge</b>

Install magic opencv</br>
<b>conda install opencv</b>

With a clean cloned repo run the setup (this was a problem, my previous attempts had left dirty lib files around so re-running the setup wouldn’t clean up beforehand and continued to use the dirty libs)</br>
<b>python3 setup.py build_ext --inplace</b>

Download both CFG and and WEIGHTS files of the model you’ll use and place them in their respective folders (create the bin/ folder for weights). If they don’t match you’ll get errors.
Everything should work now!!!
You should see now (py3.6) just before ur machine name in terminal.

<div style="font-size:14px;">Now Lets Jump in to the usage of IP camera modules.</div>
<h4>liveStreaming/main.py</h4>
<p>Lets see folder liveStreaming, This folder helps in streaming a video over IP camera, just in case if u want to use web camera.</p>
<p>In this folder run main.py, <b>python3 main.py</b>This should stream VideoCamera over your local ip, check localhost:5000/video_feed</p>

<h4>app.py</h4>
<p>Here we give our camera ip address to check with our AI if the pattern is matached or not.Run app.py with python3 app.py, dont forget to change the cfg and weight files in the program, If u trained your own dataset then need to add new weights to bin folder and respective cfg file in cfg folder.</p>
