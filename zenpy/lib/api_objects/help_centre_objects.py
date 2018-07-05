from zenpy.lib.api_objects import BaseObject
import dateutil.parser


class AccessPolicy(BaseObject):
    def __init__(self,
                 api=None,
                 manageable_by=None,
                 required_tags=None,
                 restricted_to_group_ids=None,
                 restricted_to_organization_ids=None,
                 viewable_by=None,
                 **kwargs):

        self.api = api
        self.manageable_by = manageable_by
        self.required_tags = required_tags
        self.restricted_to_group_ids = restricted_to_group_ids
        self.restricted_to_organization_ids = restricted_to_organization_ids
        self.viewable_by = viewable_by

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def restricted_to_groups(self):

        if self.api and self.restricted_to_group_ids:
            return self.api._get_restricted_to_groups(
                self.restricted_to_group_ids)

    @restricted_to_groups.setter
    def restricted_to_groups(self, restricted_to_groups):
        if restricted_to_groups:
            self.restricted_to_group_ids = [o.id for o in restricted_to_groups]
            self._restricted_to_groups = restricted_to_groups

    @property
    def restricted_to_organizations(self):

        if self.api and self.restricted_to_organization_ids:
            return self.api._get_restricted_to_organizations(
                self.restricted_to_organization_ids)

    @restricted_to_organizations.setter
    def restricted_to_organizations(self, restricted_to_organizations):
        if restricted_to_organizations:
            self.restricted_to_organization_ids = [
                o.id for o in restricted_to_organizations
            ]
            self._restricted_to_organizations = restricted_to_organizations


class Article(BaseObject):
    def __init__(self,
                 api=None,
                 author_id=None,
                 body=None,
                 comments_disabled=None,
                 created_at=None,
                 draft=None,
                 html_url=None,
                 id=None,
                 label_names=None,
                 locale=None,
                 name=None,
                 outdated=None,
                 outdated_locales=None,
                 position=None,
                 promoted=None,
                 section_id=None,
                 source_locale=None,
                 title=None,
                 updated_at=None,
                 url=None,
                 vote_count=None,
                 vote_sum=None,
                 **kwargs):

        self.api = api

        # Comment: The id of the user who wrote the article (set to the user who made the request on create by default)
        # Mandatory: no
        # Read-only: no
        # Type: integer
        self.author_id = author_id

        # Comment: The body of the article
        # Mandatory: no
        # Read-only: no
        # Type: string
        self.body = body

        # Comment: True if comments are disabled; false otherwise
        # Mandatory: no
        # Read-only: no
        # Type: boolean
        self.comments_disabled = comments_disabled

        # Comment: The time the article was created
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: True if the translation for the current locale is a draft; false otherwise. false by default. Can be set when creating but not when updating. For updating, see Translations
        # Mandatory: no
        # Read-only: yes
        # Type: boolean
        self.draft = draft

        # Comment: The url of the article in Help Center
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.html_url = html_url

        # Comment: Automatically assigned when the article is created
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: An array of label names associated with this article. By default no label names are used. Only available on certain plans
        # Mandatory: no
        # Read-only: no
        # Type: string
        self.label_names = label_names

        # Comment: The locale that the article is being displayed in
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.locale = locale
        self.name = name

        # Comment: Deprecated. Always false because the source translation is always the most up-to-date translation
        # Mandatory: no
        # Read-only: yes
        # Type: boolean
        self.outdated = outdated

        # Comment: Locales in which the article was marked as outdated
        # Mandatory: no
        # Read-only: yes
        # Type: array
        self.outdated_locales = outdated_locales

        # Comment: The position of this article in the article list. 0 by default
        # Mandatory: no
        # Read-only: no
        # Type: integer
        self.position = position

        # Comment: True if this article is promoted; false otherwise. false by default
        # Mandatory: no
        # Read-only: no
        # Type: boolean
        self.promoted = promoted

        # Comment: The id of the section to which this article belongs
        # Mandatory: no
        # Read-only: no
        # Type: integer
        self.section_id = section_id

        # Comment: The source (default) locale of the article
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.source_locale = source_locale

        # Comment: The title of the article
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.title = title

        # Comment: The time the article was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The API url of the article
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.url = url

        # Comment: The total number of upvotes and downvotes
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.vote_count = vote_count

        # Comment: The sum of upvotes (+1) and downvotes (-1), which may be positive or negative
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.vote_sum = vote_sum

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def author(self):
        """
        |  Comment: The id of the user who wrote the article (set to the user who made the request on create by default)
        """
        if self.api and self.author_id:
            return self.api._get_user(self.author_id)

    @author.setter
    def author(self, author):
        if author:
            self.author_id = author.id
            self._author = author

    @property
    def created(self):
        """
        |  Comment: The time the article was created
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def section(self):
        """
        |  Comment: The id of the section to which this article belongs
        """
        if self.api and self.section_id:
            return self.api._get_section(self.section_id)

    @section.setter
    def section(self, section):
        if section:
            self.section_id = section.id
            self._section = section

    @property
    def updated(self):
        """
        |  Comment: The time the article was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated


