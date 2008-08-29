
## Overview of ``django-monetize``

``django-monetize`` a Django application that intends to facilitate optimizing website monetization. It has a two tiered approach to this:

1.  Supporting a wide variety of monetization options: advertising, amazon affiliates, donations and custom made ads.

2. Allow a high degree of context-based targeting and customization.

Lets give some examples of what ``django-monetize`` can do.

### A Hypothetical Case Study: Will Larson and His Blog

In a far away universe, long long ago, there was a blogger and Django developer named Will Larson. He enjoyed blogging very much, but began to wonder why he spent so much time blogging when his blog didn't even cover its hosting fees. Since he used a VPS for hosting, and only got 20-30k pageviews per month he knew any strategy as simply as throwing Google AdSense on his page wasn't going to be sufficient.

Worse yet, he was well aware that much of his traffic was from programmers and other technological types, and that they were afflicted with a blight called ad... ad... well, whatever it was called, they never even noticed ads on most pages.

However, he knew that these tech types liked to purchase technical books, and that also that some individuals might even appreciate particularly indepth tutorials enough to donate a few coins his way.

The problem was that he wanted to advertise different books for different topics, and only wanted to ask for donations for particularly long works. He was very, very sad.

Thankfully, one day he found a leprechaun in the bushes nearby his home. The leprechaun offered him one wish, and he wished for riches. The wise leprechaun knew if he gave Will a fortune, he might not be wise enough to invest it in the turmultuous stock market, and instead he gave him a gift that would allow him to reap riches for years to come: ``django-monetize``.

Using ``django-monetize``, Will was able to do some amazing things. He was already tagging his contents, and was able to display different monetization techniques depending on the tag for the current content being displayed. For articles in a series about PyObjC, he was able to display a donation box pleading for relief from his intense poverty for anyone who found his epic tutorial helpful. For blog entries tagged with Django he was able to advertise a custom ad for the Django Book. For blog entries tagged with cooking he was able to just use ad sense, since people who read about cooking might not be the afflicted with the cruel plague of ad blindness.

Everyone lived happily ever after.

The end.


## High Level Overview

TBA

## Installation

1. Add the ``django_monetize`` to your Python path. Likely your site folder.
2. Add ``django_monetize`` to your ``INSTALLED_APPS`` setting in your ``settings.py`` file.
3. ?
4. Profit.

## Configuration

One of the key focuses of ``django_monetize`` is to support a high degree of targetting. The logic for that targetting is stored in the ``MONETIZE_TARGET`` and ``MONETIZE_DEFAULT`` values in your project's settings.py file.

For example, consider the simplest situation where you wanted to display AdSense ad units in all monetization slots:

    MONETIZE_DEFAULT = 'django_monetize/adsense_ad_unit.html'

Now lets say you want to display a link to an Amazon Affiliate's search results page when targetted on a list containing ``django`` (and otherwise default back to an Adsense ad unit):

    MONETIZE_TARGET = {
        'django':['django_monetize/amazon_search.html',('amazon_search_terms','Django books'),('amazon_search_title','Buy some Django books today!')],
    }
    MONETIZE_DEFAULT = 'django_monetize/adsense_ad_unit.html'

If you specify a monetization method using a list/tuple instead of a string, then the zeroth value is the template's string, and the remaining values are 2-tuples (or 2-lists) containing a key and a value, which are used to overwrite values in ``MONETIZE_CONTEXT`` for this specfic monetization.

Now lets say you have three ad slots on your page: 'header','footer', and 'side'. You can customize the contents of each slot for each term. For this example, lets not show any ads by default.

    MONETIZE_TARGET = {
        'django':{
            'header':'django_monetize/adsense_ad_unit.html',
            'footer':'django_monetize/slicehost_referral.html',
            None:'django_monetize/dreamhost_referral.html',
            # Value for None specifies value for non-listed slots.
	    # if you don't specify an ad for a slot, and don't specify
            # a value default, then it won't display an ad.
        },
    }
    MONETIZE_DEFAULT = False

Specifying an ad you either pass a string with the ads template, or you pass a list (or tuple) where the zeroth object is the template's string and the other objects are parameters for the rendering function. Whether or not a specific monetization option takes parameters varies, so you'll have to consult the documentation (or the source, if documentation is lacking).

## Monetizaton Options

Here are some monetizations that already have built-in support. If you can't find what you're looking for, remember that you can always roll your own!

### Amazon Affiliates: Custom Link

Use this template along with your Amazon Affiliates account to create referral links for arbitrary Amazon URLs.

Uses the ``amazon_custom_link.html`` template, and requires the ``amazon_affiliates_id``, ``amazon_custom_link_title``, and ``amazon_custom_link_url`` values in the ``MONETIZE_CONTEXT`` dictionary.

    MONETIZE_CONTEXT = {
        'amazon_affiliates_id='yourAffiliatesID',
        'amazon_custom_link_title':'Look at the Kindle!',
        'amazon_custom_link_url':'http://www.amazon.com/etc/etc',
    }
    MONETIZE_DEFAULT = 'django_monetize/amazon_custom_link.html'

Is surrounded by a div with CSS class ``amazon_custom_link``.

### Amazon Affiliates: Omakase

Amazon Affiliate's Omakase widget (Japanese for 'leave it to us') creates and displays a banner that is targeted for your page's content, without you doing any work.

