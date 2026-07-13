---
title: "LaneAttribute class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-laneattribute-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneAttribute-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/LaneAttribute-class-sidebar.html">

<div>

# <span class="kind-class">LaneAttribute</span> class

</div>

<div class="section desc markdown">

A class that describes attributes assigned to a specific section of a lane.

It includes lane markings, allowed travel directions, tolling info, access restrictions, and optional lane type.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-laneattribute">LaneAttribute</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-startOffsetInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">startOffsetInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-markings" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lanemarkings-class">LaneMarkings</a></span> <span class="parameter-name">markings</span>, </span><span id="sdk-for-flutter-navigate-param-access" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-laneaccess-class">LaneAccess</a></span> <span class="parameter-name">access</span>, </span><span id="sdk-for-flutter-navigate-param-tollStructures" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-tollstructure-class">TollStructure</a></span>\></span></span> <span class="parameter-name">tollStructures</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-access">access</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-laneaccess-class">LaneAccess</a></span>  
Access characteristics of the lane that identifies the vehicle type(s) allowed to access a lane.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-markings">markings</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-lanemarkings-class">LaneMarkings</a></span>  
Indicate the markings on the road

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-startoffsetinmeters">startOffsetInMeters</a></span> <span class="signature">↔ int</span>  
The start offset of the lane in meters from the beginning of the segment

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-tollstructures">tollStructures</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-tollstructure-class">TollStructure</a></span>\></span></span>  
List of Toll Structure that identifies the presence of physical toll structures or automatic controls on the lane at entry and exit points along a toll road which requires payment (cash, electronic, etc.) or ticket

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-type">type</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-lanetype-class">LaneType</a>?</span>  
Specifies the functional and regulatory roles a lane may serve, such as turn, express, HOV, or bike use

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-laneattribute-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
