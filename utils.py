from fractions import Fraction as frac
import numpy as np


def convert_to_frac(mat):
    result = []
    mat_list = mat.astype(str).tolist()
    for i in range(0, len(mat_list)):
        result.append([])
        for j in range(0, len(mat_list[i])):
            result[i].append(
                str(frac(str(mat_list[i][j])).limit_denominator(10)))
    return result


def convert_to_latex(mat):
    mat_list = convert_to_frac(mat)
    mat_list_rows = list(map(r" & ".join, mat_list))
    mat_latex_content = r" \\\ ".join(mat_list_rows)
    return mat_latex_content
