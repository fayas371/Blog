from django import forms
from .models import Post,Category


#choices=[('technology','technology'),('Sports','Sports'),('Marketing','Marketing')]
choices=Category.objects.all().values_list('name','name')

choices_list=[]
for item in choices:
    choices_list.append(item)





class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','title_tag','category','body','snippet','header_image')

        widgets={
        'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title of the post'}),
        'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title tag'}),
        'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
        #'body':forms.Textarea(attrs={'class':'form-control','rows':'4'}),
        'snippet':forms.Textarea(attrs={'class':'form-control','rows':'4'}),
          
        
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','title_tag','category','body','snippet','header_image')

        widgets={
        'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title of the post'}),
        'title_tag':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the title tag'}),
        'category':forms.Select(choices=choices_list,attrs={'class':'form-control'}),
        #'body':forms.Textarea(attrs={'class':'form-control','rows':'4'}),
        'snippet':forms.Textarea(attrs={'class':'form-control','rows':'4'}),
        }

