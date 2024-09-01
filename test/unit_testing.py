import pytest
# Add this at the beginning of your unit_testing.py to check where Python is searching for modules
import sys
import os

# Adjust this path according to the actual location of your 'vulnerabilities' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the vulnerability detection functions
from vulnerabilities.Broken_Authentication import check_broken_authentication
from vulnerabilities.Broken_Object_Level_Authorization import check_broken_object_level_authorization
from vulnerabilities.SQL_Injection import check_sql_injection
from vulnerabilities.Unrestricted_Resource_Consumption import check_unrestricted_resource_consumption
from vulnerabilities.BOPA import check_bopa
from vulnerabilities.SSRF import check_ssrf
from vulnerabilities.BFLA import check_bfla
from vulnerabilities.Check_xss import check_xss
from vulnerabilities.Unrestricted_business_flow import check_unrestricted_business_flow
from vulnerabilities.security_misconfig import check_security_misconfiguration
from vulnerabilities.improper_inventory_management import check_improper_inventory_management
from vulnerabilities.unsafe_api_usage import check_unsafe_api_usage

# from vulnerabilities import *
# SQL Injection Testing

@pytest.mark.parametrize("query, expected", [
    ("SELECT * FROM users WHERE user='admin';", False),
    ("SELECT * FROM users WHERE user=''; DROP TABLE users; --", True),
    ("SELECT * FROM users WHERE user='admin' OR '1'='1';", True),
    ("SELECT * FROM users WHERE user='admin' AND 'x'='x';", False),
])
def test_sql_injection(query, expected):
    assert check_sql_injection(query) == expected

# Usage in tests
@pytest.mark.parametrize("url, expected", [
    ("http://example.com", False),
    ("http://metadata.google.internal/computeMetadata/v1/", True),
])
def test_check_ssrf(url, expected):
    assert check_ssrf(url) == expected



# BFLA Testing
# Usage in tests
@pytest.mark.parametrize("function_call, expected", [
    ("delete_user(user_id)", True),
    ("fetch_user_data(user_id)", False),
])
def test_check_bfla(function_call, expected):
    assert check_bfla(function_call) == expected


# Usage in tests
# Usage in tests
@pytest.mark.parametrize("api_call, expected", [
    ("api.execute(unvalidated_input)", True),
    ("api.query(validated_input)", False),
])
def test_check_unsafe_api_usage(api_call, expected):
    assert check_unsafe_api_usage(api_call) == expected


# Usage in tests unrestricted_resource_consumption
@pytest.mark.parametrize("code_snippet, expected", [
    ("for i in range(10000000): do_something()", True),
    ("for i in range(100): do_something()", False),
])
def test_check_unrestricted_resource_consumption(code_snippet, expected):
    assert check_unrestricted_resource_consumption(code_snippet) == expected

# Unrestricted Business Flow Testing
# Usage in tests
@pytest.mark.parametrize("process_flow, expected", [
    ("process_order(order_id)", False),
    ("bypass_order_process(user_id)", True),
])
def test_check_unrestricted_business_flow(process_flow, expected):
    assert check_unrestricted_business_flow(process_flow) == expected


# Security Misconfiguration Testing
# Usage in tests
@pytest.mark.parametrize("config_setting, expected", [
    ("config.DEBUG = True", True),
    ("config.SECURE = True", False),
])
def test_check_security_misconfiguration(config_setting, expected):
    assert check_security_misconfiguration(config_setting) == expected

# Usage in tests bola
@pytest.mark.parametrize("auth_check, expected", [
    ("check_permissions(user, 'edit')", False),
    ("bypass_authorization(user)", True),
])
def test_check_broken_object_level_authorization(auth_check, expected):
    assert check_broken_object_level_authorization(auth_check) == expected

# Usage in tests broken authentication
@pytest.mark.parametrize("auth_process, expected", [
    ("login(user, 'weak_password')", True),
    ("authenticate_user(session_id)", False),
])
def test_check_broken_authentication(auth_process, expected):
    assert check_broken_authentication(auth_process) == expected

# BOPA Testing
# Usage in tests
@pytest.mark.parametrize("data_access, expected", [
    ("access_sensitive_data()", True),
    ("log_data_usage()", False),
])
def test_check_bopa(data_access, expected):
    assert check_bopa(data_access) == expected

# Usage in tests
@pytest.mark.parametrize("route, expected", [
    ("app.iter_rules()", True),
    ("app.route('/secure')", False),
])
def test_check_improper_inventory_management(route, expected):
    assert check_improper_inventory_management(route) == expected

    # Usage in tests
@pytest.mark.parametrize("input_string, expected", [
    ("<script>alert('XSS')</script>", True),
    ("<img src=x onerror=alert('XSS')>", True),
    ("Hello, world!", False),
    ("<b>Bold Text</b>", False)
])
def test_check_xss(input_string, expected):
    assert check_xss(input_string) == expected


@pytest.mark.parametrize("query, expected", [
    ("SELECT * FROM users WHERE user='admin';", False),
    ("SELECT * FROM users WHERE user=''; DROP TABLE users; --", True),
    ("SELECT * FROM users WHERE user='admin' OR '1'='1';", True),
    ("SELECT * FROM users WHERE user='admin' AND 'x'='x';", True),
])
def test_sql_injection(query, expected):
    assert check_sql_injection(query) == expected

@pytest.mark.parametrize("function_call, expected", [
    ("delete_user(user_id)", True),
    ("fetch_user_data(user_id)", False),
])
def test_check_bfla(function_call, expected):
    assert check_bfla(function_call) == expected

@pytest.mark.parametrize("process_flow, expected", [
    ("process_order(order_id)", False),
    ("bypass_order_process(user_id)", True),
])
def test_check_unrestricted_business_flow(process_flow, expected):
    assert check_unrestricted_business_flow(process_flow) == expected
