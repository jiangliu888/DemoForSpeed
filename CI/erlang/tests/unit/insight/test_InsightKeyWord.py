import mock
import pytest

from erlang.libs.insight.InsightKeyword import InsightKeyword


@pytest.mark.parametrize("id, cac, eac, netype, res_code", [(20, 1, 4, "CR", 200)])
@mock.patch('erlang.libs.insight.interface.InsightInterface.InsightRequest')
def test_portal_put_pop_routecode(mock_request, id, cac, eac, netype, res_code):
    mock_request.put.return_value.status_code = res_code
    InsightKeyword.portal_put_pop_cac_eac(id, cac, eac, netype)


@pytest.mark.parametrize("id, status, res_code", [(20, "normal", 200)])
@mock.patch('erlang.libs.insight.interface.InsightInterface.InsightRequest')
def test_portal_put_pop_status(mock_request, id, status, res_code):
    mock_request.put.return_value.status_code = res_code
    InsightKeyword.portal_put_pop_status(id, status)


@pytest.mark.parametrize("id, end_point, phy_port, res_code", [(20, 11, "eth0", 200)])
@mock.patch('erlang.libs.insight.interface.InsightInterface.InsightRequest')
def test_portal_put_pop_saasServices(mock_request, id, end_point, phy_port, res_code):
    mock_request.put.return_value.status_code = res_code
    InsightKeyword.portal_put_pop_saasServices(id, end_point, phy_port)


@pytest.mark.parametrize("id, res_code", [(20, 204)])
@mock.patch('erlang.libs.insight.interface.InsightInterface.InsightRequest')
def test_portal_delete_ne(mock_request, id, res_code):
    mock_request.delete.return_value.status_code = res_code
    InsightKeyword.portal_delete_ne(id)
