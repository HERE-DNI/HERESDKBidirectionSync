---
title: "IndoorRouteStyle class - venue.routing library - Dart API"
slug: "sdk-for-flutter-navigate-venue.routing-indoorroutestyle-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="venue.routing/venue.routing-library-sidebar.html" data-below-sidebar="venue.routing/IndoorRouteStyle-class-sidebar.html">

<div>

# <span class="kind-class">IndoorRouteStyle</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Represents a style of the indoor route.

Contains information about route colors and widths. Optionally, this style allows to set <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> instances that can be used for specific route elements.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-indoorroutestyle">IndoorRouteStyle</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-destinationmarker">destinationMarker</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span>  
A <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> instance representing the destination of the route. By default, no map marker is provided The destination map marker of the resulting route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-drivemarker">driveMarker</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span>  
A <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> instance representing the drive point of the route. By default, no map marker is provided. The drive map marker of the resulting route. It signals that a user should take a transport vehicle.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-indoorpolylinecolor">indoorPolylineColor</a></span> <span class="signature">↔ Color</span>  
The color value. The default color is #48DAD0. The color of polylines for indoor route sections.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-indoorpolylinewidth">indoorPolylineWidth</a></span> <span class="signature">↔ double</span>  
The width in pixels. Default value is 15 pixels The width in pixels of polylines for indoor route sections.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-startmarker">startMarker</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span>  
A <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> instance representing the start of the route. By default, no map marker is provided. The start map marker of the resulting route.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-walkmarker">walkMarker</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span>  
A <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> instance representing the walk point of the route. By default, no map marker is provided. The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-getindoormarkerfor">getIndoorMarkerFor</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getIndoorMarkerFor-param-feature" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a></span> <span class="parameter-name">feature</span>, </span><span id="sdk-for-flutter-navigate-getIndoorMarkerFor-param-deltaZ" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">deltaZ</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span> </span>  
Returns a <a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> for a given indoor feature and the number of levels to change.

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-setindoormarkersfor">setIndoorMarkersFor</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setIndoorMarkersFor-param-feature" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-indoorlevelchangefeatures">IndoorLevelChangeFeatures</a></span> <span class="parameter-name">feature</span>, </span><span id="sdk-for-flutter-navigate-setIndoorMarkersFor-param-upMarker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span> <span class="parameter-name">upMarker</span>, </span><span id="sdk-for-flutter-navigate-setIndoorMarkersFor-param-downMarker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span> <span class="parameter-name">downMarker</span>, </span><span id="sdk-for-flutter-navigate-setIndoorMarkersFor-param-exitMarker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>?</span> <span class="parameter-name">exitMarker</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets map markers for the given indoor feature.

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-venue-routing-indoorroutestyle-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

