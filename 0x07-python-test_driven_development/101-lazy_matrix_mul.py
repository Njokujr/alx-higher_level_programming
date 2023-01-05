#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Author: Victory Njoku
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix
    Args:
        m_a (list): First matrix
        m_b (list): second matrix
    Returns:
        The result of m_a,m_b
        """
    '''multipy 2 patrices with numpy'''
    return (np.matmul(m_a, m_b))
