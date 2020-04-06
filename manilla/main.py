#!/usr/bin/env python

import argparse
import shlex
import subprocess
import clipsvg
from collections import defaultdict

def main(main_file, formula_file):
    if formula_file is not None:
        header = []
        footer = ["\\end{document}"]
        formulae = defaultdict(list)
        current_formula = None
        with open(formula_file) as f:
            for line in f:
                line = line.strip()
                header.append(line)

                if line == "\\begin{document}":
                    break
            
            for line in f:
                line = line.strip()
                if line.startswith("%%START"):
                    name = line.split(":")[1]
                    current_formula = name
                    continue
                
                if line.startswith("%%END"):
                    name = line.split(":")[1]
                    if name != current_formula:
                        # TODO: turn this into a real error
                        print("START and END are not paired correctly.")
                        quit()
                    current_formula = None
                    continue
            
                if current_formula is not None:
                    formulae[current_formula].append(line)
        
            print(formulae)
        
        for name, formula in formulae.items():
            tmp_file = "/tmp/tmp.tex"

            with open(tmp_file, "w") as f:
                output = header + formula + footer
                f.write("\n".join(output) + "\n")
            
            # compile all tex documents to pdf
            subprocess.check_output(shlex.split("pdflatex -output-directory /tmp /tmp/tmp.tex"))

            # convert pdfs to svgs
            # inkscape -l <output>.svg <input>.pdf
            subprocess.check_output(shlex.split("pdftocairo -svg /tmp/tmp.pdf /tmp/tmp.svg"))

            # crop svgs
            clipsvg.clip_svg("/tmp/tmp.svg", f"./{name}.svg", 0)
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--formula_file",
        help = "location of the LaTeX formulae to render into SVGs",
        default = None
        )

    parser.add_argument("main_file",
        help = "main file to generate HTML document for",
        )
    
    args = parser.parse_args()

    main(args.main_file, args.formula_file)
