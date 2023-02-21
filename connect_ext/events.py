# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Globex Corporation
# All rights reserved.
#
from connect.eaas.core.decorators import (
    event,
    schedulable,
    variables,
)
from connect.eaas.core.extension import EventsApplicationBase
from connect.eaas.core.responses import (
    BackgroundResponse,
    InteractiveResponse,
    ScheduledExecutionResponse,
)


@variables([
    {
        'name': 'VAR_NAME_1',
        'initial_value': 'VAR_VALUE_1',
        'secure': False,
    },
    {
        'name': 'VAR_NAME_N',
        'initial_value': 'VAR_VALUE_N',
        'secure': True,
    },
])
class OcrProjEventsApplication(EventsApplicationBase):
    @event(
        'asset_purchase_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_purchase_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'tier_config_adjustment_request_processing',
        statuses=[
            'pending', 'failed', 'approved',
            'inquiring',
        ],
    )
    def handle_tier_config_adjustment_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_change_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_change_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_adjustment_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'inquiring', 'scheduled', 'revoking',
            'revoked',
        ],
    )
    def handle_asset_adjustment_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'tier_config_setup_request_processing',
        statuses=[
            'pending', 'failed', 'approved',
            'inquiring',
        ],
    )
    def handle_tier_config_setup_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_resume_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'scheduled', 'revoking', 'revoked',
        ],
    )
    def handle_asset_resume_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'tier_account_update_request_processing',
        statuses=[
            'pending', 'accepted', 'ignored',
        ],
    )
    def handle_tier_account_update_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_suspend_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'scheduled', 'revoking', 'revoked',
        ],
    )
    def handle_asset_suspend_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'tier_config_change_request_processing',
        statuses=[
            'pending', 'failed', 'approved',
            'inquiring',
        ],
    )
    def handle_tier_config_change_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'usage_file_request_processing',
        statuses=[
            'draft', 'uploading', 'uploaded',
            'invalid', 'processing', 'ready',
            'rejected', 'pending', 'accepted',
            'closed',
        ],
    )
    def handle_usage_file_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_cancel_request_processing',
        statuses=[
            'pending', 'approved', 'failed',
            'scheduled', 'revoking', 'revoked',
        ],
    )
    def handle_asset_cancel_request_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return BackgroundResponse.done()

    @event(
        'asset_change_request_validation',
        statuses=[
            'draft', 'inquiring',
        ],
    )
    def handle_asset_change_request_validation(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return InteractiveResponse.done(
            http_status=200,
            headers={'X-Custom-Header': 'value'},
            body=request,
        )

    @event('product_custom_event_processing')
    def handle_product_custom_event_processing(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return InteractiveResponse.done(
            http_status=200,
            headers={'X-Custom-Header': 'value'},
            body=request,
        )

    @event(
        'asset_purchase_request_validation',
        statuses=[
            'draft', 'inquiring',
        ],
    )
    def handle_asset_purchase_request_validation(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return InteractiveResponse.done(
            http_status=200,
            headers={'X-Custom-Header': 'value'},
            body=request,
        )

    @event('product_action_execution')
    def handle_product_action_execution(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return InteractiveResponse.done(
            http_status=200,
            headers={'X-Custom-Header': 'value'},
            body=request,
        )

    @event(
        'tier_config_change_request_validation',
        statuses=[
            'draft', 'inquiring',
        ],
    )
    def handle_tier_config_change_request_validation(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return InteractiveResponse.done(
            http_status=200,
            headers={'X-Custom-Header': 'value'},
            body=request,
        )

    @event(
        'tier_config_setup_request_validation',
        statuses=[
            'draft', 'inquiring',
        ],
    )
    def handle_tier_config_setup_request_validation(self, request):
        self.logger.info(f"Obtained request with id {request['id']}")
        return InteractiveResponse.done(
            http_status=200,
            headers={'X-Custom-Header': 'value'},
            body=request,
        )

    @schedulable('Schedulable method', 'It can be used to test DevOps scheduler.')
    def execute_scheduled_processing(self, schedule):
        self.logger.info(
            f"Received event for schedule  {schedule['id']}",
        )
        return ScheduledExecutionResponse.done()
