---
title: "RailwayCrossingWarningListener class abstract"
slug: "sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RailwayCrossingWarningListener-class.html -->


<div>
<h1>RailwayCrossingWarningListener class abstract</h1></div>

<p>This abstract class
should be implemented in order to receive railway crossing warnings.</p>
<p><strong>Note:</strong> The railway crossing warner can be either a zone warner or a point warner, depending
on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This
means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad
crossing is a zone warner then 3 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>,
<code>DistanceType.REACHED</code> and lastly <code>DistanceType.PASSED</code> when the end of the railway crossing is passed. In
case the railroad crossing is a point warner then 2 warnings will be emitted with the <code>RailwayCrossingWarning.distance_type</code>
set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code> when the end of the railway crossing is passed.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-railwaycrossingwarninglistener">RailwayCrossingWarningListener</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-onrailwaycrossingwarningupdated">onRailwayCrossingWarningUpdated</a></li><li><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
