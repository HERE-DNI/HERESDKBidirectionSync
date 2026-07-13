---
title: "TrackingCameraBehaviorSpeedBasedZoomPolicyOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrackingCameraBehaviorSpeedBasedZoomPolicyOptions-class-sidebar.html">

<div>

# <span class="kind-class">TrackingCameraBehaviorSpeedBasedZoomPolicyOptions</span> class

</div>

<div class="section desc markdown">

Configuration for computing zoom levels from speed thresholds defined per road classification.

For correct default initialization, use <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultspeedbasedzoompolicyoptions">TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-trackingcamerabehaviorspeedbasedzoompolicyoptions">TrackingCameraBehaviorSpeedBasedZoomPolicyOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-delaybetweenthresholdchanges">delayBetweenThresholdChanges</a></span> <span class="signature">↔ Duration?</span>  
Minimum time interval that must pass before the zoom level is allowed to switch to a new speed threshold. If <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultspeedbasedzoompolicyoptions">TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions</a> is not used for <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class">TrackingCameraBehaviorSpeedBasedZoomPolicyOptions</a>, it will be `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-roadclassificationtospeedthreshold">roadClassificationToSpeedThreshold</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-roadclassification">RoadClassification</a></span>, <span class="type-parameter">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedthreshold-class">TrackingCameraBehaviorSpeedThreshold</a></span>\></span></span>\></span></span>  
Defines, per road classification, how the zoom level should change in response to different vehicle speeds. If <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultspeedbasedzoompolicyoptions">TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions</a> is not used for <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class">TrackingCameraBehaviorSpeedBasedZoomPolicyOptions</a>, it will be an empty map.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

