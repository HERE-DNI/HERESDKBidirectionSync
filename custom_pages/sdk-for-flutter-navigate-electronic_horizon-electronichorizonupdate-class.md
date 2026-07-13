---
title: "ElectronicHorizonUpdate class - electronic_horizon library - Dart API"
slug: "sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonUpdate-class-sidebar.html">

<div>

# <span class="kind-class">ElectronicHorizonUpdate</span> class

</div>

<div class="section desc markdown">

A class representing a full update delivered via <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonlistener-class">ElectronicHorizonListener</a> notifications.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-electronichorizonupdate">ElectronicHorizonUpdate</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-position" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonposition-class">ElectronicHorizonPosition</a></span> <span class="parameter-name">position</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-electronichorizon">electronicHorizon</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizon-class">ElectronicHorizon</a>?</span>  
The full electronic horizon recomputed for the current vehicle state. May be `null` if there is no update.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-position">position</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonposition-class">ElectronicHorizonPosition</a></span>  
The vehicle’s updated position relative to the electronic horizon. Always present. If no `electronic_horizon` is available, the position refers to the most recently known horizon.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-segmentchanges">segmentChanges</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonsegmentchanges-class">ElectronicHorizonSegmentChanges</a>?</span>  
The difference between the previously emitted horizon and the newly computed one. Contains added and removed segments. May be `null` if there is no update.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-electronic_horizon-electronichorizonupdate-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

