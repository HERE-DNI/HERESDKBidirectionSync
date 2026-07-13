---
title: "Lane class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-lane-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/Lane-class-sidebar.html">

<div>

# <span class="kind-class">Lane</span> class

</div>

<div class="section desc markdown">

A class that provides information for a lane.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-lane-withall">Lane.withAll</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withAll-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lanetype-class">LaneType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-navigate-withAll-param-recommendationState" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate">LaneRecommendationState</a></span> <span class="parameter-name">recommendationState</span>, </span><span id="sdk-for-flutter-navigate-withAll-param-access" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-laneaccess-class">LaneAccess</a></span> <span class="parameter-name">access</span>, </span><span id="sdk-for-flutter-navigate-withAll-param-laneMarkings" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lanemarkings-class">LaneMarkings</a></span> <span class="parameter-name">laneMarkings</span>, </span><span id="sdk-for-flutter-navigate-withAll-param-directions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a></span>\></span></span> <span class="parameter-name">directions</span>, </span><span id="sdk-for-flutter-navigate-withAll-param-directionsOnRoute" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a></span>\></span></span> <span class="parameter-name">directionsOnRoute</span></span>)</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-lane-withdirections">Lane.withDirections</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withDirections-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lanetype-class">LaneType</a></span> <span class="parameter-name">type</span>, </span><span id="sdk-for-flutter-navigate-withDirections-param-access" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-laneaccess-class">LaneAccess</a></span> <span class="parameter-name">access</span>, </span><span id="sdk-for-flutter-navigate-withDirections-param-laneMarkings" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lanemarkings-class">LaneMarkings</a></span> <span class="parameter-name">laneMarkings</span>, </span><span id="sdk-for-flutter-navigate-withDirections-param-directions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a></span>\></span></span> <span class="parameter-name">directions</span>, </span><span id="sdk-for-flutter-navigate-withDirections-param-directionsOnRoute" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a></span>\></span></span> <span class="parameter-name">directionsOnRoute</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-access">access</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-laneaccess-class">LaneAccess</a></span>  
Indicates which vehicle types can access this lane.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-directions">directions</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a></span>\></span></span>  
Indicates all the lane directions that are available for this lane.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-directionsonroute">directionsOnRoute</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-lanedirection">LaneDirection</a></span>\></span></span>  
Indicates the lane directions that are on the route. Following these directions keeps the driver on the route. This is a subset of <a href="sdk-for-flutter-navigate-navigation-lane-directions">Lane.directions</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-lanemarkings">laneMarkings</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-lanemarkings-class">LaneMarkings</a></span>  
Indicates the lane markings between the lanes.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-recommendationstate">recommendationState</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-lanerecommendationstate">LaneRecommendationState</a></span>  
Indicates if this lane leads to the upcoming maneuvers.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-lanetype-class">LaneType</a></span>  
Indicates the properties of this lane. For example, it indicates whether parking is allowed, if it is an acceleration lane, an express lane, or other attributes.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lane-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

