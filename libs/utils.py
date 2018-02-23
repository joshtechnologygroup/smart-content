import imp


def get_default_django_settings_module():
    try:
        file_ = imp.find_module('local', ['scontent/settings'])[0]
    except ImportError:
        default_django_settings_module = "scontent.settings.dev"
    else:
        default_django_settings_module = "scontent.settings.local"
        file_.close()
    return default_django_settings_module
