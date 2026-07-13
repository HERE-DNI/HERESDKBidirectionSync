---
title: "TransportMode enum - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-transportmode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TransportMode.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/transport-library-sidebar.html" data-below-sidebar="transport/TransportMode-enum-sidebar.html">

<div>

# <span class="kind-enum">TransportMode</span> enum

</div>

<div class="section desc markdown">

Specifies the mode of transport used for route calculalation.

</div>

## Values

<span class="name">car</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
The calculated route is optimized for cars.

<span class="name">truck</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
The calculated route is optimized for trucks. This mode considers truck restrictions and uses truck specific speed assumptions when calculating the route.

<span class="name">pedestrian</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
The calculated route is optimized for pedestrians. As one effect, maneuvers will be optimized for walking, i.e. segments will consider actions relevant for pedestrians and maneuver instructions will contain texts suitable for a walking person. This mode disregards any traffic information.

<span class="name">scooter</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
The calculated route is optimized for scooters.

<span class="name">bicycle</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
Route calculation for bicycles.

<span class="name">publicTransit</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
The calculated route is optimized for public transit. Note that this transport mode is available only for some versions of the HERE SDK. Check `SDKBuildInformation` and consult your HERE representative if necessary.

<span class="name">taxi</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
The taxi transport mode takes into account tax restricted streets as well as streets reserved for exclusive taxi access. Note that roads that are restricted or reserved for taxis are avoided, unless a waypoint is set on such a road - as this may indicate to pick-up or to drop-off a passenger.

**Note:** This is a beta release of this transport mode, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases or even become unsupported, without a deprecation process.

<span class="name">bus</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
Route calculation for buses. Denotes those vehicles operated by public transport provider. This transport mode has the access to the bus-only lane/road.

<span class="name">privateBus</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>  
Route calculation for private buses. Denotes those vehicles operated by private transport company. This transport mode does not have the access to the bus-only lane/road.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-transport-transportmode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-transportmode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-transportmode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-transport-transportmode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-transport-transportmode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-transport-transportmode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-transport-transportmode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
