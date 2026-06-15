---
title: "RealisticViewWarningListener class abstract"
slug: "sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RealisticViewWarningListener-class.html -->


<div>
<h1>RealisticViewWarningListener class abstract</h1></div>

<p>This abstract class
should be implemented in order to receive realistic view warnings.</p>
<p>A <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> will not be given until the previous warning of that type has been passed.
For example, a route with <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> 120 meters and <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> 160 meters ahead,
the first <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">RealisticViewWarning.distanceToRealisticViewInMeters</a> is 120 meters
and the next <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">RealisticViewWarning.distanceToRealisticViewInMeters</a> is then 40 meters,
since that is the distance between the first and second warnings.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-realisticviewwarninglistener">RealisticViewWarningListener</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-onrealisticviewwarningupdated">onRealisticViewWarningUpdated</a></li><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
