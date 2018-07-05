from zenpy.lib.api_objects import BaseObject
import dateutil.parser


class Account(BaseObject):
    def __init__(self,
                 api=None,
                 account_key=None,
                 billing=None,
                 create_date=None,
                 plan=None,
                 status=None,
                 **kwargs):

        self.api = api

        # Description: The widget key for the account
        # Read-only: yes
        # Type: string
        self.account_key = account_key

        # Description: The billing information of the account
        # Read-only: no
        # Type: :class:`email`
        self.billing = billing

        # Description: The date of creation of the account
        # Read-only: yes
        # Type: timestamp
        self.create_date = create_date

        # Description: Information about the package of the account
        # Read-only: yes
        # Type: :class:`dictionary`
        self.plan = plan

        # Description: The status of the account
        # Read-only: yes
        # Type: string
        self.status = status

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Agent(BaseObject):
    def __init__(self,
                 api=None,
                 create_date=None,
                 departments=None,
                 display_name=None,
                 email=None,
                 enabled=None,
                 first_name=None,
                 id=None,
                 last_login=None,
                 last_name=None,
                 login_count=None,
                 roles=None,
                 **kwargs):

        self.api = api

        # Description: The date of creation of the agent
        # Read-only: yes
        # Type: timestamp
        self.create_date = create_date

        # Description: The departments for the agent
        # Read-only: yes
        # Type: array
        self.departments = departments

        # Description: The name to be displayed for the agent
        # Read-only: no
        # Type: string
        self.display_name = display_name

        # Description: The email ID of the agent
        # Read-only: no
        # Type: integer
        self.email = email

        # Description: Describes whether the agent is enabled
        # Read-only: no
        # Type: integer
        self.enabled = enabled

        # Description: The agent's first name
        # Read-only: no
        # Type: string
        self.first_name = first_name

        # Description: The ID of the agent
        # Read-only: yes
        # Type: integer
        self.id = id
        self.last_login = last_login

        # Description: The agent's last name
        # Read-only: no
        # Type: string
        self.last_name = last_name
        self.login_count = login_count

        # Description: Special role privileges. See below for values (deprecated)
        # Read-only: yes
        # Type: object
        self.roles = roles

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Ban(BaseObject):
    def __init__(self, api=None, ip_address=None, visitor=None, **kwargs):

        self.api = api

        # Description: The IP address of the banned visitor
        # Read-only: yes
        # Type: string
        self.ip_address = ip_address
        self.visitor = visitor

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Billing(BaseObject):
    def __init__(self,
                 api=None,
                 additional_info=None,
                 address1=None,
                 address2=None,
                 city=None,
                 company=None,
                 country_code=None,
                 email=None,
                 first_name=None,
                 last_name=None,
                 postal_code=None,
                 state=None,
                 **kwargs):

        self.api = api
        self.additional_info = additional_info
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.company = company
        self.country_code = country_code
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code
        self.state = state

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Chat(BaseObject):
    def __init__(self,
                 api=None,
                 agent_ids=None,
                 agent_names=None,
                 comment=None,
                 count=None,
                 department_id=None,
                 department_name=None,
                 duration=None,
                 history=None,
                 id=None,
                 missed=None,
                 rating=None,
                 referrer_search_engine=None,
                 referrer_search_terms=None,
                 response_time=None,
                 session=None,
                 started_by=None,
                 tags=None,
                 triggered=None,
                 triggered_response=None,
                 type=None,
                 unread=None,
                 visitor=None,
                 webpath=None,
                 zendesk_ticket_id=None,
                 **kwargs):

        self.api = api

        self._end_timestamp = None

        # Description: Timestamp for the chat
        # Read-only: yes
        # Type: timestamp

        self._timestamp = None

        # Description: IDs of agents involved in the chat
        # Read-only: yes
        # Type: array
        self.agent_ids = agent_ids

        # Description: Names of agents involved in the chat
        # Read-only: yes
        # Type: array
        self.agent_names = agent_names

        # Description: The customer comment on the chat
        # Read-only: no
        # Type: string
        self.comment = comment

        # Description: Number of messages (each) by the visitor and the agent(s)
        # Read-only: yes
        # Type: object
        self.count = count

        # Description: The ID of the department to which the chat is directed
        # Read-only: yes
        # Type: integer
        self.department_id = department_id

        # Description: The name of the department to which the chat is directed
        # Read-only: yes
        # Type: integer
        self.department_name = department_name

        # Description: Duration of the chat
        # Read-only: yes
        # Type: timestamp
        self.duration = duration

        # Description: Chronological list of messages in the chat
        # Read-only: yes
        # Type: array
        self.history = history

        # Description: The ID of the chat
        # Read-only: yes
        # Type: string
        self.id = id

        # Description: Whether the chat was missed or not
        # Read-only: yes
        # Type: boolean
        self.missed = missed

        # Description: The customer satisfaction rating for the chat
        # Read-only: no
        # Type: string
        self.rating = rating
        self.referrer_search_engine = referrer_search_engine
        self.referrer_search_terms = referrer_search_terms

        # Description: Statistics about the response times in the chat, avg, max and first
        # Read-only: yes
        # Type: object
        self.response_time = response_time

        # Description: Information related to the session of the session of the chat
        # Read-only: yes
        # Type: object
        self.session = session

        # Description: Who started the chat. Can be one of visitor, agent or trigger
        # Read-only: yes
        # Type: string
        self.started_by = started_by

        # Description: Tags associated with the chat
        # Read-only: no
        # Type: array
        self.tags = tags

        # Description: Whether the chat was a triggered chat or not
        # Read-only: yes
        # Type: boolean
        self.triggered = triggered

        # Description: Whether the response was a triggered response or not
        # Read-only: yes
        # Type: boolean
        self.triggered_response = triggered_response

        # Description: Chat type. One of offline_msg, chat
        # Read-only: yes
        # Type: string
        self.type = type

        # Description: Whether the chat is unread
        # Read-only: no
        # Type: boolean
        self.unread = unread

        # Description: Information about the visitor
        # Read-only: yes
        # Type: object
        self.visitor = visitor

        # Description: The list of pages the customer navigated to during the chat
        # Read-only: yes
        # Type: array
        self.webpath = webpath

        # Description: The ID of the Zendesk Support ticket created from this chat. Available only if using version 2 of the Zendesk Chat-Support integration
        # Read-only: yes
        # Type: integer
        self.zendesk_ticket_id = zendesk_ticket_id

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def end_timestamp(self):

        if self._end_timestamp:
            return dateutil.parser.parse(self._end_timestamp)

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        if end_timestamp:
            self._end_timestamp = end_timestamp

    @property
    def timestamp(self):
        """
        |  Description: Timestamp for the chat
        """
        if self._timestamp:
            return dateutil.parser.parse(self._timestamp)

    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp:
            self._timestamp = timestamp

    @property
    def agents(self):
        """
        |  Description: IDs of agents involved in the chat
        """
        if self.api and self.agent_ids:
            return self.api._get_agents(self.agent_ids)

    @agents.setter
    def agents(self, agents):
        if agents:
            self.agent_ids = [o.id for o in agents]
            self._agents = agents

    @property
    def department(self):
        """
        |  Description: The ID of the department to which the chat is directed
        """
        if self.api and self.department_id:
            return self.api._get_department(self.department_id)

    @department.setter
    def department(self, department):
        if department:
            self.department_id = department.id
            self._department = department

    @property
    def zendesk_ticket(self):
        """
        |  Description: The ID of the Zendesk Support ticket created from this chat. Available only if using version 2 of the Zendesk Chat-Support integration
        """
        if self.api and self.zendesk_ticket_id:
            return self.api._get_zendesk_ticket(self.zendesk_ticket_id)

    @zendesk_ticket.setter
    def zendesk_ticket(self, zendesk_ticket):
        if zendesk_ticket:
            self.zendesk_ticket_id = zendesk_ticket.id
            self._zendesk_ticket = zendesk_ticket


