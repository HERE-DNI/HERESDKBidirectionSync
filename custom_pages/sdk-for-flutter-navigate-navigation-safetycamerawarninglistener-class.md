---
title: "SafetyCameraWarningListener class abstract"
slug: "sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SafetyCameraWarningListener-class.html -->


<div>
<h1>SafetyCameraWarningListener class abstract</h1></div>

<p>This abstract class
should be implemented in order to receive notifications on safety cameras.</p>
<p>A <code>SafetyCameraWarning</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>SafetyCameraWarning</code> 120 meters and <code>SafetyCameraWarning</code> 160 meters ahead,
the first <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is 120 meters
and the next <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>
<p>When <code>SafetyCameraWarningListener</code> is enabled, a new set of text notifications (e.g. "Speed camera ahead") will be trigger if any has been also enabled.
The updates for the same safety camera appear in order of the initial <code>DistanceType.AHEAD</code> event.
That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-safetycamerawarninglistener">SafetyCameraWarningListener</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-onsafetycamerawarningupdated">onSafetyCameraWarningUpdated</a></li><li><a href="/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
