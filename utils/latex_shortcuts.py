#!/usr/bin/env python
# -*- coding: utf-8 -*-


def section(s):
    return "\n\\section*{" + s + "}\n"


def hiddenToc(s):
    return (
        """
    \n\\section*{}
    \\addcontentsline{toc}{section}{"""
        + s
        + """}
    \\vspace{-4em}
    """
    )


def cite(b):
    return "\\cite{" + b + "} "


def par():
    return "\\par\n"


def clearpage():
    return "\\clearpage\n"


def centering():
    return "\\centering"


def hspace(n):
    return "\\hspace{" + n + "}"


def vspace(n):
    return "\\vspace{" + n + "}"


def input(n):
    return "\n\\input{" + n + "}\n"


def figure_fullwidth(path, caption=""):
    block = (
        """
    \\begin{center}
    \\begin{figure}[!htb]
        \\caption{"""
        + caption
        + """}
        \\includegraphics[width=\\textwidth]{"""
        + path
        + """}
    \\end{figure}
    \\end{center}
    """
    )
    return block


def figure_squeeze(path, caption=""):
    block = (
        """
    \\hspace{-0.7in}
    \\begin{center}
    \\begin{figure}[!htb]
        \\caption{"""
        + caption
        + """}
        \\includegraphics[width=.7\\textwidth]{"""
        + path
        + """}
    \\end{figure}
    \\end{center}
    """
    )
    return block


def figure_twopanel(path1, path2, caption1="", caption2=""):
    block = (
        """
    \\begin{figure}[ht!]
    \\centering
    \\begin{subfigure}{.5\\textwidth}
        \\centering
        \\includegraphics[width=.8\\linewidth]{"""
        + path1
        + """}
        \\caption{"""
        + caption1
        + """}
    \\end{subfigure}%
    \\begin{subfigure}{.5\\textwidth}
        \\centering
        \\includegraphics[width=.8\\linewidth]{"""
        + path2
        + """}
        \\caption{"""
        + caption1
        + """}
    \end{subfigure}
    \\end{figure}
    """
    )
    return block


if __name__ == "__main__":
    print("This is just a collection of shortcuts. Nothing to show")
