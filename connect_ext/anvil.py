# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Globex Corporation
# All rights reserved.
#
from connect.eaas.core.decorators import anvil_callable, anvil_key_variable, variables
from connect.eaas.core.extension import AnvilApplicationBase


@anvil_key_variable('ANVIL_API_KEY')
@variables([{
    'name': 'VAR_NAME_1',
    'initial_value': 'VAR_VALUE_1',
    'secure': False,
}])
class OcrProjAnvilApplication(AnvilApplicationBase):
    @anvil_callable(
        summary='This is an example method',
        description='This method is just an example.',
    )
    def example_method(self, example_argument):
        return f'Example method invoked, argument = {example_argument}'
