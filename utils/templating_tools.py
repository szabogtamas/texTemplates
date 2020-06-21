#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, jinja2

dr = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/templates/"


def latex_jinja_env(dr=dr):
    # Settings adapted from http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs

    return jinja2.Environment(
        block_start_string="\BLOCK{",
        block_end_string="}",
        variable_start_string="\VAR{",
        variable_end_string="}",
        comment_start_string="\#{",
        comment_end_string="}",
        line_statement_prefix="%%",
        line_comment_prefix="%#",
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.abspath(dr)),
    )


def openTemplate(fn=None):
    if fn is None:
        fn = "ligthweight_report_template.tex"
    lenv = latex_jinja_env()
    template = lenv.get_template(fn)
    return template


if __name__ == "__main__":
    print("This is just a helper. Nothing to show")
