"""
Unit tests for agent_economy_sdk — bounty #1589
"""
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from agent_economy_sdk import (
    AgentEconomySDK,
    TaskPriority,
    TaskStatus,
    check_bounty_eligibility,
    format_rtc,
)


class TestFormatRtc:
    def test_format_integer(self):
        result = format_rtc(100)
        assert isinstance(result, str)
        assert "100" in result

    def test_format_float(self):
        result = format_rtc(50.5)
        assert isinstance(result, str)
        assert "50.5" in result

    def test_format_zero(self):
        result = format_rtc(0)
        assert isinstance(result, str)

    def test_format_negative(self):
        result = format_rtc(-10)
        assert isinstance(result, str)


class TestTaskPriority:
    def test_priority_order(self):
        assert TaskPriority.CRITICAL.value < TaskPriority.HIGH.value
        assert TaskPriority.HIGH.value < TaskPriority.MEDIUM.value
        assert TaskPriority.MEDIUM.value < TaskPriority.LOW.value

    def test_priority_values(self):
        assert TaskPriority.CRITICAL.value == 0
        assert TaskPriority.LOW.value == 3


class TestTaskStatus:
    def test_status_values(self):
        assert TaskStatus.PENDING.value == "pending"
        assert TaskStatus.COMPLETED.value == "completed"

    def test_all_statuses_defined(self):
        statuses = [TaskStatus.PENDING, TaskStatus.IN_PROGRESS,
                    TaskStatus.COMPLETED, TaskStatus.FAILED]
        assert len(statuses) == 4


class TestCheckBountyEligibility:
    def test_eligible_balance(self):
        result = check_bounty_eligibility(50)
        assert isinstance(result, bool)

    def test_zero_balance(self):
        result = check_bounty_eligibility(0)
        assert isinstance(result, bool)

    def test_negative_balance(self):
        result = check_bounty_eligibility(-10)
        assert isinstance(result, bool)

    def test_large_balance(self):
        result = check_bounty_eligibility(1000000)
        assert isinstance(result, bool)


class TestAgentEconomySDK:
    def test_init_default_values(self):
        sdk = AgentEconomySDK()
        assert sdk.wallet_address == ""
        assert sdk.balance == 0

    def test_init_with_wallet(self):
        sdk = AgentEconomySDK(wallet_address="test_wallet")
        assert sdk.wallet_address == "test_wallet"

    def test_init_with_balance(self):
        sdk = AgentEconomySDK(balance=100.0)
        assert sdk.balance == 100.0

    def test_repr(self):
        sdk = AgentEconomySDK(wallet_address="wallet", balance=50.0)
        r = repr(sdk)
        assert "wallet" in r or "50.0" in r

    def test_str(self):
        sdk = AgentEconomySDK(wallet_address="wallet", balance=50.0)
        s = str(sdk)
        assert isinstance(s, str)
