---
title: 'Pony Capabilities made simple'
post_type: 'post'
source: 'https://soyyomakesgames.wordpress.com/2016/10/10/ponys-capabilities-made-simple/'
pub_date: 'Mon, 10 Oct 2016 18:12:52 +0000'
post_date: '2016-10-10 18:12:52'
post_modified_gmt: '2016-10-12 19:11:01'
post_name: 'ponys-capabilities-made-simple'
date: '2016-10-12T19:11:01'
post_id: '141'
tags:
    - soyyomakesgames
    - teenage
    - nerd
---
<span style="color:#999999;">Foreword: I'm still struggling to understand Pony's capabilities and everything below may be just wrong. Also, this article does not replace <a href="http://tutorial.ponylang.org">the tutorial</a>.</span>

For a course on programming languages, we have decided to learn the Pony language. Learning Pony has been something really pleasant and easy until I came across capabilities. Looking for an easy and simple way to understand them, I found this. I call this "The deny properties matrix from hell". Not because it's evil, but because I find it really hard to learn from that diagram and also because it's evil.

[caption id="attachment_160" align="aligncenter" width="989"]<img class=" size-full wp-image-160 aligncenter" src="https://soyyomakesgames.files.wordpress.com/2016/10/matrix-from-hell.png" alt="matrix-from-hell" width="989" height="738" /> Evil. <a href="http://www.doc.ic.ac.uk/~scd/Pony-WG2.16.pdf">Source  </a>[/caption]

Ok, so I know this denying capabilities stuff is very formally correct, but it's too hard to understand. So I re-wrote it thinking about what you <em>allow</em> instead of what you <em>deny</em>, and everything started to make sense. Of course, you can scroll down and see it right now but the idea of this article is to -sort of- deduce it so you can see how obvious and logical everything is.
<h1>About iso and the point of all this</h1>
Two threads can't just share data: writes can happen simultaneously with reads and things get corrupted pretty easily. For two threads to share data, you either:
<ul>
	<li>Only allow both threads to read</li>
	<li>You allow full access to shared data in turns: only Thread A or Thread B can write and read from at a time.</li>
</ul>
Which means: you either share immutable data or <strong>pass</strong> mutable data. Traditionally, passing data is done with locks and mutexes. In pony, this is done with <strong>iso</strong>.

The whole point of pony is that actors send and receive messages, but the content of those messages <strong>must</strong> be either:
<ul>
	<li>opaque: something you can't read nor write to, only identify it. (tag)</li>
	<li>immutable. (val)</li>
	<li>mutable but isolated: If you send the thing you can't <strong>EVER</strong> read from or write to it again. (iso)</li>
</ul>
What's cool about this is that you don't need to copy stuff when you send messages. In other languages, to send data to another thread you either:

a)copy everything you are passing in the message to be sure that the other thread doesn't touch your data.

b)put some locks here and there

In pony, that need vanishes because of reference capabilities.

So <strong>you can share mutable data with iso without copying it and with no mutexes</strong>. That's the point of all this.
<h1>The security scale</h1>
This is sort of obvious, but let's say it:

[caption id="attachment_243" align="aligncenter" width="640"]<img class=" size-full wp-image-243 aligncenter" src="https://soyyomakesgames.files.wordpress.com/2016/10/security-scale.png" alt="security-scale" width="640" height="300" /> The colours[/caption]

We're going to talk about reference capabilities, so just forget about the "No access" part.

<img class="alignnone size-full wp-image-254" src="https://soyyomakesgames.files.wordpress.com/2016/10/security-scale1.png" alt="security-scale" width="640" height="300" />
<h1>Here comes the matrix</h1>
In most papers and talks about Pony, "local" means <em>this thread/actor</em> and "global" means <em>other thread/actor</em>. This is the same matrix as before, just in terms of what you are allowed to do through the reference instead of what you can't do.

<img class="alignnone size-full wp-image-271" src="https://soyyomakesgames.files.wordpress.com/2016/10/capabilities-matrix.png" alt="capabilities-matrix" width="900" height="600" />

Iso and trn are problematic, because as said before it's unsafe for two threads to write to the same data, and for a thread to read data which can be written to by other thread (you can get a data structure that is half-updated!). So iso and trn only make sense if they are <em>unique references</em>. This means that only one actor has access and data never gets corrupted.
<h1>Sendables</h1>
iso, val and tag are the only sendable reference types because what <em>this actor</em> can do to the references is the same as what <em>the other actor</em> can.
<h1>Here comes the Hasse diagram</h1>
<a href="https://tutorial.ponylang.org/capabilities/capability-subtyping.html">Capability subtyping</a>, from the tutorial, establishes which reference types can be assigned to which. You should read that. Here is the Hasse diagram:

<img class="alignnone size-full wp-image-308" src="https://soyyomakesgames.files.wordpress.com/2016/10/hasse.png" alt="hasse" width="640" height="480" />

Note that the Hasse diagram also shows transitivity: box is safer than val and tag is safer that box so tag is safer than val. This means you can:

var number_val:U32 val = 5

var number_tag:U32 tag = number_val

However, you can't just:

var iso_thing:Thing iso = ....

var ref_thing:Thing ref = iso_thing

because of the uniqueness of iso.
<h1>See how it makes sense</h1>
<img class="alignnone size-full wp-image-337" src="https://soyyomakesgames.files.wordpress.com/2016/10/capabilities-matrix-con-hasse.png" alt="capabilities-matrix-con-hasse" width="900" height="600" />

Here I tried to put the hasse diagram on top of the matrix. See how you deny one thing at a time?
<h1>iso only makes sense thanks to consume</h1>
I mentioned how you can't

var ref_thing:Thing ref = iso_thing

this is because of the uniqueness of iso: by performing that assignment, you create a new reference to iso_thing so it's not isolated anymore. Instead, what you must do is:

var ref_thing:Thing ref = consume iso_thing

Consuming iso_thing sort of destroys the reference: you can't use it anymore, it's a compile-time error!
<h1>recover lets you change the reference type (in the other direction)</h1>
With assignments and consume you can only go downwards (I mean down the matrix: from iso to ref, from val to box and such). However, recover blocks let you go upwards (e.g. from ref to iso).

In fact, you can also go downwards and right (just like with assignments)(Thing.create() returns a ref)

var iso_thing:Thing iso = recover Thing.create() end

var val_thing:Thing val = recover Thing.create() end

recover will by default return the topmost reference type (iso, val, tag), which is all you need anyways. You can also specify a target reference type, for example:

var trn_thing:Thing trn = recover <strong>trn</strong> Thing.create() end
<h1>recover isn't cheating</h1>
Inside the recover block you can only access iso, val and tag references from the scope, which ensures thread-safety, as discussed in "about iso and the point of all this".

So no, it's not cheating.
<h1>Final words</h1>
I hope this was useful. Please point out any mistakes in the comments or e-mail me.