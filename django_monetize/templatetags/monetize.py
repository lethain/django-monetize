"""
Contains the template tags used to facilitate the django_monetize app.

Usage (from within a template):

    {% load monetize %}
    
    {% monetize_slot "top" object.tags %}

    <p> Some content. </p>
    {% monetize_slot "bottom" request.META.HTTP_USER_AGENT %}

    <div class="sidebar">
    {% monetize_slot "side bar" request.META object.tags "django" %}
    </div>


In the first of those examples we are targeting monetization using an object's tags, and in the second example we are targeting monetization using a request's user agent.

The third example (at the "side bar" slot) shows passing an arbitrary number of dictionaries, lists and strings into the slot. Excluding the first parameter, which is the name of the slot, they will be systematically searched for values specified in your ``MONETIZE_TARGET`` dictionary.

The first value matching a targeting value will be used. Values will be matched as follows:

1.  It will sensibly match against the contents of lists, tuples
    and dictionaries, but **all other objects will be matched by
    using the value returned by their __repr__ method**.

2.  **String/Unicode objects** will be matched against the keys
    in the ``MONETIZE_TARGET`` dictionary. (If you specify "django"
    it will check for a key named "django" and use its targeting logic.)

3.  **Lists/Tuples** will be stepped through, with each value being checked against the keys in the ``MONETIZE_TARGET`` dictionary.

4.  **Dictionaries** will be replaced by a list of their items, which will then be processed normally as a list.

5.  The **None** value will be ignored.

6.  If there are no matches, then the system will fall back onto the ``MONETIZE_DEFAULT`` value. If ``MONETIZE_DEFAULT`` is not specified (or its value is NONE) then it will simply return an empty string.


Don't be fooled by the above example: ``django_monetize`` doesn't help you inject ``request`` into your templates' context; you'll have to handle that yourself.
"""

from django import template
from django.conf import settings

register = template.Library()

@register.tag(name="monetize_slot")
def monetize_slot(parser, token):
    'Template tag for displaying a monetization option in a slot.'
    lst = token.split_contents()
    return MonetizeSlotNode(*lst[1:])


class MonetizeSlotNode(template.Node):
    def __init__(self, *vals):
        if len(vals) > 0:
            self.slot = vals[0].strip('"')
            self.params = vals[1:]
        else:
            self.slot = None
            self.params = ()

    def render(self,context):
        'Apply targeting and render monetization option for value/slot combo.'
        target = self.acquire_target(self.params,context)
        return self.target(target,self.slot,context)

    def acquire_target(self,params,context):
        'Go through parameters and try to find a valid targeting parameter.'
        logic_dict = getattr(settings,'MONETIZE_TARGET',{})

        for param in params:
            try:
                param = template.resolve_variable(param,context)
            except template.VariableDoesNotExist:
                pass
            if type(param) == dict:
                param = dict.iteritems()

            if hasattr(param,'__iter__'):
                for x in param:
                    x = unicode(x)
                    if logic_dict.has_key(x):
                        return x
            else:
                param = unicode(param)
                if logic_dict.has_key(param):
                    return param

        return None

    def target(self,value,slot,context):
        '''
        Returns the rendered text for 'value'. 'value' should be
        the output of the 'choose_target' method.

        Also be aware the distinction being made between
        False and None. None refers to the concept of using
        the default monetization option, while False refers
        to not using a monetization option.
        '''
        logic_dict = getattr(settings,'MONETIZE_TARGET',{})
        if logic_dict.has_key(value):
            logic = logic_dict[value]
        else:
            logic = getattr(settings,"MONETIZE_DEFAULT",False)

        # Deconstruct slot specific logic from dict.
        if type(logic) == dict:
            if logic.has_key(slot):
                # Check for slot specific logic.
                logic = logic[slot]
            elif logic.has_key(None):
                # Check for value specific default logic.
                logic = logic[None]
            else:
                # Otherwise display nothing.
                logic = False

        if type(logic) == tuple or type(logic) == list:
            context_dict = getattr(settings,'MONETIZE_CONTEXT',{}).copy()
            if len(logic) == 0:
                logic = False
            else:
                # load extra context from list
                for key,val in logic[1:]:
                    context_dict[key] = val
                logic = logic[0]
        else:
            context_dict = getattr(settings,'MONETIZE_CONTEXT',{})

        # At this point ``logic`` should be a string for a template, or False
        if logic == False:
            # False means no monetization option, so return empty string.
            rendered = u""
        else:
            new_context = template.Context(context_dict,context.autoescape)
            t = template.loader.get_template(logic)
            rendered = t.render(new_context)

        return rendered
