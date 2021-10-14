from erlang.libs.variables import PortalVariables


def set_portal(url, super_user=None, super_psd=None):
    PortalVariables.url = url
    if super_user and super_psd:
        PortalVariables.portal_user = super_user
        PortalVariables.portal_psd = super_psd
