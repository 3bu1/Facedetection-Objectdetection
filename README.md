# Facedetection-Objectdetection
Object detection using an IP camera. This project can take a video url (http://xxxxxxx.com)  as input and can predict the object/face/pattern.

### Dependencies
Python3, tensorflow 1.4 , numpy, opencv 3, darkflow


It is  a fork of darkflow project on github,Read more about YOLO (in darknet/darkflow) and download weight files <a href="https://pjreddie.com/darknet/yolo/">here</a>. 

For more information on Trainning custom models, cfg modification etc, u can get it from https://github.com/3bu1/darkflow/blob/master/README.md


### Installation:

Clone <a href="https://github.com/3bu1/Facedetection-Objectdetection">https://github.com/3bu1/Facedetection-Objectdetection</a>

For installing i would be using conda package manager as it can create a customised environment for our project with different versioned python packages. Just to avoid package version conflict, which i faced a lot.

#### Create conda virtual env for the project

```conda create -n py3.5 python=3.5```

#### Access new environment</br>
```source activate py3.5```

#### Install dependencies (no prob if they are already installed, conda will just skip them)
```conda install tensorflow cython numpy```

#### Add the repo with the magic opencv version
```conda config --add channels conda-forge```

#### Install magic opencv
```conda install opencv```

With a clean cloned repo run the setup (this was a problem, my previous attempts had left dirty lib files around so re-running the setup wouldn’t clean up beforehand and continued to use the dirty libs)

```python3 setup.py build_ext --inplace```

Download both CFG and and WEIGHTS files of the model you’ll use and place them in their respective folders (create the bin/ folder for weights). If they don’t match you’ll get errors.
Everything should work now!!!
You should see now (py3.5) just before ur machine name in terminal.

### Generate Annotaions for custom dataset

Change dataset names to our labels
```python3 generateDataSet/renameFile.py```

In order to train our models we will be generating annotion files for our collected dataset.To run
```python3 generateDataSet/drawbox.py ```



### Now Lets Jump in to the usage of IP camera modules.

#### main.py
Lets see folder liveStreaming, This folder helps in streaming a video over IP camera, just in case if u want to use web camera 

```python3 liveStreaming/main.py```

This should stream VideoCamera over your local ip, check localhost:5000/video_feed

#### app.py
Here we give our camera ip address to check with our AI if the pattern is matached or not.
Run app.py with 

```python3 app.py```

Dont forget to change the cfg and weight files in the program, If u trained your own dataset then need to add new weights to bin folder and respective cfg file in cfg folder.
