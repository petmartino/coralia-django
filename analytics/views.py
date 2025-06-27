# analytics/views.py

from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count
from django.contrib import admin # <-- ADD THIS IMPORT
from .models import Visit
import pandas as pd

@staff_member_required
def dashboard_view(request):
    # Fetch all visits into a pandas DataFrame for easy analysis
    all_visits = Visit.objects.all().values('timestamp', 'path', 'session_key')
    
    # --- ADD THESE TWO LINES ---
    # Get the list of all registered apps and their models
    app_list = admin.site.get_app_list(request)
    # ---------------------------

    if not all_visits.exists():
        # Also pass the app_list in the no_data case
        return render(request, 'admin/dashboard.html', {'no_data': True, 'title': 'Dashboard', 'app_list': app_list})

    df = pd.DataFrame.from_records(all_visits)
    # ... (the rest of the data processing code remains the same) ...
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)

    # Daily Unique Visitors (counting unique sessions per day)
    daily_visitors = df['session_key'].resample('D').nunique()
    
    # Weekly Unique Visitors
    weekly_visitors = df['session_key'].resample('W-MON', label='left', closed='left').nunique()
    
    chart_data = {
        'daily_labels': daily_visitors.index.strftime('%Y-%m-%d').tolist(),
        'daily_values': daily_visitors.values.tolist(),
        'weekly_labels': weekly_visitors.index.strftime('%Y-%m-%d').tolist(),
        'weekly_values': weekly_visitors.values.tolist()
    }
    
    # Top Pages
    filtered_paths = df[~df['path'].str.startswith(('/admin', '/static', '/favicon.ico'))]
    top_pages = filtered_paths['path'].value_counts().nlargest(10).to_dict()

    # Session Timelines
    sessions = {}
    for session_id, group in df.groupby('session_key'):
        sorted_group = group.sort_index()
        start_time = sorted_group.index[0]
        path_timeline = sorted_group['path'].tolist()
        sessions[session_id] = {'start_time': start_time, 'timeline': path_timeline}
    
    sorted_sessions = sorted(sessions.items(), key=lambda item: item[1]['start_time'], reverse=True)

    context = {
        'app_list': app_list, # <-- ADD THIS TO THE CONTEXT
        'chart_data': chart_data,
        'top_pages': top_pages,
        'sorted_sessions': sorted_sessions[:20],
        'title': 'Dashboard de Estadísticas',
        'has_permission': True,
    }
    return render(request, 'admin/dashboard.html', context)