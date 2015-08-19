# pyterpretor
pyterpretor, pronounced as **pi-ter-prator** is an integration between Python interpreter and vim (capable of other editors as well) which lets edit python files from inside python interpreter. The code inside the file is executed as soon as you exit the editor. It was inspired by **interactive_editor** rubygem in Ruby interpreter.


## Installation

Put the following lines in your shell's configuration file:

    export PYTHONSTARTUP=/path/to/pyterpretor.py

## Usages

Edit any file like this:

    >>> vim('filename.py')

Code in filename.py will be executed as soon as you exit the editor.

## To do
 * Make it a pip candidate
 * Make it work for other editors (DRY)

## Contributers
You are most welcome to contribute to this project. Here are the contributors:

 * [santosh][2] *([Twitter][1])*

   [1]: https://twitter.com/sntshk
   [2]: https://github.com/santosh
