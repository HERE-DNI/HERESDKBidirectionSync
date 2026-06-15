---
title: "RealisticViewWarning class"
slug: "sdk-for-flutter-navigate-navigation-realisticviewwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RealisticViewWarning-class.html -->


<div>
<h1>RealisticViewWarning class</h1></div>

<p>A realistic view notification.</p>
<p>This notification is given for complex junctions and it includes a visual
representation of that junction, in order to help the user to better navigate it. When
<code>RealisticViewWarning.distanceType</code> is <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a>, the <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage">RealisticViewWarning.realisticViewVectorImage</a> object
will be provided with the junction view and the signpost representations. For <code>RealisticViewWarning.distanceType</code>
with value <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.passed</a>, the <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage">RealisticViewWarning.realisticViewVectorImage</a> object will be null.
Use <code>RealisticViewWarningListener</code> to get notifications about the realistic views of the upcoming junctions.</p>
<p>Realistic view notifications require an online connection in order to function properly, or that the
junction or signpost map layer data is cached, installed or preloaded as part of a <code>Region</code>.
This can be enabled via feature configurations.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewwarning">RealisticViewWarning</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">distanceToRealisticViewInMeters</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetype">distanceType</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-id">id</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewrasterimage">realisticViewRasterImage</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage">realisticViewVectorImage</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
