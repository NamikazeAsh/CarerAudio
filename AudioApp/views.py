from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AudioFileForm
from .models import AudioFile

def upload_audio(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = AudioFileForm()
    return render(request, 'upload_audio.html', {'form': form})

def upload_success(request):
    return HttpResponse('File uploaded successfully!')

def serve_audio(request, slug):
    audio_file = AudioFile.objects.get(slug=slug)
    with open(audio_file.audio.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='audio/mpeg')
        response['Content-Disposition'] = 'inline; filename=' + audio_file.audio.name
        return response