class ArticleAttachment(BaseObject):
    def __init__(self,
                 api=None,
                 article_id=None,
                 content_type=None,
                 content_url=None,
                 file_name=None,
                 id=None,
                 inline=None,
                 size=None,
                 **kwargs):

        self.api = api

        # Comment: Id of the associated article, if present
        # Type: integer
        self.article_id = article_id

        # Comment: The content type of the file. Example: image/png
        # Type: string
        self.content_type = content_type

        # Comment: A full URL where the attachment file can be downloaded
        # Type: string
        self.content_url = content_url

        # Comment: The name of the file
        # Type: string
        self.file_name = file_name

        # Comment: Automatically assigned when the article attachment is created
        # Type: integer
        self.id = id

        # Comment: If true, the attached file is shown in the dedicated admin UI for inline attachments and its url can be referenced in the HTML body of the article. If false, the attachment is listed in the list of attachments. Default is false
        # Type: boolean
        self.inline = inline

        # Comment: The size of the attachment file in bytes
        # Type: integer
        self.size = size

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def article(self):
        """
        |  Comment: Id of the associated article, if present
        """
        if self.api and self.article_id:
            return self.api._get_article(self.article_id)

    @article.setter
    def article(self, article):
        if article:
            self.article_id = article.id
            self._article = article


class Category(BaseObject):
    def __init__(self,
                 api=None,
                 created_at=None,
                 description=None,
                 html_url=None,
                 id=None,
                 locale=None,
                 name=None,
                 outdated=None,
                 position=None,
                 source_locale=None,
                 updated_at=None,
                 url=None,
                 **kwargs):

        self.api = api
        self.created_at = created_at
        self.description = description
        self.html_url = html_url
        self.id = id
        self.locale = locale
        self.name = name
        self.outdated = outdated
        self.position = position
        self.source_locale = source_locale
        self.updated_at = updated_at
        self.url = url

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def created(self):

        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def updated(self):

        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated


