#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

import pprint


sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

#  здесь заполнение словаря

moskow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moskow_london = ((moskow[0] - london[0])**2 + (moskow[1] - london[1])**2)**0.5
moskow_paris = ((moskow[0] - paris[0])**2 + (moskow[1] - paris[1])**2)**0.5
london_paris = ((london[0] - paris[0])**2 + (london[1] - paris[1])**2)**0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moskow_london
distances['Moscow']['Paris'] = moskow_paris
distances['london'] = {}
distances['london']['Moscow'] = moskow_london
distances['london']['Paris'] = london_paris
distances['Paris'] = {}
distances['Paris']['Moscow'] = moskow_paris
distances['Paris']['London'] = london_paris

pprint.pprint(distances)
