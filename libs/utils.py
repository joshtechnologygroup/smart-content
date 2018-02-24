import imp


def get_default_django_settings_module():
    try:
        file_ = imp.find_module('local', ['scontract/settings'])[0]
    except ImportError:
        default_django_settings_module = "scontract.settings.dev"
    else:
        default_django_settings_module = "scontract.settings.local"
        file_.close()
    return default_django_settings_module
