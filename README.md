Chaotic Double Pendulum
=======================

This code is for visualizing a collection of double pendulums with slightly different initial conditions.

Based on some code found at https://scipython.com/blog/the-double-pendulum/

Requirements
============

- Python >=3.6
- numpy
- scipy
- matplotlib
- tqdm

Use
===

``python simulate --simulation-time <t> --num-pendulums <n> --fps <fps> --noise-scale <s>``

Each frame will be saved as a separate image in a ``./frames`` directory.

Note that the plotting in particular could be optimized, and will be quite slow for more than 10 pendulums.

If you're using linux and have ffmpeg installed, you can combine these images
into a video using the provided ``./make_video.sh`` script.