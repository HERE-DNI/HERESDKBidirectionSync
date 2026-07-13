---
title: "MapCameraFarPlaneConfiguration class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraFarPlaneConfiguration-class-sidebar.html">

<div>

# <span class="kind-class">MapCameraFarPlaneConfiguration</span> class

</div>

<div class="section desc markdown">

Far plane distance configuration for a zoom level.

Effective far plane is computed from both parameters as: farPlaneInMeters = max( minDistanceInMeters, distanceToTargetInMeters \* distanceFactor )

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-mapcamerafarplaneconfiguration">MapCameraFarPlaneConfiguration</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-distanceFactor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceFactor</span>, </span><span id="sdk-for-flutter-explore-param-minDistanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">minDistanceInMeters</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-distancefactor">distanceFactor</a></span> <span class="signature">↔ double</span>  
Multiplier applied to the camera distance to target when calculating the far plane.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-mindistanceinmeters">minDistanceInMeters</a></span> <span class="signature">↔ double</span>  
Minimum far plane clamp in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapcamerafarplaneconfiguration-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

