from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Election, Candidate, Vote

class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1
    fields = ('name', 'bio', 'photo')
    show_change_link = True

class ElectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'created_at', 'view_results_link')
    search_fields = ('title',)
    inlines = [CandidateInline]

    def view_results_link(self, obj):
        url = reverse('election_results', args=[obj.id])
        return format_html(
            '<a class="btn btn-sm btn-success" target="_blank" href="{}">View Results</a>', url
        )

    view_results_link.short_description = 'Results'

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'election', 'bio')
    list_filter = ('election',)
    search_fields = ('name',)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('voter', 'election', 'candidate', 'voted_at')
    list_filter = ('election', 'candidate')

admin.site.register(Election, ElectionAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Vote, VoteAdmin)
