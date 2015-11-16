Data Model Planning
===================

People
======

Organization
------------

- Has Users
- Is controlled by one or more Admins (type of User, most likely the one who creates the Organization) who add Users, create Networks and accept/send Network invitations.

Admins
------

- Can add or remove uses
- Can create a network
- Can invite any other network to a network

User
----

- A User is a member of an Organization. 
- A User can be assigned to multiple Series and Stories.
- A User’s role can be different across all of these things.
- A User has a name, phone, email, short bio, profile photo, social media profile links.
- Most Users can do most things

Network
-------

- An Organization can be a part of none, one or more Networks consisting of their own Organization and other Organizations.
- If an Organization is in a Network with another Organization, Users on a Story or Series have the option to grant access (Share or Collaborate) with that Organization (and that means all of its Users)
- An Organization can be part of one or many distinct or overlapping Networks.
- If Organizations are linked by a Network, they can see a list of available Network content that has been marked for sharing.

Communication
-------------

- Team members can speak via Comments on Series Planning, Story Planning and Facets. 
- Users should also be able to message each other one-on-one.

Content
=======

Series
------

- A Series is a collection of Stories on a related topic.
- Any Story can be added to a Series.
A series has:
- Planning: all of the documents (uploaded), notes (text input) and comments around the planning and implementation of a series.
- Assets: photos, video, documents or audio that could be used in any Story.

Stories
-------

- A Story is piece of content on a specific topic.
- A Story is a bundle of related Facets
- A Story has:
- Planning: all of the documents (uploaded), notes (text input) and comments around the planning and implementation of a Story.
- Assets: photos, video, documents or audio that will be used in any of the facets of the Story.
- Meta: Common information that is true no matter what the Facet is.
Comments: All of the comments around the editing of the Facets. (displayed next to the text editor) 

*Note:* Sharing, collaborating, embargo and sensitivity are tracked at a story level

Facets
------

- Is a platform specific version of a story
- WebFacet, PrintFacet, VideoFacet, AudioFacet
- Each Facet has associated Meta specific to the kind of Facet it is
- Each Facet has three saves worth of revision history

*Notes:* Facets need to have their own status, edit datetime, run datetime and credit. Facets are frequently not created at the same time. Facets must display individually on the dashboard for correct filtering. Dashboard shows content on a facet level, the story is the link between facets

WebFacet
--------

- Has an author, editor (not required), title, summary, tags, text of the content, access to assets, comments.
- Has it’s own status, due date, publish date, edit history

PrintFacet
----------

- Has an author, editor (not required), headline, summary, wordcount, (maybe a section or page#), text of the content, access to assets, comments.
- Has it’s own status, due date, publish date, edit history

VideoFacet
----------

- Has producer, director, summary, text of scripts, access to assets, runtime, crew notes (optional), comments.
- Has it’s own status, run date, publish date, edit history

AudioFacet
----------

- Has producer, slug, summary, script, access to assets, runtime, comments.
- Has it’s own status, run date, publish date, edit history
