from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils import timezone

from .models import TopMenu, SubMenu, Greeting, Member, Lab, Project, LectureNote, LectureVideo, DemoResource, Publication, Patent, Report, Notice, News, Gallery, Community, RelatedProject, Github

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

from django.core.paginator import Paginator

from .forms import NewsForm, CommunityForm, DemoForm
# Create your views here.

def index(request):
    # topMenus = TopMenu.objects.all()
    # subMenuDict = dict()
    # for topMenu in topMenus:
    #     subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
    #     subMenuDict[topMenu.titleen] = subMenus
    # return render(request, 'web/index.html', {'topMenus' : topMenus, 'subMenuDict' : subMenuDict})

    return render(request, 'web/index.html', {'subMenuDict':getSubMenuDict()})

def getSubMenuDict():
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return subMenuDict

# def menu_detail(request, topMenu):
#     topMenu_id = TopMenu.objects.get(titleen=topMenu)
#     subMenus = get_list_or_404(SubMenu, topmenu_id=topMenu_id.pk)
#     return render(request, 'web/menu_detail.html', {'topMenu': topMenu, 'subMenus': subMenus })

# ListView
class GreetingPage(TemplateView):
    model = Greeting
    template_name = 'web/greetingTemp.html'

    def get_context_data(self, **kwargs):
        context = super(GreetingPage, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class MemberImageList(ListView):
    model = Member
    template_name = 'web/memberTemp.html'  # Default: <app_label>/<model_name>_list.html
    # context_object_name = 'member_list'
    paginate_by = 5
    queryset = Member.objects.order_by('-id')  

    # context={ 'context_object_name':'news_list', 'subMenuDict':getSubMenuDict() }
    def get_context_data(self, **kwargs):
        context = super(MemberImageList, self).get_context_data(**kwargs)
        context['object_name'] = 'member_list'
        context['subMenuDict'] = getSubMenuDict()
        return context

class LabTextList(ListView):
    model = Lab
    template_name = 'web/lab_detailTemp.html'

    def get_context_data(self, **kwargs):
        context = super(LabTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class ProjectPage(TemplateView):
    model = Project
    template_name = 'web/projectTemp.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectPage, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class LecturenoteImageList(ListView):
    model = LectureNote
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(LecturenoteImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class LecturevideoVideoList(ListView):
    model = LectureVideo
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(LecturevideoVideoList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class DemoresourceImageList(ListView):
    model = DemoResource
    template_name = 'web/demoresource.html'

    def get_context_data(self, **kwargs):
        context = super(DemoresourceImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class PublicationTextList(ListView):
    model = Publication
    template_name = 'web/publication.html'

    def get_context_data(self, **kwargs):
        context = super(PublicationTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class PatentTextList(ListView):
    model = Patent
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(PatentTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class ReportTextList(ListView):
    model = Report
    template_name = 'web/preparing.html'

    def get_context_data(self, **kwargs):
        context = super(ReportTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class NoticeTextList(ListView):
    model = Notice
    template_name = 'web/notice.html'

    def get_context_data(self, **kwargs):
        context = super(NoticeTextList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class NewsImageList(ListView):
    model = News
    template_name = 'web/news_temp.html'  # Default: <app_label>/<model_name>_list.html
    # context_object_name = 'news_list'
    paginate_by = 5
    queryset = News.objects.order_by('-id') 
    # context={ 'context_object_name':'news_list', 'subMenuDict':getSubMenuDict() }
    def get_context_data(self, **kwargs):
        context = super(NewsImageList, self).get_context_data(**kwargs)
        context['object_name'] = 'news_list'
        context['subMenuDict'] = getSubMenuDict()
        return context

class GalleryImageList(ListView):
    model = Gallery
    template_name = 'web/imagelist.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryImageList, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class CommunityBoard(ListView):
    model = Community
    template_name = 'web/community.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityBoard, self).get_context_data(**kwargs)
        context['object_name'] = 'community_list'
        context['subMenuDict'] = getSubMenuDict()
        return context

class CommunityDetail(DetailView):
    model = Community
    template_name = 'web/community_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityDetail, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'web/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

#OPEN SOURCE
class GithubTextlist(ListView):
    model = Github
    template_name = 'web/github.html'

    def get_context_data(self, **kwargs):
        context = super(GithubTextlist, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

class RelatedProject(ListView):
    model = RelatedProject
    template_name = 'web/relatedproject.html'

    def get_context_data(self, **kwargs):
        context = super(RelatedProject, self).get_context_data(**kwargs)
        context['subMenuDict'] = getSubMenuDict()
        return context

def RelatedProject2(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/relatedproject_2.html', {'subMenuDict':getSubMenuDict()})

def RelatedProject3(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/relatedproject_3.html', {'subMenuDict':getSubMenuDict()})    

def Amorepacific(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/amorepacific.html', {'subMenuDict':getSubMenuDict()})

def HyundaiMobis(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/hyundaiMobis.html', {'subMenuDict':getSubMenuDict()})

def hyundaimotor(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/hyundaimotor.html', {'subMenuDict':getSubMenuDict()})

def koreaelectric(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/koreaelectric.html', {'subMenuDict':getSubMenuDict()})

def lgchem(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/lgchem.html', {'subMenuDict':getSubMenuDict()})

def lghnhc(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/lghnhc.html', {'subMenuDict':getSubMenuDict()})

def samsungcnt(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/samsungcnt.html', {'subMenuDict':getSubMenuDict()})

def samsungelectronics(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/samsungelectronics.html', {'subMenuDict':getSubMenuDict()})

def samsungsds(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/samsungsds.html', {'subMenuDict':getSubMenuDict()})

def Contact(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus
    return render(request, 'web/contact.html', {'subMenuDict':getSubMenuDict()})

#News Board
def news_new(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus

    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.writer = request.user
            news.date = timezone.now()
            news.save()
            return redirect('news_detail', pk=news.pk)
    elif request.method == "GET":
        form = NewsForm()

    return render(request, 'web/news_edit.html', {'form':form}, {'subMenuDict':getSubMenuDict()})

def news_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', pk=post.pk)
    elif request.method == "GET":
        form = PostForm(instance=post)
    return render(request, 'web/news_edit.html', {'form': form})

#Community
def community_new(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus

    if request.method == "POST":
        form = CommunityForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.writer = request.user
            news.date = timezone.now()
            news.save()
            return redirect('community_detail', pk=news.pk)
    elif request.method == "GET":
        form = CommunityForm()

    return render(request, 'web/community_edit.html',{'subMenuDict':getSubMenuDict()})

def community_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommunityForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', pk=post.pk)
    elif request.method == "GET":
        form = CommunityForm(instance=post)
    return render(request, 'web/community_edit.html', {'form': form})

#demoresource
def demoresource_new(request):
    topMenus = TopMenu.objects.all()
    subMenuDict = dict()
    for topMenu in topMenus:
        subMenus = SubMenu.objects.filter(topmenu_id=topMenu.id)
        subMenuDict[topMenu.titleen] = subMenus

    if request.method == "POST":
        form = DemoForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.writer = request.user
            news.date = timezone.now()
            news.save()
            return redirect('demoresource_detail', pk=news.pk)
    elif request.method == "GET":
        form = DemoForm()

    return render(request, 'web/demoresource_edit.html', {'form':form}, {'subMenuDict':getSubMenuDict()})

def demoresource_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = DemoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('demoresource_detail', pk=post.pk)
    elif request.method == "GET":
        form = DemoForm(instance=post)
    return render(request, 'web/demoresource_edit.html', {'form': form})