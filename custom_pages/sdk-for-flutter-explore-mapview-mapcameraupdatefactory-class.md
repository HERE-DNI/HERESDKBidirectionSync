---
title: "MapCameraUpdateFactory class abstract"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapCameraUpdateFactory-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapCameraUpdateFactory-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapCameraUpdateFactory/MapCameraUpdateFactory.html">MapCameraUpdateFactory</a></li>
<li class="section-title inherited">
<a href="mapview/MapCameraUpdateFactory-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapCameraUpdateFactory/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapCameraUpdateFactory/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MapCameraUpdateFactory-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapCameraUpdateFactory/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapCameraUpdateFactory/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapCameraUpdateFactory-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapCameraUpdateFactory/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="mapview/MapCameraUpdateFactory-class.html#static-methods">Static methods</a></li>
<li><a href="mapview/MapCameraUpdateFactory/compositeUpdate.html">compositeUpdate</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookAtArea.html">lookAtArea</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookAtAreaWithGeoOrientationAndViewRectangle.html">lookAtAreaWithGeoOrientationAndViewRectangle</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookAtAreaWithViewRectangle.html">lookAtAreaWithViewRectangle</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookAtPoint.html">lookAtPoint</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookAtPoints.html">lookAtPoints</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookAtPointWithGeoOrientationAndMeasure.html">lookAtPointWithGeoOrientationAndMeasure</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookAtPointWithMeasure.html">lookAtPointWithMeasure</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookAtPointWithOrientation.html">lookAtPointWithOrientation</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookAtTargetAndPoints.html">lookAtTargetAndPoints</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookToMatchGeoPointToViewPoint.html">lookToMatchGeoPointToViewPoint</a></li>
<li><a href="mapview/MapCameraUpdateFactory/lookToMatchGeoPointToViewPointWithOrientationMapMeasure.html">lookToMatchGeoPointToViewPointWithOrientationMapMeasure</a></li>
<li><a href="mapview/MapCameraUpdateFactory/orbitBy.html">orbitBy</a></li>
<li><a href="mapview/MapCameraUpdateFactory/panBy.html">panBy</a></li>
<li><a href="mapview/MapCameraUpdateFactory/rotateBy.html">rotateBy</a></li>
<li><a href="mapview/MapCameraUpdateFactory/setNormalizedPrincipalPoint.html">setNormalizedPrincipalPoint</a></li>
<li><a href="mapview/MapCameraUpdateFactory/setPrincipalPoint.html">setPrincipalPoint</a></li>
<li><a href="mapview/MapCameraUpdateFactory/setVerticalFieldOfView.html">setVerticalFieldOfView</a></li>
<li><a href="mapview/MapCameraUpdateFactory/zoomBy.html">zoomBy</a></li>
<li><a href="mapview/MapCameraUpdateFactory/zoomTo.html">zoomTo</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapCameraUpdateFactory class</li>
</ol>
<div class="self-name">MapCameraUpdateFactory</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapCameraUpdateFactory-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapCameraUpdateFactory class abstract</h1></div>
<section class="desc markdown">
<p>Factory for creating MapCameraUpdate to change map's camera.</p>
<p>For some factory methods you can apply an additional padding in pixels by setting a
<code>viewRectangle</code> parameter based on the current size of the map view:</p>
<pre class="language-dart"><code>var leftPaddingInPixels = 5;
var rightPaddingInPixels = 5;
var topPaddingInPixels = 5;
var bottomPaddingInPixels = 5;
var horizontalPaddingInPixels = leftPaddingInPixels + rightPaddingInPixels;
var verticalPaddingInPixels = topPaddingInPixels + bottomPaddingInPixels;

var origin = Point2D(leftPaddingInPixels, topPaddingInPixels);
var sizeInPixels = Size2D(_hereMapController.viewportSize.width - horizontalPaddingInPixels, _hereMapController.viewportSize.height - verticalPaddingInPixels);
var paddedViewRectangle = Rectangle2D(origin, sizeInPixels);
</code></pre>
<p>The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates
also the top-left corner of the map's viewport.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapCameraUpdateFactory">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-mapcameraupdatefactory()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="compositeUpdate">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-compositeupdate(<wbr/>List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapcameraupdate-class&gt; mapCameraUpdates)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates a composite camera update from a list of camera updates.
  

</dd>
<dt class="callable" id="lookAtArea">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatarea(<wbr/>/sdk-for-flutter-explore-core-geobox-class target)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to look at the given geo-box,
preserving current orientation and zooming at the center of viewport.
  

</dd>
<dt class="callable" id="lookAtAreaWithGeoOrientationAndViewRectangle">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatareawithgeoorientationandviewrectangle(<wbr/>/sdk-for-flutter-explore-core-geobox-class target, /sdk-for-flutter-explore-core-geoorientationupdate-class orientation, /sdk-for-flutter-explore-core-rectangle2d-class viewRectangle)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Create an update to look at the given geo-box and fit it inside the given rectangle.
  

</dd>
<dt class="callable" id="lookAtAreaWithViewRectangle">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatareawithviewrectangle(<wbr/>/sdk-for-flutter-explore-core-geobox-class target, /sdk-for-flutter-explore-core-rectangle2d-class viewRectangle)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to look at the given geo-box and fit it inside the given rectangle,
preserving current orientation and zooming at the center of view rectangle.
  

