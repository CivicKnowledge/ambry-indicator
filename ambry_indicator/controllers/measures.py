# -*- coding: utf-8 -*-
#
# Copyright 2016 Civic Knowledge. All Rights Reserved
# This software may be modified and distributed under the terms of the BSD license.  
# See the LICENSE file for details.

from . import jsonify

def find_measure(name = None, tag = None, id = None, search = None):
    return 'do some magic!'


def get_indicator(id):
    
  
    return jsonify({
      "role": "Indicator",
      "vid": id,
      "data": [ [j for j in range(10) ] for i in range(10) ]
    })
    

def get_measure(id):
    return 'do some magic!'


def list_measures():
    return 'do some magic!'

def reduce_indicator(id):
    return 'do some magic!'