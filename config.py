# coding: utf-8
import web
from web.contrib.template import render_mako

lang = 'zh-CN'

pre_fix = 'controllers.'

urls = ('/?', pre_fix + 'welcome.index',
		'/admin/goods/?', pre_fix + 'goods_admin.index',
		'/admin/goods/edit/?', pre_fix + 'goods_admin.edit',
		'/admin/goods/edit/(.*)/?', pre_fix + 'goods_admin.edit',
		'/admin/goods/del/?', pre_fix + 'goods_admin.delete',
		'/admin/goods/show/(.*)/?', pre_fix + 'goods_admin.detail',
        '/admin/goods/images/(.*)/?', pre_fix + 'goods_admin.images',
        '/admin/goods_cateory/?', pre_fix + 'goods_category_admin.index',
        '/account/register/?', pre_fix + 'account.register',
        '/account/login/?', pre_fix + 'account.login',

		)


app = web.application(urls, globals(), autoreload=True)

page_admin = render_mako(
    directories=['templates/admin/'],
    default_filters=['decode.utf8'],
    input_encoding='utf-8',
    output_encoding='utf-8',

)
page_front = render_mako(
    directories=['templates/'],
    default_filters=['decode.utf8'],
    input_encoding='utf-8',
    output_encoding='utf-8',
)
