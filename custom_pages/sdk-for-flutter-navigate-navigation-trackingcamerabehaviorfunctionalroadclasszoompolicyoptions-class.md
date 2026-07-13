---
title: "TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions-class-sidebar.html">

<div>

# <span class="kind-class">TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions</span> class

</div>

<div class="section desc markdown">

Configuration for mapping functional road classes to zoom levels.

For correct default initialization, use <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultfunctionalroadclasszoompolicyoptions">TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions">TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-defaultzoom">defaultZoom</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>  
Default zoom returned when the functional road class is missing or unmapped. Defaults to a <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> with kind <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> and value 16.5.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-functionalroadclasstozoom">functionalRoadClassToZoom</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-functionalroadclass">FunctionalRoadClass</a></span>, <span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>\></span></span>  
Maps each functional road class to the zoom that should be used for it. If <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultfunctionalroadclasszoompolicyoptions">TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions</a> is not used for <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class">TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions</a>, it will be an empty map.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

