#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np


def johnson_2_machines(t_ij):
    t_ij_opt = np.zeros(t_ij.shape)
    left_threshold = 0
    right_threshold = t_ij.shape[1] - 1
    threshold = np.max(t_ij[1:, :]) + 1

    while True:
        min_tab = [np.min(t_ij[1:, :]), list(np.argwhere(t_ij[1:, :] == np.min(t_ij[1:, :])))]

        for elem in min_tab[1]:
            if elem[0] == 0:
                t_ij_opt[:, left_threshold] = t_ij[:, elem[1]]
                left_threshold += 1
            elif elem[0] == 1:
                t_ij_opt[:, right_threshold] = t_ij[:, elem[1]]
                right_threshold -= 1
            t_ij[0, elem[1]] = 0
            t_ij[1:, elem[1]] = threshold

        if np.all(t_ij[0, :] == 0):
            break

    T_ij = np.zeros(t_ij.shape)
    T_ij[0, :] = t_ij_opt[0, :]

    for row in range(1, t_ij.shape[0]):
        for col in range(t_ij.shape[1]):
            if row == 1 and col == 0:
                T_ij[row, col] = t_ij_opt[row, col]
            elif row == 2 and col == 0:
                T_ij[row, col] = T_ij[1, 0] + t_ij_opt[row, col]
            elif row == 1 and col != 0:
                T_ij[row, col] = T_ij[1, col-1] + t_ij_opt[row, col]
            elif row == 2 and col != 0:
                T_ij[row, col] = max(T_ij[2, col - 1], T_ij[1, col]) + t_ij_opt[row, col]

    return T_ij


if __name__ == '__main__':
    m = np.array([[1, 2, 3, 4, 5, 6],
                  [9, 6, 8, 7, 12, 3],
                  [7, 3, 5, 10, 4, 7]])

    print(johnson_2_machines(m))