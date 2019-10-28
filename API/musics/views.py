from django.shortcuts import render,get_object_or_404
from .models import Music,Artist,Comment
from rest_framework.decorators import api_view
from .serializers import MusicSerializer, ArtistSerializer, ArtistDetailSerializer, CommentSerializer
from rest_framework.response import Response

#  GET,   POST,  PUT/PATCH,  DELETE
# Read,  Create,  Update,    Delete

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, id):
    music = get_object_or_404(music, id=id)
    serializer = MusicSerializer(music)
    return Response(serializer.data)

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detail(request,id):
    artist = get_object_or_404(Artist, id=id)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music_id=id)
    return Response(serializer.data)



@api_view(['GET','PUT','DELETE'])
def comment_detail(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            # return Response({'message':'업데이트!'})
    else:
        pass
