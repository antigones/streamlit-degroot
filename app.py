import streamlit as st
import numpy as np
from numpy.linalg import matrix_power
import pandas as pd
import deGroot as dg
import networkx as nx
import graphviz as graphviz

import utils as u


st.title("DeGroot")
st.write("DeGroot gives an insight about how network topology influence spread of information and opinion formation.It also gives an intuition about the reason why eigenvector centrality expresses influence.")
st.write("Move the slide to inspect the belief vector as it updates according to DeGroot model.")

p0 = np.matrix([1, 0, 0]).T
T = np.matrix([[1/3, 1/3, 1/3], [1/2, 1/2, 0], [0, 1/4, 3/4]])

dg_steps = dg.deGrootSteps(T, p0)

step = st.slider('Step', 0, len(dg_steps)-1, 0)
st.write("Step: ", step, '')

G = nx.from_numpy_matrix(T, create_using=nx.MultiDiGraph())
dot = nx.nx_pydot.to_pydot(G)

chart_data = pd.DataFrame(dg_steps[step])

ltx_mat = u.convert_to_latex(T)
b_mat = u.convert_to_latex(dg_steps[step])
p0_mat = u.convert_to_latex(p0)

col1, col2 = st.beta_columns(2)

with col1:
    st.graphviz_chart(dot.to_string())
with col2:
    st.bar_chart(chart_data)

col3, col4, col5 = st.beta_columns(3)
with col3:
    st.latex(r'''
        T =
        \begin{pmatrix}
        '''+ltx_mat+r'''
        \end{pmatrix}
        ''')
with col4:
    st.latex(r'''
        p(0) =
        \begin{pmatrix} ''' + p0_mat + r'''\end{pmatrix}
        ''')
with col5:
    st.latex(r'''
        T^{t}p(0) {\rightarrow}
        \begin{pmatrix}
        ''' + b_mat + r'''
        \end{pmatrix}
        ''')

st.title("Convergence of T")

T_t = np.linalg.matrix_power(T, step+1)
T_t_mat = u.convert_to_latex(T_t)

st.latex(r'''
    T^{t} {\rightarrow}
    \begin{pmatrix}
    ''' + T_t_mat + r'''
    \end{pmatrix}
	''')
