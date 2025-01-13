# OpenCV_Course
Code from following along this [OpenCV Course](https://www.youtube.com/watch?v=oXlwWbU8l2o).

## Packages

Packages Needed:
```
pip install opencv-contrib-python
pip install caer
pip install matplotlib
pip install canaro
```

In order for tensorflow to detect the GPU:
```
pip uninstall tensorflow
pip install tensorflow[and-cuda]
```

At some point, `LBPHFaceRecognizer_create` wasnt working, so I uninstalled and reinstalled packages as such:
```
pip uninstall opencv-python
pip uninstall opencv-python-headless
pip uninstall opencv-contrib-python
pip uninstall caer

pip install opencv-contrib-python
pip install caer
```

## Links
- https://www.tensorflow.org/install/pip#linux_setup

Neural Network Explainations:
- https://setosa.io/ev/image-kernels/
- https://poloclub.github.io/cnn-explainer/

![Convulution Explaination Image](convulution_explaination.png)