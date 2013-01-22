# coding: utf-8
import web

pre_fix = 'controllers.';
urls = ('/?', pre_fix + 'welcome.index',
		'/admin/goods/?', pre_fix + 'goods_admin.index',
		'/admin/goods/edit/?', pre_fix + 'goods_admin.edit',
		'/admin/goods/edit/(.*)/?', pre_fix + 'goods_admin.edit',
		'/admin/goods/del/?', pre_fix + 'goods_admin.delete',
		'/admin/goods/show/(.*)/?', pre_fix + 'goods_admin.detail',
		)


app = web.application(urls, globals())

page_admin = web.template.render('templates/admin/', base='_layout')
page_front = web.template.render('templates/', base='_layout')


