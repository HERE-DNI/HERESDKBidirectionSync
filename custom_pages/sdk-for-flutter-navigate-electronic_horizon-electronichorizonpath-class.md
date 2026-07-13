---
title: "ElectronicHorizonPath class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonPath-class-sidebar.html">

<div>

# <span class="kind-class">ElectronicHorizonPath</span> class

</div>

<div class="section desc markdown">

Represents a single electronic horizon path.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-electronichorizonpath">ElectronicHorizonPath</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-segments" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonsegment-class">ElectronicHorizonSegment</a></span>\></span></span> <span class="parameter-name">segments</span>, </span><span id="sdk-for-flutter-navigate-param-probability" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">probability</span>, </span><span id="sdk-for-flutter-navigate-param-level" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">level</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-level">level</a></span> <span class="signature">↔ int</span>  
The level of this path. A value of 0 represents the most-preferred path.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-parentpathindex">parentPathIndex</a></span> <span class="signature">↔ int?</span>  
The index of the parent path. Index 0 marks the most-preferred path.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-parentsegmentindex">parentSegmentIndex</a></span> <span class="signature">↔ int?</span>  
The index of the parent segment in the parent path. This value is `null` if the path is the most-preferred path.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-probability">probability</a></span> <span class="signature">↔ double</span>  
The probability of this electronic horizon path, where a value of 1 represents the most-preferred path and a value of 0 represents an unlikely path.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-segments">segments</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonsegment-class">ElectronicHorizonSegment</a></span>\></span></span>  
The ordered list of segments in this path. The list can be empty when no segments are available for the current path.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonpath-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

