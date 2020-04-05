#!/usr/bin/env python

import argparse
from collections import defaultdict

def main(main_file, formula_file):
    if formula_file is not None:
        header = []
        formulae = defaultdict(list)
        current_formula = None
        with open(formula_file) as f:
            for line in f:
                line = line.strip()

                if line == "\\begin{document}":
                    break
                    
                header.append(line)
            
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

        # compile all tex documents to pdf
        # convert pdfs to svgs
        # crop svgs

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
