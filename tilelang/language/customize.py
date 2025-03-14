# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
"""The language interface for tl programs."""

from tvm.script import tir as T
from tvm.tir import PrimExpr


def atomic_add(dst, value):
    return T.call_extern("handle", "AtomicAdd", T.address_of(dst), value)


def atomic_addx2(dst, value):
    return T.call_extern("handle", "AtomicAddx2", T.address_of(dst), T.address_of(value))


def dp4a(A, B, C):
    return T.call_extern("handle", "DP4A", T.address_of(A), T.address_of(B), T.address_of(C))


def clamp(dst, min_val: PrimExpr, max_val: PrimExpr):
    dst = T.max(dst, min_val)
    dst = T.min(dst, max_val)
    return dst