class Count(BaseObject):
    def __init__(self,
                 api=None,
                 agent=None,
                 total=None,
                 visitor=None,
                 **kwargs):

        self.api = api
        self.agent = agent
        self.total = total
        self.visitor = visitor

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Definition(BaseObject):
    def __init__(self,
                 api=None,
                 actions=None,
                 condition=None,
                 event=None,
                 **kwargs):

        self.api = api
        self.actions = actions
        self.condition = condition
        self.event = event

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Department(BaseObject):
    def __init__(self,
                 api=None,
                 description=None,
                 enabled=None,
                 id=None,
                 members=None,
                 name=None,
                 settings=None,
                 **kwargs):

        self.api = api

        # Description: The description of the department
        # Read-only: no
        # Type: string
        self.description = description

        # Description: Describes whether the department is enabled
        # Read-only: no
        # Type: integer
        self.enabled = enabled

        # Description: The ID of the department
        # Read-only: yes
        # Type: integer
        self.id = id

        # Description: The member agent IDs for the account
        # Read-only: no
        # Type: array
        self.members = members

        # Description: The name of the department
        # Read-only: no
        # Type: string
        self.name = name

        # Description: The settings for the department
        # Read-only: no
        # Type: object
        self.settings = settings

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Goal(BaseObject):
    def __init__(self,
                 api=None,
                 attribution_model=None,
                 attribution_period=None,
                 description=None,
                 enabled=None,
                 id=None,
                 name=None,
                 settings=None,
                 **kwargs):

        self.api = api

        # Description: Describes the attribution model associated with the goal. One of first_touch, last_touch
        # Read-only: no
        # Type: string
        self.attribution_model = attribution_model

        # Description: Describes the attribution period in days for this goal. Range between 1 to 30
        # Read-only: no
        # Type: integer
        self.attribution_period = attribution_period

        # Description: The description of the goal
        # Read-only: no
        # Type: string
        self.description = description

        # Description: Describes whether the goal is enabled
        # Read-only: no
        # Type: integer
        self.enabled = enabled

        # Description: The ID of the goal
        # Read-only: yes
        # Type: integer
        self.id = id

        # Description: The name of the goal
        # Read-only: no
        # Type: string
        self.name = name

        # Description: The settings for the goal. Contains the conditions array (described below).
        # Read-only: no
        # Type: object
        self.settings = settings

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class IpAddress(BaseObject):
    def __init__(self,
                 api=None,
                 id=None,
                 ip_address=None,
                 reason=None,
                 type=None,
                 **kwargs):

        self.api = api
        self.id = id
        self.ip_address = ip_address
        self.reason = reason
        self.type = type

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class OfflineMessage(BaseObject):
    def __init__(self,
                 api=None,
                 department_id=None,
                 department_name=None,
                 id=None,
                 message=None,
                 session=None,
                 type=None,
                 unread=None,
                 visitor=None,
                 zendesk_ticket_id=None,
                 **kwargs):

        self.api = api

        self._timestamp = None
        self.department_id = department_id
        self.department_name = department_name
        self.id = id
        self.message = message
        self.session = session
        self.type = type
        self.unread = unread
        self.visitor = visitor
        self.zendesk_ticket_id = zendesk_ticket_id

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def timestamp(self):

        if self._timestamp:
            return dateutil.parser.parse(self._timestamp)

    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp:
            self._timestamp = timestamp

    @property
    def department(self):

        if self.api and self.department_id:
            return self.api._get_department(self.department_id)

    @department.setter
    def department(self, department):
        if department:
            self.department_id = department.id
            self._department = department

    @property
    def zendesk_ticket(self):

        if self.api and self.zendesk_ticket_id:
            return self.api._get_zendesk_ticket(self.zendesk_ticket_id)

    @zendesk_ticket.setter
    def zendesk_ticket(self, zendesk_ticket):
        if zendesk_ticket:
            self.zendesk_ticket_id = zendesk_ticket.id
            self._zendesk_ticket = zendesk_ticket


