# Coding Challenge

## How to run the program
* Install the python package opencv-python in your system/ python virtual environment
* Go to the directory and run the programs by executing the following commands. Replace **python3** with the python command installed in your system. Both are independent of each other and are meant to be run seperately.

        python3 code.py
        python3 code2.py

* Close any windows that pop up and continue the execution by pressing any key on the keyboard.

## Two implementations
* ### code .py
    * Implementation based on simple parsing.
    * Accuracy better than the other implementation but still not perfect.
    * Results acheived using very narrow boundary conditions heavily dependent on particular pixel value thresholds. We might want to tweak these values/condiitons for other inputs to maximise accuracy.
    * **Results saved in *letters* directory**

* ### code2 .py
    * Initial approach.
    * Implementation based on techniques of thresholding and segmentation.
    * Not many variables involved in boundary conditions since the parsing is done in a thresholded image (because there are only two distinct pixel values present in the image after thresholding, 0 and 255).
    * Less accurate results.
    * **Results saved in *letters2* directory**
