---
title: "JunctionViewLaneAssistance class"
slug: "sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- JunctionViewLaneAssistance-class.html -->


<div>
<h1>JunctionViewLaneAssistance class</h1></div>

<p>A class that provides lane assistance information for the next complex junction
in order to keep following the route.</p>
<p>It is recommended to indicate <a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a>
and <a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> separately or to indicate only <a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> information -
<a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a> will recommend all lanes that allow to pass the upcoming complex junction, regardless
if they will lead to the next maneuver or not.
If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be
the same as the ones from <a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a>.</p>
<p>A junction is recognized as complex only if:</p>
<ul>
<li>it is at least a bifurcation;</li>
<li>it has at least two lanes whose directions do not follow the current route.
In opposition to <a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a>, notifications are also forwarded when there is
no maneuver action occurring at the next complex junction.
Therefore, <a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a> can be disjointed from maneuvers. If lane assistance should be used to
associate it with upcoming maneuvers, consider to use <a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> instead.
Note that <a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> notifications are synchronized with maneuver events,
whereas <a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a> events are not strictly synchronized with maneuver events.</li>
</ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-junctionviewlaneassistance">JunctionViewLaneAssistance</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-distancetojunctioninmeters">distanceToJunctionInMeters</a></li><li><a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-lanesfornextjunction">lanesForNextJunction</a></li><li><a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
