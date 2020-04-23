# -*- coding: utf-8 -*-
"""Este archivo extrae una lista de apellidos
de la pagina de genealogiasdecolombia.co"""

import requests as rqs
import string as st
from bs4 import BeautifulSoup as bs
import re
from unicodedata import normalize
import csv

abcdario = st.ascii_uppercase


def obtener_apellidos():
    todos_apellidos = []
    for i in range(len(abcdario)):
        url = f'https://www.genealogiasdecolombia.co/apellidos/?l={abcdario[i]}'
        pagina = rqs.get(url)
        sopa = bs(pagina.text, 'lxml')
        secciones = sopa.find('div', attrs={'id': 'Myproducts'}) \
            .find_all('div', attrs={'class': 'box photo col2'})
        apellidos = [seccion.a.get_text() for seccion in secciones]
        apellidos = [x.lower() for x in apellidos]
        todos_apellidos.append(apellidos)
    return todos_apellidos


def funcion(apellidos):
    nms = apellidos

    f = open('numbers3.csv', 'w')
    with f:
        writer = csv.writer(f)
        writer.writerows(nms)
    print(writer)


def transformar():
    apellidos = obtener_apellidos()

    for i in range(len(apellidos)):
        for u in range(len(apellidos[i])):
            apellidos[i][u] = re.sub(
                r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
                normalize("NFD", apellidos[i][u]), 0, re.I
            )
    return apellidos


funcion(transformar())
