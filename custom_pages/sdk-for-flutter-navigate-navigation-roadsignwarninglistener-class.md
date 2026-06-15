---
title: "RoadSignWarningListener class abstract"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadSignWarningListener-class.html -->


<div>
<h1>RoadSignWarningListener class abstract</h1></div>

<p>This abstract class
should be implemented in order to receive road sign warnings.</p>
<p><strong>Note:</strong> The road sign warner is a point warner, which means that for a road sign there will <em>always</em> be
2 warnings emitted, with the <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetype">RoadSignWarning.distanceType</a> set to <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a> and <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.passed</a>
which is given when the location of the road sign is reached.
A <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> will not be given until the previous warning of that type has been passed.
For example, a route with <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> 120 meters and <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> 160 meters ahead,
the first <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters">RoadSignWarning.distanceToRoadSignInMeters</a> is 120 meters
and the next <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters">RoadSignWarning.distanceToRoadSignInMeters</a> is then 40 meters,
since that is the distance between the first and second warnings.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-roadsignwarninglistener">RoadSignWarningListener</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-onroadsignwarningupdated">onRoadSignWarningUpdated</a></li><li><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