class Comment(BaseObject):
    def __init__(self,
                 api=None,
                 author_id=None,
                 body=None,
                 created_at=None,
                 html_url=None,
                 id=None,
                 locale=None,
                 source_id=None,
                 source_type=None,
                 updated_at=None,
                 url=None,
                 vote_count=None,
                 vote_sum=None,
                 **kwargs):

        self.api = api

        # Comment: The id of the author of this comment. Writable on create by Help Center managers -- see Create Comment
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.author_id = author_id

        # Comment: The comment made by the author
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.body = body

        # Comment: The time at which the comment was created. Writable on create by Help Center managers -- see Create Comment
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: The url at which the comment is presented in Help Center
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.html_url = html_url

        # Comment: Automatically assigned when the comment is created
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: The locale in which this comment was made
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.locale = locale

        # Comment: The id of the item on which this comment was made
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.source_id = source_id

        # Comment: The type of the item on which this comment was made. Currently only supports 'Article'
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.source_type = source_type

        # Comment: The time at which the comment was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The API url of this comment
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.url = url

        # Comment: The total number of upvotes and downvotes
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.vote_count = vote_count

        # Comment: The sum of upvotes (+1) and downvotes (-1), which may be positive or negative
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.vote_sum = vote_sum

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def author(self):
        """
        |  Comment: The id of the author of this comment. Writable on create by Help Center managers -- see Create Comment
        """
        if self.api and self.author_id:
            return self.api._get_user(self.author_id)

    @author.setter
    def author(self, author):
        if author:
            self.author_id = author.id
            self._author = author

    @property
    def created(self):
        """
        |  Comment: The time at which the comment was created. Writable on create by Help Center managers -- see Create Comment
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def updated(self):
        """
        |  Comment: The time at which the comment was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated


class Label(BaseObject):
    def __init__(self,
                 api=None,
                 created_at=None,
                 id=None,
                 name=None,
                 updated_at=None,
                 url=None,
                 **kwargs):

        self.api = api

        # Comment: The time at which the label was created
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: Automatically assigned when the label is created
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: The actual name of the label
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.name = name

        # Comment: The time at which the label was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The API url of this label
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.url = url

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def created(self):
        """
        |  Comment: The time at which the label was created
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def updated(self):
        """
        |  Comment: The time at which the label was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated


class Post(BaseObject):
    def __init__(self,
                 api=None,
                 author_id=None,
                 closed=None,
                 comment_count=None,
                 created_at=None,
                 details=None,
                 featured=None,
                 follower_count=None,
                 html_url=None,
                 id=None,
                 pinned=None,
                 status=None,
                 title=None,
                 topic_id=None,
                 updated_at=None,
                 url=None,
                 vote_count=None,
                 vote_sum=None,
                 **kwargs):

        self.api = api

        # Comment: The id of the author of the post. Writable on create by Help Center managers -- see Create Post
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.author_id = author_id

        # Comment: Whether further comments are allowed
        # Mandatory: no
        # Read-only: no
        # Type: boolean
        self.closed = closed

        # Comment: The number of comments on the post
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.comment_count = comment_count

        # Comment: When the post was created. Writable on create by Help Center managers -- see Create Post
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: The details of the post
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.details = details

        # Comment: Whether the post is featured
        # Mandatory: no
        # Read-only: no
        # Type: boolean
        self.featured = featured

        # Comment: The number of followers of the post
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.follower_count = follower_count

        # Comment: The community url of the post
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.html_url = html_url

        # Comment: Automatically assigned when the post is created
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: When true, pins the post to the top of its topic
        # Mandatory: no
        # Read-only: no
        # Type: boolean
        self.pinned = pinned

        # Comment: The status of the post. Possible values: "planned", "not_planned" , "answered", or "completed"
        # Mandatory: no
        # Read-only: no
        # Type: string
        self.status = status

        # Comment: The title of the post
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.title = title

        # Comment: The id of the topic that the post belongs to
        # Mandatory: yes
        # Read-only: no
        # Type: integer
        self.topic_id = topic_id

        # Comment: When the post was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The API url of the post
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.url = url

        # Comment: The total number of upvotes and downvotes
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.vote_count = vote_count

        # Comment: The sum of upvotes (+1) and downvotes (-1), which may be positive or negative
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.vote_sum = vote_sum

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def author(self):
        """
        |  Comment: The id of the author of the post. Writable on create by Help Center managers -- see Create Post
        """
        if self.api and self.author_id:
            return self.api._get_user(self.author_id)

    @author.setter
    def author(self, author):
        if author:
            self.author_id = author.id
            self._author = author

    @property
    def created(self):
        """
        |  Comment: When the post was created. Writable on create by Help Center managers -- see Create Post
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def topic(self):
        """
        |  Comment: The id of the topic that the post belongs to
        """
        if self.api and self.topic_id:
            return self.api._get_topic(self.topic_id)

    @topic.setter
    def topic(self, topic):
        if topic:
            self.topic_id = topic.id
            self._topic = topic

    @property
    def updated(self):
        """
        |  Comment: When the post was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated


