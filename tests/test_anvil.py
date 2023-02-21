# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Globex Corporation
# All rights reserved.
#
from connect_ext.anvil import OcrProjAnvilApplication


def test_example_method(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    anvil_app = OcrProjAnvilApplication(connect_client, logger, config)
    assert anvil_app.example_method('an_argument') == (
        'Example method invoked, argument = an_argument'
    )
