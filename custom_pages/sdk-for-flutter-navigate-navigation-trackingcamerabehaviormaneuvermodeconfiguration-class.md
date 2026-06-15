---
title: "TrackingCameraBehaviorManeuverModeConfiguration class"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrackingCameraBehaviorManeuverModeConfiguration-class.html -->


<div>
<h1>TrackingCameraBehaviorManeuverModeConfiguration class</h1></div>

<p>Configuration that defines how <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class">TrackingCameraBehavior</a> reacts to nearby maneuvers.</p>
<p>On each frame, and based on the current position, the availability of its functional road
class, and the availability of maneuver data for at least one adjacent maneuver, the camera
checks for a match against the <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-maneuverrules">TrackingCameraBehaviorManeuverModeConfiguration.maneuverRules</a> in the order they are listed. If a match is
found, subsequent rules are not checked. If no match is found, if inputs are unavailable,
or if the matched rule has <code>null</code> options, the camera does not react.</p>
<p>For correct default initialization, use <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultmaneuvermodeconfiguration">TrackingCameraBehavior.defaultManeuverModeConfiguration</a>.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-trackingcamerabehaviormaneuvermodeconfiguration">TrackingCameraBehaviorManeuverModeConfiguration</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-bearingthresholdindegrees">bearingThresholdInDegrees</a></li><li><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-maneuverrules">maneuverRules</a></li><li><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