</dd>
<dt class="callable" id="lookAtPoint">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpoint(<wbr/>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to position the map camera to look at the given target,
preserving the current orientation at look-at target and map measure.
  

</dd>
<dt class="callable" id="lookAtPoints">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpoints(<wbr/>List&lt;<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class&gt; points, /sdk-for-flutter-explore-core-rectangle2d-class viewRectangle, /sdk-for-flutter-explore-core-geoorientationupdate-class orientation, /sdk-for-flutter-explore-mapview-mapmeasure-class measureLimit)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Create an update to look at the given geo locations and fit them inside the given rectangle,
in accordance with a map measure limit.
  

</dd>
<dt class="callable" id="lookAtPointWithGeoOrientationAndMeasure">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpointwithgeoorientationandmeasure(<wbr/>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target, /sdk-for-flutter-explore-core-geoorientationupdate-class orientation, /sdk-for-flutter-explore-mapview-mapmeasure-class measure)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to position the map camera to look at the given target with the given
orientation and map measure.
  

</dd>
<dt class="callable" id="lookAtPointWithMeasure">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpointwithmeasure(<wbr/>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target, /sdk-for-flutter-explore-mapview-mapmeasure-class measure)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to position the map camera to look at the given target with the given
map measure preserving the current orientation at look-at target.
  

</dd>
<dt class="callable" id="lookAtPointWithOrientation">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookatpointwithorientation(<wbr/>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target, /sdk-for-flutter-explore-core-geoorientationupdate-class orientation)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to position the map camera to look at the given target with the given
orientation preserving the current map measure (zoom level/distance/scale)
Any target or orientation sub-element value that is not finite will be excluded from the update.
  

</dd>
<dt class="callable" id="lookAtTargetAndPoints">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-lookattargetandpoints(<wbr/>/sdk-for-flutter-explore-core-geocoordinatesupdate-class target, /sdk-for-flutter-explore-core-geoorientationupdate-class orientation, List&lt;<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class&gt; points, /sdk-for-flutter-explore-core-rectangle2d-class viewRectangle, /sdk-for-flutter-explore-mapview-mapmeasure-class minMeasure, /sdk-for-flutter-explore-mapview-mapmeasure-class maxMeasure)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to position the camera to look at the given target with the given
orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.
  

</dd>
<dt class="callable" id="lookToMatchGeoPointToViewPoint">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpoint(<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class geoPoint, /sdk-for-flutter-explore-core-point2d-class viewPoint)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to position the map camera to look at the map
with the given geo point located at the given view point.
  

</dd>
<dt class="callable" id="lookToMatchGeoPointToViewPointWithOrientationMapMeasure">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-looktomatchgeopointtoviewpointwithorientationmapmeasure(<wbr/>/sdk-for-flutter-explore-core-geocoordinates-class geoPoint, /sdk-for-flutter-explore-core-point2d-class viewPoint, /sdk-for-flutter-explore-core-geoorientationupdate-class orientation, /sdk-for-flutter-explore-mapview-mapmeasure-class measure)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to position the map camera to look at the map with the given
orientation and map measure and with the given geo point located at the given view point.
  

</dd>
<dt class="callable" id="orbitBy">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-orbitby(<wbr/>/sdk-for-flutter-explore-core-geoorientationupdate-class delta, /sdk-for-flutter-explore-core-point2d-class origin)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.
  

</dd>
<dt class="callable" id="panBy">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-panby(<wbr/>double xOffset, double yOffset)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to pan map camera over the map by the specified number of pixels
in the x and y direction starting from current principal point position.
  

</dd>
<dt class="callable" id="rotateBy">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-rotateby(<wbr/>/sdk-for-flutter-explore-core-geoorientationupdate-class delta)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to change map camera orientation by specified geodetic orientation delta.
  

</dd>
<dt class="callable" id="setNormalizedPrincipalPoint">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setnormalizedprincipalpoint(<wbr/>/sdk-for-flutter-explore-core-anchor2d-class principalPoint)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to change the map camera's principal point (where the view vector
intersects the image plane - default is (0.5, 0.5)).
  

</dd>
<dt class="callable" id="setPrincipalPoint">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setprincipalpoint(<wbr/>/sdk-for-flutter-explore-core-point2d-class principalPoint)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to change the map camera's principal point (where the view vector intersects
the image plane - default is the center of the view).
  

</dd>
<dt class="callable" id="setVerticalFieldOfView">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setverticalfieldofview(<wbr/>double verticalFieldOfView)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to change the vertical field of view of the map camera.
  

</dd>
<dt class="callable" id="zoomBy">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-zoomby(<wbr/>double factor, /sdk-for-flutter-explore-core-point2d-class origin)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to zoom map camera by a given factor preserving a given focus point.
  

</dd>
<dt class="callable" id="zoomTo">
/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-zoomto(<wbr/>double zoomLevel)
    → /sdk-for-flutter-explore-mapview-mapcameraupdate-class

</dt>
<dd>
  Creates an update to move map camera's viewpoint to a particular zoom level by adjusting its position.
  

</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapCameraUpdateFactory class</li>
</ol>
<h5>mapview library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
