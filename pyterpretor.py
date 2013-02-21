#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import os
import imp
from os import system as sh

'''
File: pyterpretor.py
Author : Santosh Kumar <https://twitter.com/sntshk>
Date created: Wed 20 Feb 2013 09:23:46 PM IST
Description: Inspired by interactive_editor rubygem which allowed user to
             open up a text editor in Ruby interpreter.
'''

def _vim(fname, globs):
    sh('vim ' + fname)
    (dirname, _, basename) = fname.rpartition('/')
    modname = basename.rpartition('.')[0]
    m = imp.load_source(modname, fname)
    globs[modname] = m