class Section(BaseObject):
    def __init__(self,
                 api=None,
                 category_id=None,
                 created_at=None,
                 description=None,
                 html_url=None,
                 id=None,
                 locale=None,
                 manageable_by=None,
                 name=None,
                 outdated=None,
                 position=None,
                 sorting=None,
                 source_locale=None,
                 updated_at=None,
                 url=None,
                 user_segment_id=None,
                 **kwargs):

        self.api = api

        # Comment: The id of the category to which this section belongs
        # Mandatory: no
        # Read-only: no
        # Type: integer
        self.category_id = category_id

        # Comment: The time at which the section was created
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: The description of the section
        # Mandatory: no
        # Read-only: no
        # Type: string
        self.description = description

        # Comment: The url of this section in HC
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.html_url = html_url

        # Comment: Automatically assigned when creating subscriptions
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: The locale in which the section is displayed
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.locale = locale

        # Comment: The set of users who can manage this section
        # Mandatory: no
        # Read-only: no
        # Type: string
        self.manageable_by = manageable_by

        # Comment: The name of the section
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.name = name

        # Comment: Whether the section is out of date
        # Mandatory: no
        # Read-only: yes
        # Type: boolean
        self.outdated = outdated

        # Comment: The position of this section in the section list. By default the section is added to the end of the list
        # Mandatory: no
        # Read-only: no
        # Type: integer
        self.position = position
        self.sorting = sorting

        # Comment: The source (default) locale of the section
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.source_locale = source_locale

        # Comment: The time at which the section was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The API url of this section
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.url = url

        # Comment: The id of the user segment to which this section belongs
        # Mandatory: no
        # Read-only: no
        # Type: integer
        self.user_segment_id = user_segment_id

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def category(self):
        """
        |  Comment: The id of the category to which this section belongs
        """
        if self.api and self.category_id:
            return self.api._get_category(self.category_id)

    @category.setter
    def category(self, category):
        if category:
            self.category_id = category.id
            self._category = category

    @property
    def created(self):
        """
        |  Comment: The time at which the section was created
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def updated(self):
        """
        |  Comment: The time at which the section was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated

    @property
    def user_segment(self):
        """
        |  Comment: The id of the user segment to which this section belongs
        """
        if self.api and self.user_segment_id:
            return self.api._get_user_segment(self.user_segment_id)

    @user_segment.setter
    def user_segment(self, user_segment):
        if user_segment:
            self.user_segment_id = user_segment.id
            self._user_segment = user_segment


class Subscription(BaseObject):
    def __init__(self,
                 api=None,
                 content_id=None,
                 created_at=None,
                 id=None,
                 locale=None,
                 updated_at=None,
                 url=None,
                 user_id=None,
                 **kwargs):

        self.api = api

        # Comment: The id of the subscribed item
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.content_id = content_id

        # Comment: The time at which the subscription was created
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: Automatically assigned when the subscription is created
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: The locale of the subscribed item
        # Mandatory: yes
        # Read-only: yes
        # Type: string
        self.locale = locale

        # Comment: The time at which the subscription was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The API url of the subscription
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.url = url

        # Comment: The id of the user who has this subscription
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.user_id = user_id

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def created(self):
        """
        |  Comment: The time at which the subscription was created
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def updated(self):
        """
        |  Comment: The time at which the subscription was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated

    @property
    def user(self):
        """
        |  Comment: The id of the user who has this subscription
        """
        if self.api and self.user_id:
            return self.api._get_user(self.user_id)

    @user.setter
    def user(self, user):
        if user:
            self.user_id = user.id
            self._user = user


