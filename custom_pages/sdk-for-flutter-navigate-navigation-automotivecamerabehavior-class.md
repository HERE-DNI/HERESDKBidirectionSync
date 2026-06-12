---
title: "AutomotiveCameraBehavior class abstract"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AutomotiveCameraBehavior-class.html -->


<div>
<h1>AutomotiveCameraBehavior class abstract</h1></div>

<p>Provides a high-level camera controller for automotive navigation that manages both tracking
and area camera behaviors.</p>
<p>This class acts as a facade, delegating camera operations to either
a <a href="/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class">TrackingCameraBehavior</a> for following the vehicle during navigation or an <a href="/sdk-for-flutter-navigate-navigation-areacamerabehavior-class">AreaCameraBehavior</a>
for showing overview areas such as points of interest or route previews.</p>
<p>The controller supports three states: tracking mode (following the vehicle), area mode (showing
geographic regions), or inactive (no automatic camera control). The inactive state allows
external control of the camera, such as when responding to user touch events or when UI logic
temporarily disables automatic camera behavior.</p>
<p>Camera configuration, including animation durations, zoom policies, and maneuver handling
settings, can be provided through a JSON configuration string or file. The configuration is
validated and parsed during construction.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-automotivecamerabehavior">AutomotiveCameraBehavior</a></li><li><a href="/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-automotivecamerabehavior-fromjson">AutomotiveCameraBehavior.fromJson</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">activeCameraType</a></li><li><a href="/sdk-for-flutter-navigate-navigation-camerabehavior-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-ismaneuverdetectionenabled">isManeuverDetectionEnabled</a></li><li><a href="/sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint">normalizedPrincipalPoint</a></li><li><a href="/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-orientationmode">orientationMode</a></li><li><a href="/sdk-for-flutter-navigate-navigation-camerabehavior-runtimetype">runtimeType</a></li><li><a href="/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-viewrectangle">viewRectangle</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-camerabehavior-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorgeobox">setAreaCameraBehaviorGeobox</a></li><li><a href="/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorvisiblepoints">setAreaCameraBehaviorVisiblePoints</a></li><li><a href="/sdk-for-flutter-navigate-navigation-camerabehavior-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-camerabehavior-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