class Plan(BaseObject):
    def __init__(self,
                 api=None,
                 agent_leaderboard=None,
                 agent_reports=None,
                 analytics=None,
                 chat_reports=None,
                 daily_reports=None,
                 email_reports=None,
                 file_upload=None,
                 goals=None,
                 high_load=None,
                 integrations=None,
                 ip_restriction=None,
                 long_desc=None,
                 max_advanced_triggers=None,
                 max_agents=None,
                 max_basic_triggers=None,
                 max_concurrent_chats=None,
                 max_departments=None,
                 max_history_search_days=None,
                 monitoring=None,
                 name=None,
                 operating_hours=None,
                 price=None,
                 rest_api=None,
                 short_desc=None,
                 sla=None,
                 support=None,
                 unbranding=None,
                 widget_customization=None,
                 **kwargs):

        self.api = api
        self.agent_leaderboard = agent_leaderboard
        self.agent_reports = agent_reports
        self.analytics = analytics
        self.chat_reports = chat_reports
        self.daily_reports = daily_reports
        self.email_reports = email_reports
        self.file_upload = file_upload
        self.goals = goals
        self.high_load = high_load
        self.integrations = integrations
        self.ip_restriction = ip_restriction
        self.long_desc = long_desc
        self.max_advanced_triggers = max_advanced_triggers
        self.max_agents = max_agents
        self.max_basic_triggers = max_basic_triggers
        self.max_concurrent_chats = max_concurrent_chats
        self.max_departments = max_departments
        self.max_history_search_days = max_history_search_days
        self.monitoring = monitoring
        self.name = name
        self.operating_hours = operating_hours
        self.price = price
        self.rest_api = rest_api
        self.short_desc = short_desc
        self.sla = sla
        self.support = support
        self.unbranding = unbranding
        self.widget_customization = widget_customization

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class ResponseTime(BaseObject):
    def __init__(self, api=None, avg=None, first=None, max=None, **kwargs):

        self.api = api
        self.avg = avg
        self.first = first
        self.max = max

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Roles(BaseObject):
    def __init__(self, api=None, administrator=None, owner=None, **kwargs):

        self.api = api
        self.administrator = administrator
        self.owner = owner

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class SearchResult(BaseObject):
    def __init__(self,
                 api=None,
                 id=None,
                 preview=None,
                 type=None,
                 url=None,
                 **kwargs):

        self.api = api

        self._timestamp = None
        self.id = id
        self.preview = preview
        self.type = type
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
    def timestamp(self):

        if self._timestamp:
            return dateutil.parser.parse(self._timestamp)

    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp:
            self._timestamp = timestamp


