# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Globex Corporation
# All rights reserved.
#
from connect_ext.events import OcrProjEventsApplication


def test_handle_asset_purchase_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_purchase_request_processing(request)
    assert result.status == 'success'


def test_handle_tier_config_adjustment_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_config_adjustment_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_change_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_change_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_adjustment_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_adjustment_request_processing(request)
    assert result.status == 'success'


def test_handle_tier_config_setup_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_config_setup_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_resume_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_resume_request_processing(request)
    assert result.status == 'success'


def test_handle_tier_account_update_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_account_update_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_suspend_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_suspend_request_processing(request)
    assert result.status == 'success'


def test_handle_tier_config_change_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_config_change_request_processing(request)
    assert result.status == 'success'


def test_handle_usage_file_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_usage_file_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_cancel_request_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_cancel_request_processing(request)
    assert result.status == 'success'


def test_handle_asset_change_request_validation(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_change_request_validation(request)
    assert result.status == 'success'
    assert result.body == request


def test_handle_product_custom_event_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_product_custom_event_processing(request)
    assert result.status == 'success'
    assert result.body == request


def test_handle_asset_purchase_request_validation(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_asset_purchase_request_validation(request)
    assert result.status == 'success'
    assert result.body == request


def test_handle_product_action_execution(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_product_action_execution(request)
    assert result.status == 'success'
    assert result.body == request


def test_handle_tier_config_change_request_validation(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_config_change_request_validation(request)
    assert result.status == 'success'
    assert result.body == request


def test_handle_tier_config_setup_request_validation(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.handle_tier_config_setup_request_validation(request)
    assert result.status == 'success'
    assert result.body == request


def test_execute_scheduled_processing(
    connect_client,
    client_mocker_factory,
    logger,
):
    config = {}
    request = {'id': 1}
    ext = OcrProjEventsApplication(connect_client, logger, config)
    result = ext.execute_scheduled_processing(request)
    assert result.status == 'success'
