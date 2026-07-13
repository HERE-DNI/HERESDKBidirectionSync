---
title: "MapSceneMapPickFilterContentType enum - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapSceneMapPickFilterContentType-enum-sidebar.html">

<div>

# <span class="kind-enum">MapSceneMapPickFilterContentType</span> enum

</div>

<div class="section desc markdown">

Type of the map content to be picked.

</div>

## Values

<span class="name">mapItems</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype">MapSceneMapPickFilterContentType</a></span>  
Map items added through a <a href="sdk-for-flutter-explore-mapview-mapscene-class">MapScene</a> like <a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a>, <a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a>, <a href="sdk-for-flutter-explore-mapview-mappolygon-class">MapPolygon</a>.

<span class="name">mapContent</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype">MapSceneMapPickFilterContentType</a></span>  
Pickable map content currently consists of:

- Embedded carto POI markers that by default are available on the map.
- Traffic incidents that are visible when they are enabled using <a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> with <a href="sdk-for-flutter-explore-mapview-mapfeatures-trafficincidents">MapFeatures.trafficIncidents</a>.
- Vehicle restrictions are only available for the Navigate license. Vehicle restrictions are enabled using <a href="sdk-for-flutter-explore-mapview-mapscene-enablefeatures">MapScene.enableFeatures</a> with `MapFeatures.VEHICLE_RESTRICTIONS`. Please note that the vehicle restriction line marking the affected street is pickable and not the restriction icon itself. Only visible POIs, traffic incidents and vehicle restrictions lines can be picked, i.e. only those categories that are not hidden and those that are not covered by any custom marker.

<span class="name">customLayerData</span> <span class="signature">→ const <a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype">MapSceneMapPickFilterContentType</a></span>  
Custom user map content added using custom datasources e.g. <a href="sdk-for-flutter-explore-mapview-datasource-linedatasource-class">LineDataSource</a>, <a href="sdk-for-flutter-explore-mapview-datasource-polygondatasource-class">PolygonDataSource</a> and layers.

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapscenemappickfiltercontenttype">MapSceneMapPickFilterContentType</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

