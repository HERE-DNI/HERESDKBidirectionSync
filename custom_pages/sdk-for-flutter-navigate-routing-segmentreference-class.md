---
title: "SegmentReference class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-segmentreference-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/SegmentReference-class-sidebar.html">

<div>

# <span class="kind-class">SegmentReference</span> class

</div>

<div class="section desc markdown">

Reference to a segment id with a travel direction.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-segmentreference">SegmentReference</a></span><span class="signature">(\<a href="sdk-for-flutter-navigate-routing-traveldirection"><span id="sdk-for-flutter-navigate-param-segmentId" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">segmentId</span> = <span class="default-value">""</span>, </span><span id="sdk-for-flutter-navigate-param-travelDirection" class="parameter"><span class="type-annotation">[TravelDirection</a></span> <span class="parameter-name">travelDirection</span> = <span class="default-value">TravelDirection.bidirectional</span>, </span><span id="sdk-for-flutter-navigate-param-offsetStart" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">offsetStart</span> = <span class="default-value">0.0</span>, </span><span id="sdk-for-flutter-navigate-param-offsetEnd" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">offsetEnd</span> = <span class="default-value">1.0</span>, </span><span id="sdk-for-flutter-navigate-param-tilePartitionId" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">tilePartitionId</span> = <span class="default-value">0</span>, </span><span id="sdk-for-flutter-navigate-param-localId" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">localId</span> = <span class="default-value">0</span></span>\])</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-segmentreference-withdefaults">SegmentReference.withDefaults</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-localid">localId</a></span> <span class="signature">↔ int?</span>  
Local ID of the segment inside the OCM tile.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-offsetend">offsetEnd</a></span> <span class="signature">↔ double</span>  
The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-offsetstart">offsetStart</a></span> <span class="signature">↔ double</span>  
The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-segmentid">segmentId</a></span> <span class="signature">↔ String</span>  
Topology segment id representing a unique identifier within the HERE platform catalogs.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-tilepartitionid">tilePartitionId</a></span> <span class="signature">↔ int</span>  
HERE tile partition id (Morton-encoding + level indicator) of the segment. As in HERE Map Content.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-traveldirection">travelDirection</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-traveldirection">TravelDirection</a></span>  
Travel direction of the segment.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-segmentreference-fromstring">fromString</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-fromString-param-segmentRef" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">segmentRef</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a>?</span> </span>  
Returns an instance of this struct from a string if it's well-formatted, `null` otherwise.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

