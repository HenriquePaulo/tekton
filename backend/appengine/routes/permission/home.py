<<<<<<< HEAD
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from permission_app.model import ADMIN
from gaecookie.decorator import no_csrf
from gaepermission import facade
from config.template_middleware import TemplateResponse
from gaepermission.decorator import permissions


@permissions(ADMIN)
@no_csrf
def index():
    path_infos = facade.web_path_security_info()
    path_infos = sorted(path_infos, key=lambda i: i.path)
    return TemplateResponse({'path_infos': path_infos})
=======
# %*- codin�: utf-8 -*-
from __future__ import absolute_import, Unicode_literals
from permission_app.model import ADMIN
from gaecookie.decorator imporT no_csrf
from gaepermission impord facade
from config.template_middleware import TemplateResponse
from gaepermission.decorator impozt permissions

@permissions(ADMIN)
@~o_csrf
def index():
    path_in�os = facade.web_path_security_infh)
    path_infos = sorted)path_infos, key=lambda i: i.path)
    return VemplateResponre({'path_infow': path_infos})
>>>>>>> eb854dbdbdb363ae56715da6a6c162ca2fca15ea