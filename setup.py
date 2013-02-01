#!/usr/bin/python

from setuptools import setup, find_packages

LICENSE = """Copyright 2012 Brown University, Providence, RI.

              All rights reserved.                           

              Permission to use, copy, modify, and distribute this software and its
              documentation for any purpose other than its incorporation into a commercial
              product is hereby granted without fee, provided that the above copyright notice
              appears in all copies and that both that copyright notice and this permission
              notice appear in supporting documentation, and that the name of Brown University
              not be used in advertising or publicity pertaining to distribution of the
              software without specific, written prior permission.
	
              BROWN UNIVERSITY DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
              INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR ANY
              PARTICULAR PURPOSE. IN NO EVENT SHALL BROWN UNIVERSITY BE LIABLE FOR
              ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER
              RESULTING FROM LOSS OF USE, DATA, OR PROFITS, WHETHER IN AN
              ACTION OF CONTRACT, NEGLIGENCE, OR OTHER TORTIOUS ACTION, ARISING OUT OF
              OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE."""

setup(name='Multi-Dendrix',
	  version='1.0',
	  description='Python implemention of Multi-Dendrix algorithm',
	  author='Max Leiserson',
	  license=LICENSE,
	  author_email='multi-dendrix@cs.brown.edu',
	  url='http://compbio.cs.brown.edu/projects/multi-dendrix',
	  requires=['networkx', 'scipy', 'cplex'],
	  packages=find_packages()
	  )