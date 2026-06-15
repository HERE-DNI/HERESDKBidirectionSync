---
title: "LocationIndicator class abstract"
slug: "sdk-for-flutter-explore-mapview-locationindicator-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationIndicator-class.html -->


<div>
<h1>LocationIndicator class abstract</h1></div>

<p>Graphical object to represent the location of the user on the map.</p>
<p>It is either a green dot for pedestrian style or a triangular arrow for vehicle navigation style.
This style can be changed by <a href="sdk-for-flutter-explore-mapview-locationindicator-locationindicatorstyle">LocationIndicator.locationIndicatorStyle</a></p>
<p>The location is made available to an instance of this class by calling <a href="sdk-for-flutter-explore-mapview-locationindicator-updatelocation">LocationIndicator.updateLocation</a> or
<a href="sdk-for-flutter-explore-mapview-locationindicator-updatelocationandcamera">LocationIndicator.updateLocationAndCamera</a>.</p>
<p>Use <a href="sdk-for-flutter-explore-mapview-locationindicator-enable">LocationIndicator.enable</a> to add this object to the map and <a href="sdk-for-flutter-explore-mapview-locationindicator-disable">LocationIndicator.disable</a> to remove it.</p>
<p>Note: The LocationIndicator is always rendered at a fixed altitude near 0. Changing the MapCamera
to look at geographic coordinates with an altitude that is higher can cause the following behavior: If the
MapCamera angle is tilted and altitude is too high, the LocationIndicator can unexpectedly
disappear from the viewport due to the new perspective.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-locationindicator-locationindicator">LocationIndicator</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-locationindicator-withmapview">LocationIndicator.withMapView</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-locationindicator-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-isaccuracyvisualized">isAccuracyVisualized</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-isactive">isActive</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-locationindicatorstyle">locationIndicatorStyle</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-materialreflectivity">materialReflectivity</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-opacity">opacity</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-locationindicator-disable">disable</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-enable">enable</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-gethalocolor">getHaloColor</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-sethalocolor">setHaloColor</a></li><li><a class="deprecated" href="sdk-for-flutter-explore-mapview-locationindicator-setmarker3dmodel">setMarker3dModel</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-setmarker3dmodelwithrendersizeunit">setMarker3dModelWithRenderSizeUnit</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-tostring">toString</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-updatelocation">updateLocation</a></li><li><a href="sdk-for-flutter-explore-mapview-locationindicator-updatelocationandcamera">updateLocationAndCamera</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-locationindicator-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
