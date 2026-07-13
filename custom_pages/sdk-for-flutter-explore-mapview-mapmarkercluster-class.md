---
title: "MapMarkerCluster class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mapmarkercluster-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerCluster-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMarkerCluster-class-sidebar.html">

<div>

# <span class="kind-class">MapMarkerCluster</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Groups map markers and enables their clustering to reduce visual clutter when there are many of them in a small area.

The markers that are close to each other are replaced by a single cluster marker. Cluster groups are generated based on geographical distance between objects, not based on screen space collision. Hence it is possible, that cluster markers can overlap.

The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the map, add it to the scene using <a href="sdk-for-flutter-explore-mapview-mapscene-addmapmarkercluster">MapScene.addMapMarkerCluster</a>. The display of a cluster is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects clusters which are visually large and cover a sizeable part of the viewport.

Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-mapmarkercluster">MapMarkerCluster</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-imageStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarkerclusterimagestyle-class">MapMarkerClusterImageStyle</a></span> <span class="parameter-name">imageStyle</span></span>)</span>  
Creates a new instance of a map marker cluster which is represented as an image.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-mapmarkercluster-withcounter">MapMarkerCluster.WithCounter</a></span><span class="signature">(<span id="sdk-for-flutter-explore-WithCounter-param-imageStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarkerclusterimagestyle-class">MapMarkerClusterImageStyle</a></span> <span class="parameter-name">imageStyle</span>, </span><span id="sdk-for-flutter-explore-WithCounter-param-counterStyle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarkerclustercounterstyle-class">MapMarkerClusterCounterStyle</a></span> <span class="parameter-name">counterStyle</span></span>)</span>  
Creates a new instance of a map marker cluster which is represented as an image along with a counter showing how many markers are actually grouped under particular cluster icon.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-markers">markers</a></span> <span class="signature">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a></span>\></span></span>  
The list of map markers which currently belong to this cluster. Modifying the list has no effect on the marker cluster. Returns the list of map markers which currently belong to this cluster.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-opacity">opacity</a></span> <span class="signature">↔ double</span>  
Opacity is the factor which is applied to the alpha channel of the image used for marker cluster. Gets the current opacity of the marker cluster image.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-addmapmarker">addMapMarker</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapMarker-param-marker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a></span> <span class="parameter-name">marker</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a map marker to this cluster.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-addmapmarkers">addMapMarkers</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-addMapMarkers-param-markers" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a></span>\></span></span> <span class="parameter-name">markers</span></span>) <span class="returntype parameter">→ void</span> </span>  
Adds a list of map markers to this cluster.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-removeallmapmarkers">removeAllMapMarkers</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes all map markers from this cluster.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-removemapmarker">removeMapMarker</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapMarker-param-marker" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a></span> <span class="parameter-name">marker</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a map marker from this cluster.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-removemapmarkers">removeMapMarkers</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-removeMapMarkers-param-markers" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-mapview-mapmarker-class">MapMarker</a></span>\></span></span> <span class="parameter-name">markers</span></span>) <span class="returntype parameter">→ void</span> </span>  
Removes a list of map markers from this cluster.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapmarkercluster-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
