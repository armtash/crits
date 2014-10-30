from django.conf.urls import patterns

urlpatterns = patterns('',
    # Dashboard
    (r'^new_save_search/$', 'crits.dashboards.views.new_save_search'),
    (r'^dashboard/$', 'crits.dashboards.views.dashboard'),
    (r'^dashboard/(?P<dashId>\w+)/$', 'crits.dashboards.views.dashboard'),
    (r'^edit_save_search/(?P<id>\S+)/$', 'crits.dashboards.views.edit_save_search'),
    (r'^delete_save_search/$', 'crits.dashboards.views.delete_save_search'),
    (r'^load_data/(?P<obj>\w+)/$', 'crits.dashboards.views.load_data'),
    (r'^load_data/(?P<obj>\w+)/(?P<term>\w+)/$', 'crits.dashboards.views.load_data'),
    (r'^save_search/$', 'crits.dashboards.views.save_search'),
    (r'^save_new_dashboard/$', 'crits.dashboards.views.save_new_dashboard'),
    (r'^destroy_dashboard/$', 'crits.dashboards.views.destroy_dashboard'),
    (r'^get_dashboard_table_data/(?P<tableName>\w+)/$', 'crits.dashboards.views.get_dashboard_table_data'),
    (r'^saved_searches_list/$', 'crits.dashboards.views.saved_searches_list'),
    (r'^toggle_table_visibility/$', 'crits.dashboards.views.toggle_table_visibility'),
    (r'^set_default_dashboard/$', 'crits.dashboards.views.set_default_dashboard'),
    (r'^set_dashboard_public/$', 'crits.dashboards.views.set_dashboard_public'),
    (r'^ignore_parent/(?P<id>\S+)/$', 'crits.dashboards.views.ignore_parent'),
    (r'^delete_dashboard/$', 'crits.dashboards.views.delete_dashboard'),
    (r'^rename_dashboard/$', 'crits.dashboards.views.rename_dashboard'),
    (r'^change_theme/$', 'crits.dashboards.views.change_theme'),
)
