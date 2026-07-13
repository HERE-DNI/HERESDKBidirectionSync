---
title: "LocationTime class - core library - Dart API"
slug: "sdk-for-flutter-explore-core-locationtime-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationTime-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/LocationTime-class-sidebar.html">

<div>

# <span class="kind-class">LocationTime</span> class

</div>

<div class="section desc markdown">

This struct presents all the time data tied to a location, like an arrival or departure time.

The time data is originally specified in RFC 3339, section 5.6 format. For example, "2022-03-23T16:07:31+01:00" in Cracow, Poland, i.e. a Central European Time (CET) location. Note that this struct doesn't give any data on the tied location. The location should be derived from the context.

</div>

<div class="section">

Annotations  
- @<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-locationtime-locationtime">LocationTime</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-localTime" class="parameter"><span class="type-annotation">DateTime</span> <span class="parameter-name">localTime</span>, </span><span id="sdk-for-flutter-explore-param-utcTime" class="parameter"><span class="type-annotation">DateTime</span> <span class="parameter-name">utcTime</span>, </span><span id="sdk-for-flutter-explore-param-utcOffset" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">utcOffset</span></span>)</span>  
Creates a new instance.

<div class="constructor-modifier features">

const

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-locationtime-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-locationtime-localtime">localTime</a></span> <span class="signature">→ DateTime</span>  
The time as observed in the tied location. For example, if a route is requested in Cracow, Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-locationtime-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-locationtime-utcoffset">utcOffset</a></span> <span class="signature">→ Duration</span>  
The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC) in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is UTC-05:00, it is -18000.

<div class="features">

<span class="feature">final</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-locationtime-utctime">utcTime</a></span> <span class="signature">→ DateTime</span>  
The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland, the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.

<div class="features">

<span class="feature">final</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-locationtime-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-locationtime-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-locationtime-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
