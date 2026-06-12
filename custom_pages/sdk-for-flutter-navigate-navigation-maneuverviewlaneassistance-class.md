---
title: "ManeuverViewLaneAssistance class"
slug: "sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverViewLaneAssistance-class.html -->


<div>
<h1>ManeuverViewLaneAssistance class</h1></div>

<p>A class that provides lane assistance information for the next maneuver(s).</p>
<p>During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes
in order to complete the upcoming maneuvers.
The notifications are synchronized with the <a href="/sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a>.
<a href="/sdk-for-flutter-navigate-navigation-eventtextlistener-class">EventTextListener</a> has 4 notification types for each maneuver:
Range, Reminder, Distance and Action.
Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object
(e.g. "After 400 meters, turn right onto Invalidenstraße").
The notification will not be sent when other types of maneuver notification are given.
The notification will not be sent when no lane data is available.
During tracking mode, no notifications are delivered.
This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextmaneuver">lanesForNextManeuver</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-lanesfornextnextmaneuver">lanesForNextNextManeuver</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