class Session(BaseObject):
    def __init__(self,
                 api=None,
                 browser=None,
                 city=None,
                 country_code=None,
                 country_name=None,
                 end_date=None,
                 id=None,
                 ip=None,
                 platform=None,
                 region=None,
                 start_date=None,
                 user_agent=None,
                 **kwargs):

        self.api = api
        self.browser = browser
        self.city = city
        self.country_code = country_code
        self.country_name = country_name
        self.end_date = end_date
        self.id = id
        self.ip = ip
        self.platform = platform
        self.region = region
        self.start_date = start_date
        self.user_agent = user_agent

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Shortcut(BaseObject):
    def __init__(self,
                 api=None,
                 message=None,
                 name=None,
                 options=None,
                 tags=None,
                 **kwargs):

        self.api = api

        # Description: The message of the shortcut
        # Read-only: no
        # Type: string
        self.message = message

        # Description: The name of the shortcut
        # Read-only: no
        # Type: integer
        self.name = name

        # Description: Options for the shortcut
        # Read-only: no
        # Type: integer
        self.options = options

        # Description: List of tags that will be added to chat if the shortcut is used
        # Read-only: no
        # Type: array
        self.tags = tags

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Trigger(BaseObject):
    def __init__(self,
                 api=None,
                 definition=None,
                 description=None,
                 enabled=None,
                 name=None,
                 **kwargs):

        self.api = api
        self.definition = definition

        # Description: The description of the trigger
        # Read-only: no
        # Type: string
        self.description = description

        # Description: Whether the trigger is enabled or not
        # Read-only: no
        # Type: integer
        self.enabled = enabled

        # Description: The name of the trigger
        # Read-only: no
        # Type: string
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Visitor(BaseObject):
    def __init__(self,
                 api=None,
                 email=None,
                 id=None,
                 name=None,
                 notes=None,
                 phone=None,
                 **kwargs):

        self.api = api

        # Description: The email ID of the visitor
        # Read-only: no
        # Type: :class:`email`
        self.email = email

        # Description: The ID of the visitor
        # Read-only: yes
        # Type: integer
        self.id = id

        # Description: The name to be displayed for the visitor
        # Read-only: no
        # Type: string
        self.name = name

        # Description: Any additional notes about the visitor
        # Read-only: yes
        # Type: string
        self.notes = notes

        # Description: The phone number of the visitor (if available)
        # Read-only: no
        # Type: integer
        self.phone = phone

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue


class Webpath(BaseObject):
    def __init__(self, api=None, from_=None, title=None, to=None, **kwargs):

        self.api = api

        self._timestamp = None
        self.from_ = from_
        self.title = title
        self.to = to

        for key, value in kwargs.items():
            setattr(self, key, value)

        for key in self.to_dict():
            if getattr(self, key) is None:
                try:
                    self._dirty_attributes.remove(key)
                except KeyError:
                    continue

    @property
    def timestamp(self):

        if self._timestamp:
            return dateutil.parser.parse(self._timestamp)

    @timestamp.setter
    def timestamp(self, timestamp):
        if timestamp:
            self._timestamp = timestamp
