# -*- coding: utf-8 -*-
#
# Copyright 2016 Civic Knowledge. All Rights Reserved
# This software may be modified and distributed under the terms of the BSD license.
# See the LICENSE file for details.

import connexion
from os.path import dirname



app = connexion.App(__name__, specification_dir=dirname(__file__))
app.add_api('swagger.yaml', arguments={'title': 'Returns indicators from properly classified Ambry bundles. \n'})