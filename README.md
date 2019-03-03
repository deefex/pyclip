#### Introduction

This is a quick and simplified python 3.x rewrite of James Bach's original PerlCip tool which generates a counterstring with a length of your choosing. For those unfamiliar with the concept when you look at a counterstring it's easy to determine the character position by virtue of the markers. 

It can come in very handing when testing text fields where the strings may be truncated but you can still tell how many characters are in the string.

James's original tool, perlclip can be found [here](http://www.satisfice.com/tools.shtml), along with a counterstring blog post [here](http://www.satisfice.com/blog/archives/22).

#### Pre-Installation Requirements

This was written with python 3.7.2, so you'll need to ensure that you have that (or a later version) installed.
For more information on installing python, refer to [python.org](https://www.python.org/downloads/)

#### Installation (Easy)

Once you have python installed and have a virtualenv of your choice activated (optional), then you can simply pip install directly from github by running:

- `pip install git+https://github.com/deefex/pyclip.git` 

Or, if you prefer you can clone the repository and pip install locally:

- `git clone https://github.com/deefex/pyclip`
- `pip install ./pyclip`

Once this completes, you should be good to go.

#### Usage

The reason for 'pip installing' above was eliminate the pain of running python locally. 

No need to remember where the cloned directory is, which script to run, or the mandatory 'python' prefix. 

All you need to do is type: 

`pyclip [length]`

on the command line, and that's it, after which the counterstring will be automatically copied to your clipboard, ready to paste into whatever you need. 

The `length` parameter will default to 1000 if not supplied. It needs to be an integer and greater than 0.

#### Example Usage

- `pyclip` - Generates a counterstring with length 1000
- `pyclip 10` - Generates a counterstring with length 10

#### Counterstring Examples

The marker element (`*`) of the counterstring marks the position of the preceding number:

- `*3*5*7*10*` is a counterstring of length 10
- `2*4*6*8*11*` is a counterstring of length 11
- `2*4*6*8*11*14*17*20*23*26*29*32*35*` is a counterstring of length 35

Have fun!