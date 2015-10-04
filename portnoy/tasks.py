from board.models import Post


def remove_dead_post(recently=True):
    queryset = Post.objects.filter(parent__isnull=True).order_by('-pk')
    if recently:
        queryset = queryset[:100]
    for post in queryset:
        if post.last_life() <= 0:
            post.delete()