class Topic(BaseObject):
    def __init__(self,
                 api=None,
                 community_id=None,
                 created_at=None,
                 description=None,
                 follower_count=None,
                 html_url=None,
                 id=None,
                 name=None,
                 position=None,
                 updated_at=None,
                 url=None,
                 user_segment_id=None,
                 **kwargs):

        self.api = api
        self.community_id = community_id

        # Comment: When the topic was created
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: The description of the topic. By default an empty string
        # Mandatory: no
        # Read-only: no
        # Type: string
        self.description = description

        # Comment: The number of users following the topic
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.follower_count = follower_count

        # Comment: The community url of the topic
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.html_url = html_url

        # Comment: Automatically assigned when the topic is created
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: The name of the topic
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.name = name

        # Comment: The position of the topic relative to other topics in the community
        # Mandatory: no
        # Read-only: no
        # Type: integer
        self.position = position

        # Comment: When the topic was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The API url of the topic
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.url = url

        # Comment: The id of the user segment to which this topic belongs
        # Mandatory: no
        # Read-only: no
        # Type: integer
        self.user_segment_id = user_segment_id

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def created(self):
        """
        |  Comment: When the topic was created
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def updated(self):
        """
        |  Comment: When the topic was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated

    @property
    def user_segment(self):
        """
        |  Comment: The id of the user segment to which this topic belongs
        """
        if self.api and self.user_segment_id:
            return self.api._get_user_segment(self.user_segment_id)

    @user_segment.setter
    def user_segment(self, user_segment):
        if user_segment:
            self.user_segment_id = user_segment.id
            self._user_segment = user_segment


class Translation(BaseObject):
    def __init__(self,
                 api=None,
                 body=None,
                 created_at=None,
                 created_by_id=None,
                 draft=None,
                 hidden=None,
                 html_url=None,
                 id=None,
                 locale=None,
                 outdated=None,
                 source_id=None,
                 source_type=None,
                 title=None,
                 updated_at=None,
                 updated_by_id=None,
                 url=None,
                 **kwargs):

        self.api = api

        # Comment: The body of the translation. Empty by default
        # Mandatory: no
        # Read-only: no
        # Type: string
        self.body = body

        # Comment: The time at which the translation was created
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: The id of the user who created the translation
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.created_by_id = created_by_id

        # Comment: True if the translation is a draft; false otherwise. False by default
        # Mandatory: no
        # Read-only: no
        # Type: boolean
        self.draft = draft
        self.hidden = hidden

        # Comment: The url of the translation in Help Center
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.html_url = html_url

        # Comment: Automatically assigned when a translation is created
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: The locale of the translation
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.locale = locale

        # Comment: True if the translation is outdated; false otherwise. False by default
        # Mandatory: no
        # Read-only: no
        # Type: boolean
        self.outdated = outdated

        # Comment: The id of the item that has this translation
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.source_id = source_id

        # Comment: The type of the item that has this translation. Can be Article, Section, or Category
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.source_type = source_type

        # Comment: The title of the translation
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.title = title

        # Comment: The time at which the translation was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The id of the user who last updated the translation
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.updated_by_id = updated_by_id

        # Comment: The API url of the translation
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.url = url

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def created(self):
        """
        |  Comment: The time at which the translation was created
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def created_by(self):
        """
        |  Comment: The id of the user who created the translation
        """
        if self.api and self.created_by_id:
            return self.api._get_user(self.created_by_id)

    @created_by.setter
    def created_by(self, created_by):
        if created_by:
            self.created_by_id = created_by.id
            self._created_by = created_by

    @property
    def updated(self):
        """
        |  Comment: The time at which the translation was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated

    @property
    def updated_by(self):
        """
        |  Comment: The id of the user who last updated the translation
        """
        if self.api and self.updated_by_id:
            return self.api._get_user(self.updated_by_id)

    @updated_by.setter
    def updated_by(self, updated_by):
        if updated_by:
            self.updated_by_id = updated_by.id
            self._updated_by = updated_by


