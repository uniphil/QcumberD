from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.cache import cache_page

import json

from enrollment.models import SolusSession
from course_catalog.models import Section

@cache_page(60 * 1)
def enrollment_numbers(request, subject_abbr, course_num, solus_id):
    section = get_object_or_404(Section, course__subject__abbreviation=subject_abbr, course__number=course_num, solus_id=solus_id)

    capacity, enrolled = SolusSession().scrape_enrollment(section)

    return render_to_response('enrollment/numbers.html', {'enrolled': enrolled, 'capacity': capacity})