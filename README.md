# pyiocutils

A collection of utilities for use in Python scripts related to
working with "indicators of compromise" (IOCs). 

+ ioc.py - a set of static methods grouped under the "Ioc" class to check and handle indicators
+ iocfile.py - a class to instantiate to parse a plain-text file of IOCs
+ icargs.py - a static method to handle IOC arguments

Note: this is not a reference to Mandiant's IOC [XML-based file format](https://github.com/fireeye/iocs). This
is more a reference to individual domain or ip strings as well as text files containings lists of these
indicators. You know - the shit with which analysts actually work.

## Usage

Basic usage examples were created using [asciinema](https://asciinema.org/). If something is
still unclear, file an issue so I can make this package as easy-to-use as possible.

Using pyiocutils.ioc - [![asciicast](https://asciinema.org/a/217356.svg)](https://asciinema.org/a/217356)
Using pyiocutils.iocfile - [![asciicast](https://asciinema.org/a/217357.svg)](https://asciinema.org/a/217357)
Using pyiocutils.iocargs - [![asciicast](https://asciinema.org/a/217358.svg)](https://asciinema.org/a/217358)

## Installation

This package is not currently hosted on the Python Package Index.

```bash
> git clone https://github.com/cmatthewbrooks/pyiocutils.git
> cd pyiocutils
> pip install .
```

## TODO
 
+ Host this package on the Python Package Index
