---
title: "EventText class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-eventtext-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/EventText-class-sidebar.html">

<div>

# <span class="kind-class">EventText</span> class

</div>

<div class="section desc markdown">

Contains all the information regarding the next text announcement.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-eventtext">EventText</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-textnotificationtype">TextNotificationType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-navigate-param-distanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-text" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">text</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-distanceinmeters">distanceInMeters</a></span> <span class="signature">↔ double</span>  
Distance in meters to the location of the event for which the text notification is given.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-maneuvernotificationdetails">maneuverNotificationDetails</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationdetails-class">ManeuverNotificationDetails</a>?</span>  
Information about the next maneuver. Is non-`null` only for <a href="sdk-for-flutter-navigate-navigation-eventtext-type">EventText.type</a> equals to <a href="sdk-for-flutter-navigate-navigation-textnotificationtype">TextNotificationType.maneuver</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-spatialnotificationdetails">spatialNotificationDetails</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-spatialnotificationdetails-class">SpatialNotificationDetails</a>?</span>  
Information for a spatial text notifications. When <a href="sdk-for-flutter-navigate-navigation-eventtextoptions-enablespatialaudio">EventTextOptions.enableSpatialAudio</a> is false, then this attribute will be `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-text">text</a></span> <span class="signature">↔ String</span>  
The text notification instruction. The text is formatted and localized as specified via <a href="sdk-for-flutter-navigate-routing-routetextoptions-class">RouteTextOptions</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-textnotificationtype">TextNotificationType</a></span>  
Indicates the type of text announcement

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtext-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

