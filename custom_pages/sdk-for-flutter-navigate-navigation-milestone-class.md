---
title: "Milestone class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-milestone-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/Milestone-class-sidebar.html">

<div>

# <span class="kind-class">Milestone</span> class

</div>

<div class="section desc markdown">

Represents information about the waypoints along the route.

Note that this can include additional waypoints added during route calculation that may not have been part of the original user-defined waypoint list. For example, additional waypoints are added automatically between sections that require a different transport mode like when taking a ferry.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-milestone-withtype">Milestone.withType</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withType-param-sectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">sectionIndex</span>, </span><span id="sdk-for-flutter-navigate-withType-param-waypointIndex" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">waypointIndex</span>, </span><span id="sdk-for-flutter-navigate-withType-param-originalCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span> <span class="parameter-name">originalCoordinates</span>, </span><span id="sdk-for-flutter-navigate-withType-param-mapMatchedCoordinates" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">mapMatchedCoordinates</span>, </span><span id="sdk-for-flutter-navigate-withType-param-type" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType</a></span> <span class="parameter-name">type</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-mapmatchedcoordinates">mapMatchedCoordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>  
Map-matched geographic coordinates.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-originalcoordinates">originalCoordinates</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>?</span>  
User-defined geographic coordinates. If not available, this waypoint was added during route calculation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-sectionindex">sectionIndex</a></span> <span class="signature">↔ int</span>  
Index of the section on the route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-milestonetype">MilestoneType</a></span>  
Type of this Milestone

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-waypointindex">waypointIndex</a></span> <span class="signature">↔ int?</span>  
If present, this index corresponds to the waypoint in the original user-defined waypoint list. Otherwise this waypoint was added during route calculation by the system.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-milestone-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

