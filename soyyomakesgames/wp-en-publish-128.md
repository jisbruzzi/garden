---
title: 'Class to modify the speed of a sound: AS3'
post_type: 'post'
source: 'https://soyyomakesgames.wordpress.com/2013/01/01/class-to-modify-the-speed-of-a-sound-as3/'
pub_date: 'Tue, 01 Jan 2013 14:40:52 +0000'
post_date: '2013-01-01 14:40:52'
post_modified_gmt: '2013-01-01 14:40:52'
post_name: 'class-to-modify-the-speed-of-a-sound-as3'
date: '2013-01-01T14:40:52'
post_id: '128'
tags:
    - soyyomakesgames
    - teenage
    - nerd
---
For the game I am making, I needed a class to change the duration and frequency of a sound, as there is the possibility to slow down time.

My first solution was to use this code: http://www.mcfunkypants.com/2011/as3-pitch-shift-mp3/. But it came out being extremely hard to read and modify. I expended all my day (I think almost 9 hours) trying to simply add the capability of playing not-looping sounds, wich this class didn't include. That was because of how unclear the code was to me: it has almost no comments at all, and the loop inside the onSampleData event is just unreadable.

I must add that, althought the code was supposed to play sound effects in a game, it's very poor in performance, so when you play more than one FrequencyChangeSound at the same time, your game could get some low FPSs.  I'll program a sound player class to do one single onSampleData event (instead of one for each sound), and get better performance.

&nbsp;

So here's the code:

https://gist.github.com/4424117