class UserSegment(BaseObject):
    def __init__(self,
                 api=None,
                 built_in=None,
                 created_at=None,
                 group_ids=None,
                 id=None,
                 name=None,
                 organization_ids=None,
                 tags=None,
                 updated_at=None,
                 user_type=None,
                 **kwargs):

        self.api = api

        # Comment: Whether the user segment is built-in. Built-in user segments cannot be modified
        # Mandatory: no
        # Read-only: yes
        # Type: boolean
        self.built_in = built_in

        # Comment: When the user segment was created
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: The ids of the groups that have access
        # Mandatory: no
        # Read-only: no
        # Type: array
        self.group_ids = group_ids

        # Comment: Automatically assigned when the user segment is created
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: User segment name (localized to the locale of the current user for built-in user segments)
        # Mandatory: no
        # Read-only: no
        # Type: string
        self.name = name

        # Comment: The ids of the organizations that have access
        # Mandatory: no
        # Read-only: no
        # Type: array
        self.organization_ids = organization_ids

        # Comment: The tags a user must have to have access
        # Mandatory: no
        # Read-only: no
        # Type: array
        self.tags = tags

        # Comment: When the user segment was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The set of users who can view content
        # Mandatory: yes
        # Read-only: no
        # Type: string
        self.user_type = user_type

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def created(self):
        """
        |  Comment: When the user segment was created
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def groups(self):
        """
        |  Comment: The ids of the groups that have access
        """
        if self.api and self.group_ids:
            return self.api._get_groups(self.group_ids)

    @groups.setter
    def groups(self, groups):
        if groups:
            self.group_ids = [o.id for o in groups]
            self._groups = groups

    @property
    def organizations(self):
        """
        |  Comment: The ids of the organizations that have access
        """
        if self.api and self.organization_ids:
            return self.api._get_organizations(self.organization_ids)

    @organizations.setter
    def organizations(self, organizations):
        if organizations:
            self.organization_ids = [o.id for o in organizations]
            self._organizations = organizations

    @property
    def updated(self):
        """
        |  Comment: When the user segment was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated


class Vote(BaseObject):
    def __init__(self,
                 api=None,
                 created_at=None,
                 id=None,
                 item_id=None,
                 item_type=None,
                 updated_at=None,
                 url=None,
                 user_id=None,
                 value=None,
                 **kwargs):

        self.api = api

        # Comment: The time at which the vote was created
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.created_at = created_at

        # Comment: Automatically assigned when the vote is created
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.id = id

        # Comment: The id of the item for which this vote was cast
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.item_id = item_id

        # Comment: The type of the item. Can be "Article", "Post" or "PostComment"
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.item_type = item_type

        # Comment: The time at which the vote was last updated
        # Mandatory: no
        # Read-only: yes
        # Type: timestamp
        self.updated_at = updated_at

        # Comment: The API url of this vote
        # Mandatory: no
        # Read-only: yes
        # Type: string
        self.url = url

        # Comment: The id of the user who cast this vote
        # Mandatory: no
        # Read-only: yes
        # Type: integer
        self.user_id = user_id

        # Comment: The value of the vote
        # Mandatory: yes
        # Read-only: no
        # Type: integer
        self.value = value

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def created(self):
        """
        |  Comment: The time at which the vote was created
        """
        if self.created_at:
            return dateutil.parser.parse(self.created_at)

    @created.setter
    def created(self, created):
        if created:
            self.created_at = created

    @property
    def updated(self):
        """
        |  Comment: The time at which the vote was last updated
        """
        if self.updated_at:
            return dateutil.parser.parse(self.updated_at)

    @updated.setter
    def updated(self, updated):
        if updated:
            self.updated_at = updated

    @property
    def user(self):
        """
        |  Comment: The id of the user who cast this vote
        """
        if self.api and self.user_id:
            return self.api._get_user(self.user_id)

    @user.setter
    def user(self, user):
        if user:
            self.user_id = user.id
            self._user = user
