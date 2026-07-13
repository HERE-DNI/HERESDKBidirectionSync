---
title: "SpecialSpeedType enum - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-specialspeedtype"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SpecialSpeedType-enum-sidebar.html">

<div>

# <span class="kind-enum">SpecialSpeedType</span> enum

</div>

<div class="section desc markdown">

Represents the speed situation type.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Values

<span class="name">unknown</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
Unknown special speed type

<span class="name">advisorySpeed</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
These posted speeds are not the legal limit, but rather serve to warn a driver that road conditions indicate a lower speed is practical. Typically, the road condition is a curved road or a ramp but it may be due to a narrow road, narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a different road than the one for which it applies (this can happen with ramps). In this case, the advisory speed is indicated for the road for which it is intended, even if the sign is further than 50 meters from the particular road.

- Advisory speed signs due to construction are not included.
- A speed value is published for advisory signs.

<span class="name">speedBumpsPresent</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
This indicates that for a stretch of road, speed bumps are present or chicanes are present that effectively reduce the posted speed.

<span class="name">school</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
School zone signs are often placed to slow drivers before reaching an intersection where children are crossing.

<span class="name">timeDependent</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
A conditional speed limit as indicated on the local road signs. Speed limit that is in effect considering the current local time provided by the device's clock.

<span class="name">approximateSeasonalTime</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
Speed limit that is in effect considering the season

<span class="name">laneDependent</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
These are situations where a road has different speed limits per lane.

<span class="name">rain</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when it is raining or there is water on the road.

A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

<span class="name">snow</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when there is snow on the road.

A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

<span class="name">fog</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility decreases due to fog.

A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

