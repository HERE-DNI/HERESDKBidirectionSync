---
title: "MapCameraUpdateFactory class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraUpdateFactory-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html">

<div>

# <span class="kind-class">MapCameraUpdateFactory</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Factory for creating MapCameraUpdate to change map's camera.

For some factory methods you can apply an additional padding in pixels by setting a `viewRectangle` parameter based on the current size of the map view:

``` dart
var leftPaddingInPixels = 5;
var rightPaddingInPixels = 5;
var topPaddingInPixels = 5;
var bottomPaddingInPixels = 5;
var horizontalPaddingInPixels = leftPaddingInPixels + rightPaddingInPixels;
var verticalPaddingInPixels = topPaddingInPixels + bottomPaddingInPixels;

var origin = Point2D(leftPaddingInPixels, topPaddingInPixels);
var sizeInPixels = Size2D(_hereMapController.viewportSize.width - horizontalPaddingInPixels, _hereMapController.viewportSize.height - verticalPaddingInPixels);
var paddedViewRectangle = Rectangle2D(origin, sizeInPixels);
```

</pre>

The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates also the top-left corner of the map's viewport.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-mapcameraupdatefactory">MapCameraUpdateFactory</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-compositeupdate">compositeUpdate</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-compositeUpdate-param-mapCameraUpdates" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span>\></span></span> <span class="parameter-name">mapCameraUpdates</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates a composite camera update from a list of camera updates.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatarea">lookAtArea</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookAtArea-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to look at the given geo-box, preserving current orientation and zooming at the center of viewport.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatareawithgeoorientationandviewrectangle">lookAtAreaWithGeoOrientationAndViewRectangle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookAtAreaWithGeoOrientationAndViewRectangle-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-navigate-lookAtAreaWithGeoOrientationAndViewRectangle-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span><span id="sdk-for-flutter-navigate-lookAtAreaWithGeoOrientationAndViewRectangle-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Create an update to look at the given geo-box and fit it inside the given rectangle.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatareawithviewrectangle">lookAtAreaWithViewRectangle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookAtAreaWithViewRectangle-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-navigate-lookAtAreaWithViewRectangle-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to look at the given geo-box and fit it inside the given rectangle, preserving current orientation and zooming at the center of view rectangle.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatpoint">lookAtPoint</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookAtPoint-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to position the map camera to look at the given target, preserving the current orientation at look-at target and map measure.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatpoints">lookAtPoints</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookAtPoints-param-points" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">points</span>, </span><span id="sdk-for-flutter-navigate-lookAtPoints-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span>, </span><span id="sdk-for-flutter-navigate-lookAtPoints-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span><span id="sdk-for-flutter-navigate-lookAtPoints-param-measureLimit" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">measureLimit</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Create an update to look at the given geo locations and fit them inside the given rectangle, in accordance with a map measure limit.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatpointwithgeoorientationandmeasure">lookAtPointWithGeoOrientationAndMeasure</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookAtPointWithGeoOrientationAndMeasure-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-navigate-lookAtPointWithGeoOrientationAndMeasure-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span><span id="sdk-for-flutter-navigate-lookAtPointWithGeoOrientationAndMeasure-param-measure" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">measure</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to position the map camera to look at the given target with the given orientation and map measure.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatpointwithmeasure">lookAtPointWithMeasure</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookAtPointWithMeasure-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-navigate-lookAtPointWithMeasure-param-measure" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">measure</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to position the map camera to look at the given target with the given map measure preserving the current orientation at look-at target.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookatpointwithorientation">lookAtPointWithOrientation</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookAtPointWithOrientation-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-navigate-lookAtPointWithOrientation-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to position the map camera to look at the given target with the given orientation preserving the current map measure (zoom level/distance/scale) Any target or orientation sub-element value that is not finite will be excluded from the update.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-lookattargetandpoints">lookAtTargetAndPoints</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-target" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinatesupdate-class">GeoCoordinatesUpdate</a></span> <span class="parameter-name">target</span>, </span><span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span><span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-points" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">points</span>, </span><span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-viewRectangle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a></span> <span class="parameter-name">viewRectangle</span>, </span><span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-minMeasure" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">minMeasure</span>, </span><span id="sdk-for-flutter-navigate-lookAtTargetAndPoints-param-maxMeasure" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">maxMeasure</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to position the camera to look at the given target with the given orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpoint">lookToMatchGeoPointToViewPoint</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookToMatchGeoPointToViewPoint-param-geoPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">geoPoint</span>, </span><span id="sdk-for-flutter-navigate-lookToMatchGeoPointToViewPoint-param-viewPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">viewPoint</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to position the map camera to look at the map with the given geo point located at the given view point.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpointwithorientationmapmeasure">lookToMatchGeoPointToViewPointWithOrientationMapMeasure</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-lookToMatchGeoPointToViewPointWithOrientationMapMeasure-param-geoPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span> <span class="parameter-name">geoPoint</span>, </span><span id="sdk-for-flutter-navigate-lookToMatchGeoPointToViewPointWithOrientationMapMeasure-param-viewPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">viewPoint</span>, </span><span id="sdk-for-flutter-navigate-lookToMatchGeoPointToViewPointWithOrientationMapMeasure-param-orientation" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">orientation</span>, </span><span id="sdk-for-flutter-navigate-lookToMatchGeoPointToViewPointWithOrientationMapMeasure-param-measure" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span> <span class="parameter-name">measure</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to position the map camera to look at the map with the given orientation and map measure and with the given geo point located at the given view point.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-orbitby">orbitBy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-orbitBy-param-delta" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">delta</span>, </span><span id="sdk-for-flutter-navigate-orbitBy-param-origin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">origin</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-panby">panBy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-panBy-param-xOffset" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">xOffset</span>, </span><span id="sdk-for-flutter-navigate-panBy-param-yOffset" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">yOffset</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to pan map camera over the map by the specified number of pixels in the x and y direction starting from current principal point position.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-rotateby">rotateBy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-rotateBy-param-delta" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geoorientationupdate-class">GeoOrientationUpdate</a></span> <span class="parameter-name">delta</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to change map camera orientation by specified geodetic orientation delta.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-setnormalizedprincipalpoint">setNormalizedPrincipalPoint</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setNormalizedPrincipalPoint-param-principalPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">principalPoint</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is (0.5, 0.5)).

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-setprincipalpoint">setPrincipalPoint</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setPrincipalPoint-param-principalPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">principalPoint</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is the center of the view).

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-setverticalfieldofview">setVerticalFieldOfView</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setVerticalFieldOfView-param-verticalFieldOfView" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">verticalFieldOfView</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to change the vertical field of view of the map camera.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-zoomby">zoomBy</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-zoomBy-param-factor" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">factor</span>, </span><span id="sdk-for-flutter-navigate-zoomBy-param-origin" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a></span> <span class="parameter-name">origin</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to zoom map camera by a given factor preserving a given focus point.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapcameraupdatefactory-zoomto">zoomTo</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-zoomTo-param-zoomLevel" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">zoomLevel</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapcameraupdate-class">MapCameraUpdate</a></span> </span>  
Creates an update to move map camera's viewpoint to a particular zoom level by adjusting its position.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
