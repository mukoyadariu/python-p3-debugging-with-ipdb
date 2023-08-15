#!/usr/bin/env python3

from ipdb_debugging import plus_two
from lib import ipdb_debugging

class TestIpdbDebugging:
    '''ipdb_debugging.py'''
    
    def test_adds_two(self):
        '''adds_two() adds 2 to input arg and returns sum.'''
        assert(plus_two(3) == 5)
        
        ipdb_debugging.plus_two(5)
