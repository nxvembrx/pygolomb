# pygolomb

Simple GUI tool for testing pseudorandom sequences for conformity with [Golomb’s randomness postulates](https://www.iitg.ac.in/pinaki/Golomb.pdf)

Welcome to the program for verifying binary sequences for conformity with Golomb’s randomness postulates! Each tab has a short information about each of three postulates. Also there's an ability to enter the sequence yourself or load it from a file. You can store resulting information in a file to show it to the professor or save for later use.

This program was developed as part of the course work in my second year of uni. Feel free to use it to learn about Golomb’s randomness postulates or modify it to your liking.

Warning! When I wrote this, I was very young and stupid and knew nothing about things like dependency management. One of the caveats of this is that you will have to install dependencies yourself. Maybe I will refactor it someday but maybe not.

## Running

Creating venv and installing dependencies.

```
python3 -m venv .venv
. .venv/bin/activate
poetry install
```

## Testing

```
. .venv/bin/activate
pytest
```

To check test coverage:

```
pytest --cov=pygolomb tests/
```
