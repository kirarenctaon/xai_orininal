from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<subMenu>.+)/$', views.subMenu, name='subMenu'),

    # List
    url(r'^about/greeting/$', views.GreetingPage.as_view(), name='greeting'),
    url(r'^about/member/$', views.MemberImageList.as_view(), name='member'),
    url(r'^about/lab/$', views.LabTextList.as_view(), name='lab'),
    url(r'^about/project/$', views.ProjectPage.as_view(), name='project'),
   
    url(r'^news&info/notice/$', views.NoticeTextList.as_view(), name='notice'),
    url(r'^news&info/news/$', views.NewsImageList.as_view(), name='news'),
    url(r'^news&info/news_new/$', views.news_new, name='news_new'),
    url(r'^news&info/gallery/$', views.GalleryImageList.as_view(), name='gallery'),
    url(r'^news&info/community/$', views.CommunityBoard.as_view(), name='community'),
    url(r'^news&info/community_new/$', views.community_new, name='community_new'),

    url(r'^research/lecturenote/$', views.LecturenoteImageList.as_view(), name='lecturenote'),
    url(r'^research/lecturevideo/$', views.LecturevideoVideoList.as_view(), name='lecturevideo'),
    url(r'^research/demoresource/$', views.DemoresourceImageList.as_view(), name='demoresource'),
    url(r'^research/publication/$', views.PublicationTextList.as_view(), name='publication'),
    url(r'^research/patent/$', views.PatentTextList.as_view(), name='patent'),
    url(r'^research/report/$', views.ReportTextList.as_view(), name='report'),


    url(r'^research/demoresource/amorepacific$', views.Amorepacific, name='amorepacific'),
    url(r'^research/demoresource/hyundaiMobis$', views.HyundaiMobis, name='hyundaiMobis'),

    #opensource
    url(r'^opensource/github/$', views.GithubTextlist.as_view(), name='github'),
    url(r'^opensource/relatedproject/1$', views.RelatedProject.as_view(), name='relatedproject'),
    url(r'^opensource/relatedproject/2$', views.RelatedProject2, name='relatedproject2'),
    url(r'^opensource/relatedproject/3$', views.RelatedProject3, name='relatedproject3'),

    url(r'^contact/$', views.Contact, name='contact'),

    # Detail
    url(r'^news&info/news/(?P<pk>\d+)/$', views.NewsDetail.as_view(), name='news_detail'),
    url(r'^news&info/community/(?P<pk>\d+)/$', views.CommunityDetail.as_view(), name='community_detail'),

]


