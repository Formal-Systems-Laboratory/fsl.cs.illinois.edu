`fsl.cs.illinois.edu`
=====================

This repo is used for generating the FSL static website.

Generating publication pages
============================

To generate publication pages, we use a python script.

After installing `python3`, install `pybtex` using `pip3`

    pip3 install --user pybtex

Next, run:

    _scripts/generate-papers <path/to/fsl/repo>
