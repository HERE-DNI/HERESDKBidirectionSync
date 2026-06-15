---
title: "MapMarker class abstract"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarker-class.html -->


<div>
<h1>MapMarker class abstract</h1></div>

<p><code>MapMarker</code> is used to draw images on the map, for example to mark a specific location.</p>
<p>By default, the marker is centered on the given geographic coordinates.
Markers keep their size regardless of the current zoom level of the map view.</p>
<p>The image to be displayed is represented by <a href="sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a> object. For performance reasons,
it is highly recommended to reuse a single instance of the image when creating multiple
identical markers.</p>
<p>To display the map marker, it needs to be added to the scene using <a href="sdk-for-flutter-navigate-mapview-mapscene-addmapmarker">MapScene.addMapMarker</a>.
To stop displaying it, remove it from the scene using <a href="sdk-for-flutter-navigate-mapview-mapscene-removemapmarker">MapScene.removeMapMarker</a>.</p>
<p>The display of a map marker is only guaranteed in case its origin is within the viewport.
At the moment, this is a known limitation that mostly affects map markers which are visually
large and cover a sizeable part of the viewport.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapMarkers API to add a very large number of markers
(several thousands, especially 10000+) is not recommended. Adding this many markers will have a
negative impact on the performance leading to stuttering of the app and lower frame rates.
To work around this limitation the following approach can be used:
Register to map camera updates using <a href="sdk-for-flutter-navigate-mapview-mapcamera-addlistener">MapCamera.addListener</a>. Query the bounding box of the
camera viewport using <a href="sdk-for-flutter-navigate-mapview-mapcamera-boundingbox">MapCamera.boundingBox</a> (it may be extended)
and then use the method <a href="sdk-for-flutter-navigate-core-geobox-containsgeocoordinates">GeoBox.containsGeoCoordinates</a> in combination with
<a href="sdk-for-flutter-navigate-mapview-mapcamerastate-distancetotargetinmeters">MapCameraState.distanceToTargetInMeters</a> to determine which MapMarkers are actually visible
to the user in the current camera viewport and thus need to be added to the map.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-mapmarker">MapMarker</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-mapmarker-withanchor">MapMarker.withAnchor</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-mapmarker-withimageandtext">MapMarker.withImageAndText</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-anchor">anchor</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-coordinates">coordinates</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-draworder">drawOrder</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-fadeduration">fadeDuration</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-image">image</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-isoverlapallowed">isOverlapAllowed</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-istextoptional">isTextOptional</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-metadata">metadata</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-opacity">opacity</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-text">text</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-textstyle">textStyle</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-visibilityranges">visibilityRanges</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-cancelanimation">cancelAnimation</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-startanimation">startAnimation</a></li><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-mapmarker-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
