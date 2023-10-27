#!/usr/bin/env python
# coding: utf-8

import time
import logging
from typing import Dict, Any, List  # noqa: F401

from testing_config import BaseTestConfig
from xrpld_netgen.main import create_network

logger = logging.getLogger("app")


class TestNetGen(BaseTestConfig):
    def test_init(cls):
        create_network(
            "ED87E0EA91AAFFA130B78B75D2CC3E53202AA1BD8AB3D5E7BAC530C8440E328501",
            "A232AD54A29466CDE4A3D99C651B332F89D25B5ACE3D8BD6ABD4748DA67159B2",
            "JAAAAAFxIe2H4OqRqv+hMLeLddLMPlMgKqG9irPV57rFMMhEDjKFAXMh7eP2BCI6nc9g/k66bj7ksWmKuwZOKJeFx1emXip6dXxCdkB/0p6s8BzkgY7AXQxJh47pGP+vVtgcVJ44y2FK9H7xMsGOhdrbl0KUWY1Y15ZHd/R/QmvLhNC05psAX1+76YkNcBJAytrEazBhxQAEZSSLkfLwNTj3MewH1l1BjZhuIARiJNzh90dkV6AFqFW2m9VyVNLJX8EKl6yau/NET8KV2oFhAQ==",
            "xahau",  # protocol
            "test",  # name
            3,  # num validators
            1,  # num peers
            21337,  # network id
            "dangell7-devnet-binary:2.0.0-b2",  # image name
        )
        print(ee)
