---
title: "SegmentSpecialSpeedSituation class - mapdata library - Dart API"
slug: "sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/SegmentSpecialSpeedSituation-class-sidebar.html">

<div>

# <span class="kind-class">SegmentSpecialSpeedSituation</span> class

</div>

<div class="section desc markdown">

A special speed situation indicates a speed that exists under special circumstances.

It can be used to further refine the estimation of traversal times, route calculation and calculation of route guidance timing.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-segmentspecialspeedsituation">SegmentSpecialSpeedSituation</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-specialSpeedType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span> <span class="parameter-name">specialSpeedType</span>, </span><span id="sdk-for-flutter-navigate-param-speedLimitInMetersPerSecond" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">speedLimitInMetersPerSecond</span>, </span><span id="sdk-for-flutter-navigate-param-appliesDuring" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-timerule-class">TimeRule</a></span>\></span></span> <span class="parameter-name">appliesDuring</span></span>)</span>  
Creates a new instance with default values.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-appliesduring">appliesDuring</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-timerule-class">TimeRule</a></span>\></span></span>  
The times during which the condition applies. May be empty for all special_speed_type values except `TIME_DEPENDENT` and `APPROXIMATE_SEASONAL_TIME`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-specialspeedtype">specialSpeedType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a></span>  
Represents the speed situation type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-speedlimitinmeterspersecond">speedLimitInMetersPerSecond</a></span> <span class="signature">↔ double</span>  
Overrides normal speed limit for this situation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

