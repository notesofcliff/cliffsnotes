from django.db import models

import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.toc import TocExtension

class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time of post creation",
    )
    modified = models.DateTimeField(
        auto_now=True,
        help_text="The date and time of the latest edit to the post",
    ) 
    title = models.CharField(
        max_length=4096,
        help_text="The title of the post",
    )
    slug = models.SlugField(
        unique=True,
        help_text="An identifier for the post, can only contain letters, numbers, underscores or hyphens",
    )
    description = models.TextField(
        help_text="A description of the content of the post",
    )
    body = models.TextField(
        help_text="The body of the post, markdown format is supported",
    )

    @property
    def rendered(self):
        """A dynamic property which provides the rendered body of the post
        """
        return markdown.markdown(
            self.body,
            extensions=[
                CodeHiliteExtension(
                    noclasses=True,
                    linenos=False,
                ),
                TocExtension(
                    baselevel=1,
                    toc_depth="2-6",
                ),
            ],
        )
