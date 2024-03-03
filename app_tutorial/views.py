#// this is a test comment
#// this is a test comment
#! this is a test comment
#? this is a test comment
#* this is a test comment
#TODO: this is a test comment


from django.shortcuts import render
from .models import Subjects, Topics, Entries
from .forms import SubjectsForm, TopicsForm, EntriesForm


# Create your views here.

def index(request):

    subjects_db = Subjects.objects.all()
    topics_db = Topics.objects.all()
    entries_db = Entries.objects.all()
    
    return render(request, 'index.html',
        {
            'subjects_db': subjects_db,
            'topics_db': topics_db,
            'entries_db': entries_db
        }
        )




def subject_view(request, subject_request):

    subjects_db = Subjects.objects.all()
    topics_db = Topics.objects.all()
    entries_db = Entries.objects.all()

    #default status for forms
    form_status = ''

    #subject_name
    if subject_request == 'all':
        # pass to keep all entries in entries_db available for view
        pass
    else:
        entries_db = Entries.objects.filter(subject__subject=subject_request)


    add_topic_form = TopicsForm()
    add_entry_form = EntriesForm()
    add_subject_form = SubjectsForm()

    if request.method == 'POST':
        #send to function to handle form data
        form_status = form_to_database(request.POST)
        print(f'form status: {form_status}')


        if 'Error' in form_status:
            if request.POST.get('add_section'):
                add_subject_form = SubjectsForm(request.POST)
                add_topic_form = TopicsForm()
                add_entry_form = EntriesForm()
            elif request.POST.get('add_topic'):
                add_subject_form = SubjectsForm()
                add_topic_form = TopicsForm(request.POST)
                add_entry_form = EntriesForm()
            elif request.POST.get('add_entry'):
                add_subject_form = SubjectsForm()
                add_topic_form = TopicsForm()
                add_entry_form = EntriesForm(request.POST)
        else:
            add_subject_form = SubjectsForm()
            add_topic_form = TopicsForm()
            add_entry_form = EntriesForm()

    return render(request, 'subject.html', {
        # forms for page
        'add_topic_form': add_topic_form,
        'add_entry_form': add_entry_form,
        'add_subject_form': add_subject_form,

        # database content
        'subjects_db': subjects_db,
        'entries_db': entries_db, 

        # subject name from page url
        'subject_request': subject_request,

        'form_error': form_status   
    })




def form_to_database(POSTrequest):
    '''this function will take the name of the button from teh form and use it to determine which form to use to save the data to the database.'''

    print(f'post request from function: {POSTrequest}')
    
    if 'add_section' in POSTrequest:

        form_post_req = SubjectsForm(POSTrequest)

        if form_post_req.is_valid():

            if Subjects.objects.filter(subject=form_post_req.cleaned_data['subject']).exists():

                return('Error: Subject already exists')
            
            else:
                
                form_post_req.save()
                return('Success: Subject added')


    elif 'add_topic' in POSTrequest:

        form_post_req = TopicsForm(POSTrequest)

        if form_post_req.is_valid():
            if Subjects.objects.filter(subject=form_post_req.cleaned_data['subject']).exists() and Topics.objects.filter(section=form_post_req.cleaned_data['section']).exists():

                return('Error: Topic already exists')
            
            else:

                form_post_req.save()
                return('Success: Subject added')



    elif 'add_entry' in POSTrequest:

        form_post_req = EntriesForm(POSTrequest)

        if form_post_req.is_valid():

            form_post_req.save()
            return('Success: Subject added')
            
        else:

            return('Error: form not valid')


    else:
        return('Error: Form not found or form not valid')

        
