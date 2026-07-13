---
title: "MaxSpeedOnSegment class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-maxspeedonsegment-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MaxSpeedOnSegment-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/MaxSpeedOnSegment-class-sidebar.html">

<div>

# <span class="kind-class">MaxSpeedOnSegment</span> class

</div>

<div class="section desc markdown">

New base speed for a segment.

Affects route calculation and the ETA. Cannot increase base speed on segment.

**Note:** This option can only be used with the `RoutingEngine`. The `OfflineRoutingEngine` is not supported and the option will be ignored. Note that the `OfflineRoutingEngine` is only available for the Navigate license.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-maxspeedonsegment">MaxSpeedOnSegment</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-segment" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-segmentreference-class">SegmentReference</a></span> <span class="parameter-name">segment</span>, </span><span id="sdk-for-flutter-explore-param-baseSpeedInMetersPerSecond" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">baseSpeedInMetersPerSecond</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-basespeedinmeterspersecond">baseSpeedInMetersPerSecond</a></span> <span class="signature">↔ double</span>  
New maximum value in m/s of baseSpeed on segment. The provided value must be in the range \[1.0, 70.0\]. Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-segment">segment</a></span> <span class="signature">↔ <a href="sdk-for-flutter-explore-routing-segmentreference-class">SegmentReference</a></span>  
A segment for which the new base speed is specified. Only the `segmendId` and `travelDirection` parameters are used, other parameters are ignored. Setting a `segmendId` is mandatory.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-routing-maxspeedonsegment-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
