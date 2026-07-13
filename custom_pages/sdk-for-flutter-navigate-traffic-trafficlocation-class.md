---
title: "TrafficLocation class - traffic library - Dart API"
slug: "sdk-for-flutter-navigate-traffic-trafficlocation-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficLocation-class-sidebar.html">

<div>

# <span class="kind-class">TrafficLocation</span> class

</div>

<div class="section desc markdown">

The location reference to the traffic incident.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-trafficlocation">TrafficLocation</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-polyline" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span> <span class="parameter-name">polyline</span>, </span><span id="sdk-for-flutter-navigate-param-additionalPolylines" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span>\></span></span> <span class="parameter-name">additionalPolylines</span>, </span><span id="sdk-for-flutter-navigate-param-lengthInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">lengthInMeters</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-additionalpolylines">additionalPolylines</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span>\></span></span>  
List of polylines that were not included in continuous polyline. Use this to fill any gaps in the continuous polyline.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-description">description</a></span> <span class="signature">↔ String</span>  
The description of the location. In general, the language can't be bound to the description. Usually, the language is one of the local languages of the incident region. Note: A localizable description of the incident is part of <a href="sdk-for-flutter-navigate-traffic-trafficincidentbase-description">TrafficIncidentBase.description</a>. This description describes only the location where the incident occurred. Defaults to an empty string.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-lengthinmeters">lengthInMeters</a></span> <span class="signature">↔ int</span>  
The affected road length in meters. The length can be 0 only if the incident supplier has provided incomplete data.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-polyline">polyline</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geopolyline-class">GeoPolyline</a></span>  
The polyline representing the traffic entity shape. The current field contains a continuous polyline with no gaps between geo-coordinates. All others following the gap are present in the `additional_polylines` field.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-traffic-trafficlocation-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

