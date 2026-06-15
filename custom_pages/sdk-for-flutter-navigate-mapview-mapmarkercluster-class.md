---
title: "MapMarkerCluster class abstract"
slug: "sdk-for-flutter-navigate-mapview-mapmarkercluster-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerCluster-class.html -->


<div>
<h1>MapMarkerCluster class abstract</h1></div>

<p>Groups map markers and enables their clustering to reduce visual clutter when there are many of
them in a small area.</p>
<p>The markers that are close to each other are replaced by a single cluster marker. Cluster groups
are generated based on geographical distance between objects, not based on screen space collision.
Hence it is possible, that cluster markers can overlap.</p>
<p>The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the
map, add it to the scene using <a href="sdk-for-flutter-navigate-mapview-mapscene-addmapmarkercluster">MapScene.addMapMarkerCluster</a>. The display of a cluster is only
guaranteed in case its origin is within the viewport. At the moment, this is a known limitation
that mostly affects clusters which are visually large and cover a sizeable part of the viewport.</p>
<p>Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-mapmarkercluster">MapMarkerCluster</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-mapmarkercluster-withcounter">MapMarkerCluster.WithCounter</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-markers">markers</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-opacity">opacity</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-addmapmarker">addMapMarker</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-addmapmarkers">addMapMarkers</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-removeallmapmarkers">removeAllMapMarkers</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-removemapmarker">removeMapMarker</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-removemapmarkers">removeMapMarkers</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapmarkercluster-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
