from django import forms

class SearchEntries(forms.Form):
	search_id = forms.CharField(max_length=100)
