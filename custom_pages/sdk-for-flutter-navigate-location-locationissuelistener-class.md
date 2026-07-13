---
title: "LocationIssueListener class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationissuelistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/LocationIssueListener-class-sidebar.html">

<div>

# <span class="kind-class">LocationIssueListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

abstract class receiving notifications when the set of currently active location issues changes.

Location issues represent unexpected or degraded conditions affecting positioning quality, availability, or functionality. The LocationEngine monitors various positioning subsystems and aggregates detected issues into a unified snapshot delivered via this interface.

- Each callback delivers the complete current set of active issues.
- An empty list indicates all previously reported issues have cleared.
- Issues are transient by design and automatically removed once underlying conditions improve. No explicit clear/dismiss API is provided.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuelistener-locationissuelistener">LocationIssueListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onLocationIssueChangedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLocationIssueChangedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>\></span></span></span>)</span>)</span>  
abstract class receiving notifications when the set of currently active location issues changes.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuelistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuelistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuelistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuelistener-onlocationissuechanged">onLocationIssueChanged</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onLocationIssueChanged-param-issues" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a></span>\></span></span> <span class="parameter-name">issues</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called when the snapshot of currently active location issues changes.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuelistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-location-locationissuelistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