It requires one settings in the ``MONETIZE_CONTENT`` dictionary: ``amazon_affiliates_id``, and uses the ``django_monetize/amazon_omakase.html`` template.

Example:

    MONETIZE_CONTEXT = {
        'amazon_affiliates_id':'yourAffiliatesID',
    }
    # use default 728 width by 90 height values
    MONETIZE_DEFAULT = 'django_monetize/amazon_omakase.html'
    # You can customize width/height, but must be one of these pairs:
    # 120x600, 120x240, 160x600, 180x150, 468x60, 300x250, 600x520
    MONETIZE_DEFAULT = ['django_monetize/amazon_omakase.html',120,600]

Surrounded by div with CSS class ``amazon_makase``.


### Amazon Affiliates: Search Links

For an Amazon Affiliate link to a search of Amazon's offerings.

Uses the ``django_monetize/amazon_search.html`` template, and in the ``MONETIZE_CONTEXT`` dictionary it requires values ``amazon_affiliates_id``, ``amazon_search_terms`` and ``amazon_search_title``.

Example:

    MONETIZE_CONTEXT = {
        'amazon_affiliates_id':'my_tracking_id',
        'amazon_search_terms':'Django book',
        'amazon_search_title':'Buy Django books on Amazon.com!',
    }
    MONETIZE_DEFAULT = "django_monetize/amazon_search.html"

Is surrounded by a div with CSS class ``amazon_search``.

### Amazon Honor System

[Amazon Honor System](http://zme.amazon.com/) allows easy donations.

In the ``MONETIZE_CONTEXT`` dict in your ``settings.py`` file you'll need to specify your paypage url as the value for key ``amazon_paypage``.

Specify ``django_monetize/amazon_honor.html`` as the template to use the default Amazon honor request.

Example:

    MONETIZE_CONTEXT = {
        'amazon_paypage':'http://www.amazon.com/pagepage/some-random-has/'
    }
    MONETIZE_DEFAULT = "django_monetize/amazon_honor.html"

Surrounded by div with CSS class ``amazon_donate``.

### Dreamhost Referrals

You can use Dreamhost referrals as a monetization option as well. At least theoretically. If you have no shame. And live life with a sadistic streak.

Uses the ``django_monetize/dreamhost_referral.html`` template. But... well, you'll see. You may want to rewrite it.

Requires the ``dreamhost_referral_code`` value in the ``MONETIZE_CONTEXT`` dictionary.

Example:

    MONETIZE_CONTEXT = {
        'dreamhost_referral_code':'123456',
    }
    MONETIZE_DEFAULT = "django_monetize/dreamhost_referral.html"

Is wrapped in a div with the ``dreamhost_referral`` CSS class.

### Google Adsense: Ad Unit

Use this monetization option to display one unit of Google ads (not a link box).

Uses the template ``django_monetize/adsense_ad_unit.html``.

Requires the ``adsense_ad_unit_client``, ``adsense_ad_unit_slot``, ``adsense_ad_width``, and ``adsense_ad_height`` values in the ``MONETIZE_CONTEXT`` dictionary.

Example:

    MONETIZE_CONTEXT = {
        'adsense_ad_unit_client':'ad client id',
        'adsense_ad_unit_slot':'ad unit slot',
        'adsense_ad_unit_width':336,
        'adsense_ad_unit_height':280,
    }
    MONETIZE_DEFAULT = "django_monetize/adsense_ad_unit.html``

### Paypal Donations

If you have a [PayPal](http://www.paypal.com) account, another option for monetization is using PayPal donations.

In your settings.py's ``MONETIZE_CONTEXT`` dict you'll need to specify a handful of values to use this option: ``paypal_business``, ``paypal_item_name``, ``paypal_currency_code``, ``paypal_tax``, ``paypal_lc``, ``paypal_bn``, and ``paypal_image``. The value ``paypal_amount`` is optional, and may be used to specify the size of the donation, otherwise the amount is up to the donator.

It uses the ``django_monetize/paypal_donate.html`` template.

Example:

    MONETIZE_CONTEXT = {
        'paypal_business':'your_paypal_account@gmail.com',
        'paypal_item_name':'My Awesome Website',
        'paypal_currency_code':'USD',
        'paypal_amount': '5.00', # optional
        'paypal_tax':'0',
        'paypal_lc':'US',
        'paypal_bn':'PP-DonationsBF',
        'paypal_image':'http://www.paypal.com/en_US/i/btn/btn_donate_LG.gif'
    }
    MONETIZE_DEFAULT = "django_monetize/paypal_donate.html"

Surrounded by div with CSS class ``paypal_donate``.

### SliceHost Referals

For those of us using SliceHost, we know there isn't a better VPS on the planet. Since we like to share that joy, sometimes we like send a few referrals their way.

Uses the ``django_monetize/slicehost_referral.html`` template.

Requires the ``slicehost_referral_id`` value in the ``MONETIZE_CONTEXT`` dictionary. It is the id at the end of the link if login to your SliceHost account, go to the ``Acount`` section, and then click on ``Referrals``. (The number after the question mark near the end of the url.)

Example:

    MONETIZE_CONTEXT = {
        'slicehost_referral_id':'123456789',
    }
    MONTIZE_DEFAULT = "slicehost_referral.html"

Is surrounded by a div with the CSS class ``slicehost_referral``.
    
