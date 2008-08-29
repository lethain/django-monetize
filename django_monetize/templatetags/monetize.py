"""
Contains the template tags used to facilitate the django_monetize app.

Usage (from within a template):

    {% load monetize %}
    
    {% monetize-slot "top" object.tags %}

    <p> Some content. </p>
    {% monetize-slot "bottom" request.META.HTTP_USER_AGENT %}

    <div class="sidebar">
    {% monetize-slot "side bar" request.META object.tags "django" %}
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

