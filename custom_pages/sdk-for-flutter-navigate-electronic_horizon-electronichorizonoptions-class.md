---
title: "ElectronicHorizonOptions class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonOptions-class-sidebar.html">

<div>

# <span class="kind-class">ElectronicHorizonOptions</span> class

</div>

<div class="section desc markdown">

Provides options to configure <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonengine-class">ElectronicHorizonEngine</a>.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-electronichorizonoptions">ElectronicHorizonOptions</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-lookAheadDistancesInMeters" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>\></span></span> <span class="parameter-name">lookAheadDistancesInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-trailingDistanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">trailingDistanceInMeters</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-lookaheaddistancesinmeters">lookAheadDistancesInMeters</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>\></span></span>  
The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths. The first entry of the list is for the most preferred path, the second is for the side paths of the first level, the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided. The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list. If the list is empty, a single default distance value is used instead.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-trailingdistanceinmeters">trailingDistanceInMeters</a></span> <span class="signature">↔ double</span>  
The trailing distance of the electronic horizon path in meters. Segments are removed from the path once they are passed and the distance to them exceeds this value.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
