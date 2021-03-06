# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
import logging
from rest_framework.renderers import JSONRenderer
from rest_framework.utils import encoders
from enum import Enum

LOG = logging.getLogger(__name__)


class ExtJSONEncoder(encoders.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        return super(ExtJSONEncoder, self).default(obj)


def apply_monkeypatch():
    if JSONRenderer.encoder_class is encoders.JSONEncoder:
        JSONRenderer.encoder_class = ExtJSONEncoder
        LOG.info("`JSONRenderer.encoder_class` patched.")
