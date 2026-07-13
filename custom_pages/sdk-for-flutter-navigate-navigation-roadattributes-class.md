---
title: "RoadAttributes class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadattributes-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RoadAttributes-class-sidebar.html">

<div>

# <span class="kind-class">RoadAttributes</span> class

</div>

<div class="section desc markdown">

Road attributes, including usage and physical characteristics.

Note that a road can have more than one attribute at the same time.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-roadattributes">RoadAttributes</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-isbridge">isBridge</a></span> <span class="signature">↔ bool</span>  
Identifies a structure that allows a road, railway, or walkway to pass over another road, railway, waterway, or valley serving map display and route guidance functionalities. Bridge is published on segments that represent significant bridges and/or overpasses; elevated roads are not published as bridge.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-isbuiltuparea">isBuiltUpArea</a></span> <span class="signature">↔ bool</span>  
Indicates if the navigable segment is a built up area.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-iscontrolledaccess">isControlledAccess</a></span> <span class="signature">↔ bool</span>  
Controlled access roads are roads with limited entrances and exits that allow uninterrupted high-speed traffic flow. For example, the Interstate/Freeway network in the United States or the Motorway network in Europe. Controlled Access can be used for map display, avoidance of freeway/motorway, publishing speed limits, and route guidance timing.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-isdirtroad">isDirtRoad</a></span> <span class="signature">↔ bool</span>  
Indicates whether the navigable segment is paved. Paved is primarily used for map display and routing by assigning higher penalties to unpaved roads. Paved roads are made of concrete, asphalt, cobblestone or brick. Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-isdividedroad">isDividedRoad</a></span> <span class="signature">↔ bool</span>  
Indicates if there is a physical structure or painted road marking intended to legally prohibit left turns in right-side driving countries, right turns in left-side driving countries, and U-turns at divided intersections or in the middle of divided segments.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-isnothrough">isNoThrough</a></span> <span class="signature">↔ bool</span>  
Identifies a no through road. This can also be a part of the route you can only enter or leave if it’s a waypoint.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-isprivate">isPrivate</a></span> <span class="signature">↔ bool</span>  
Private identifies roads that are not maintained by an organization responsible for maintenance of public roads. Allows for unique cartographic representation of roads that restrict public use. May be used to avoid routing through a private road.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-isramp">isRamp</a></span> <span class="signature">↔ bool</span>  
Range is a ramp: connects roads that do not intersect at grade. Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”) and for route guidance when determining if sign text should be used.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside">isRightDrivingSide</a></span> <span class="signature">↔ bool</span>  
Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side. For example, in New York it is always `true` and in London always `false` as the United Kingdom is a left-hand driving country.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-isroundabout">isRoundabout</a></span> <span class="signature">↔ bool</span>  
Indicates the presence of a roundabout.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-istollway">isTollway</a></span> <span class="signature">↔ bool</span>  
Identifies a road for which a fee must be paid to use the road. Tollway may be used for map display (e.g., different rendering of toll roads) and routing. Tollway is flagged on roads that require a fee for traversal.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-istunnel">isTunnel</a></span> <span class="signature">↔ bool</span>  
Identifies an enclosed (on all sides) passageway through or under an obstruction. This attribute can be used for display or route guidance.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadattributes-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

