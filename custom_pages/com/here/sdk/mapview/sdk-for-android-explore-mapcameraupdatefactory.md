---
title: "MapCameraUpdateFactory (API Reference)"
slug: "sdk-for-android-explore-mapcameraupdatefactory"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapCameraUpdateFactory.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapCameraUpdateFactory</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapCameraUpdateFactory</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Factory for creating MapCameraUpdate to change map's camera.
 </p><p>For some factory methods you can apply an additional padding in pixels by setting a
 <code>viewRectangle</code> parameter based on the current size of the map view:
 <pre><code>int leftPaddingInPixels = 5;
 int rightPaddingInPixels = 5;
 int topPaddingInPixels = 5;
 int bottomPaddingInPixels = 5;
 int horizontalPaddingInPixels = leftPaddingInPixels + rightPaddingInPixels;
 int verticalPaddingInPixels = topPaddingInPixels + bottomPaddingInPixels;

 Point2D origin = new Point2D(leftPaddingInPixels, topPaddingInPixels);
 Size2D sizeInPixels = new Size2D(mapView.getWidth() - horizontalPaddingInPixels, mapView.getHeight() - verticalPaddingInPixels);
 Rectangle2D paddedViewRectangle = new Rectangle2D(origin, sizeInPixels);
 </code></pre>
</p><p>The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates
 also the top-left corner of the map's viewport.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#compositeUpdate(java.util.List)">compositeUpdate</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a>&gt; mapCameraUpdates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a composite camera update from a list of camera updates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAt(com.here.sdk.core.GeoBox)">lookAt</a><wbr/>(<a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to look at the given geo-box,
 preserving current orientation and zooming at the center of viewport.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Rectangle2D)">lookAt</a><wbr/>(<a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target,
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 <a href="sdk-for-android-explore-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an update to look at the given geo-box and fit it inside the given rectangle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.Rectangle2D)">lookAt</a><wbr/>(<a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target,
 <a href="sdk-for-android-explore-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to look at the given geo-box and fit it inside the given rectangle,
 preserving current orientation and zooming at the center of view rectangle.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAt(com.here.sdk.core.GeoCoordinatesUpdate)">lookAt</a><wbr/>(<a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to position the map camera to look at the given target,
 preserving the current orientation at look-at target and map measure.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate)">lookAt</a><wbr/>(<a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to position the map camera to look at the given target with the given
 orientation preserving the current map measure (zoom level/distance/scale)
 Any target or orientation sub-element value that is not finite will be excluded from the update.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">lookAt</a><wbr/>(<a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measure)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to position the map camera to look at the given target with the given
 orientation and map measure.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapMeasure,com.here.sdk.mapview.MapMeasure)">lookAt</a><wbr/>(<a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; points,
 <a href="sdk-for-android-explore-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle,
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> minMeasure,
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> maxMeasure)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to position the camera to look at the given target with the given
 orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.mapview.MapMeasure)">lookAt</a><wbr/>(<a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measure)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to position the map camera to look at the given target with the given
 map measure preserving the current orientation at look-at target.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookAt(java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">lookAt</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; points,
 <a href="sdk-for-android-explore-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle,
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measureLimit)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Create an update to look at the given geo locations and fit them inside the given rectangle,
 in accordance with a map measure limit.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D)">lookToMatch</a><wbr/>(<a href="sdk-for-android-explore-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoPoint,
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewPoint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to position the map camera to look at the map
 with the given geo point located at the given view point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">lookToMatch</a><wbr/>(<a href="sdk-for-android-explore-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoPoint,
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewPoint,
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measure)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to position the map camera to look at the map with the given
 orientation and map measure and with the given geo point located at the given view point.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#orbitBy(com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Point2D)">orbitBy</a><wbr/>(<a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> delta,
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#panBy(double,double)">panBy</a><wbr/>(double xOffset,
 double yOffset)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to pan map camera over the map by the specified number of pixels
 in the x and y direction starting from current principal point position.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#rotateBy(com.here.sdk.core.GeoOrientationUpdate)">rotateBy</a><wbr/>(<a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> delta)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to change map camera orientation by specified geodetic orientation delta.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">setNormalizedPrincipalPoint</a><wbr/>(<a href="sdk-for-android-explore-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> principalPoint)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to change the map camera's principal point (where the view vector
 intersects the image plane - default is (0.5, 0.5)).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setPrincipalPoint(com.here.sdk.core.Point2D)">setPrincipalPoint</a><wbr/>(<a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> principalPoint)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to change the map camera's principal point (where the view vector intersects
 the image plane - default is the center of the view).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#setVerticalFieldOfView(double)">setVerticalFieldOfView</a><wbr/>(double verticalFieldOfView)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to change the vertical field of view of the map camera.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#zoomBy(double,com.here.sdk.core.Point2D)">zoomBy</a><wbr/>(double factor,
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to zoom map camera by a given factor preserving a given focus point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#zoomTo(double)">zoomTo</a><wbr/>(double zoomLevel)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates an update to move map camera's viewpoint to a particular zoom level by adjusting its position.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate)">
<h3>lookAt</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookAt</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target)</span></div>
<div class="block"><p>Creates an update to position the map camera to look at the given target,
 preserving the current orientation at look-at target and map measure.
 </p><p>Any target sub-element value that is not finite will be excluded from the update.
 </p><p>The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates, altitude is ignored,
     the target is considered to be located on the ground.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate)">
<h3>lookAt</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookAt</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation)</span></div>
<div class="block"><p>Creates an update to position the map camera to look at the given target with the given
 orientation preserving the current map measure (zoom level/distance/scale)
 Any target or orientation sub-element value that is not finite will be excluded from the update.
 </p><p>The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at look-at target.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookAt</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measure)</span></div>
<div class="block"><p>Creates an update to position the map camera to look at the given target with the given
 map measure preserving the current orientation at look-at target.
 Any target sub-element value that is not finite will be excluded from the update.
 If the map measure is not valid, the current map camera distance to the target point is preserved.
 </p><p>The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates.</p></dd>
<dd><code>measure</code> - <p>The desired map measure.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookAt</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measure)</span></div>
<div class="block"><p>Creates an update to position the map camera to look at the given target with the given
 orientation and map measure.
 Any target or orientation sub-element value that is not finite will be excluded from the update.
 If the map measure is not valid, the current map camera distance to the target point is preserved.
 </p><p>The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at look-at target.</p></dd>
<dd><code>measure</code> - <p>The desired map measure.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">
<h3>lookToMatch</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookToMatch</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoPoint,
 @NonNull
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewPoint,
 @NonNull
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measure)</span></div>
<div class="block"><p>Creates an update to position the map camera to look at the map with the given
 orientation and map measure and with the given geo point located at the given view point.
 </p><p>The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.
 </p><p>Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoPoint</code> - <p>The geo point that will be matched to the given view point.
     Note: the geo point will differ from the look at target of the camera. After this update the camera
     will still look at the principal point and therefore the look at target will be different from the geo
     point, since the geo point will correspond to the given view point and the look at target
     will correspond to the principal point. Look at target and the geo point will be identical only
     if the given view point is identical to the principal point.</p></dd>
<dd><code>viewPoint</code> - <p>View point coordinates in pixels.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at look-at target.</p></dd>
<dd><code>measure</code> - <p>The desired map measure.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D)">
<h3>lookToMatch</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookToMatch</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoPoint,
 @NonNull
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewPoint)</span></div>
<div class="block"><p>Creates an update to position the map camera to look at the map
 with the given geo point located at the given view point.
 Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.
 </p><p>The altitude of the target point is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoPoint</code> - <p>The geo point that will be matched to the given view point.
     Note: the geo point will differ from the look at target of the camera. After this update the camera
     will still look at the principal point and therefore the look at target will be different from the geo
     point, since the geo point will correspond to the given view point and the look at target
     will correspond to the principal point. Look at target and the geo point will be identical only
     if the given view point is identical to the principal point.</p></dd>
<dd><code>viewPoint</code> - <p>View point coordinates in pixels.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAt(java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookAt</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; points,
 @NonNull
 <a href="sdk-for-android-explore-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle,
 @NonNull
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> measureLimit)</span></div>
<div class="block"><p>Create an update to look at the given geo locations and fit them inside the given rectangle,
 in accordance with a map measure limit.
 </p><p>If the provided <code>points</code> list is empty, no update will be applied to the camera.
 </p><p>If the <code>viewRectangle</code> parameter is invalid, fully or partially outside the map view,
 then the entire map viewport will be used as <code>viewRectangle</code>. Thus, no padding will be applied.
 A <code>viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
 coordinates (x, y) are invalid, when they are negative.
 </p><p>All <code>viewRectangle</code> values need to be finite to be considered as valid.
 If measure limit is not valid, no update will be applied to the map camera.
 </p><p>The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>points</code> - <p>Array of points in geodetic space that should be visible inside the given view rectangle.</p></dd>
<dd><code>viewRectangle</code> - <p>View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at the new calculated target point.</p></dd>
<dd><code>measureLimit</code> - <p>Map measure limit:
     <ul>
<li>as distance: the minimum distance from map camera to earth surface at the center of the view rectangle in meters.
     The map camera should not be positioned closer to the center of view rectangle than this.</li>
<li>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the center of view rectangle in meters. This is not the zoom level for
     the calculated lookAt target point. Can be used to not zoom closer than a given level.</li>
<li>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the center of view rectangle in meters. This is not the scale for
     the calculated lookAt target point.</li>
</ul></p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapMeasure,com.here.sdk.mapview.MapMeasure)">
<h3>lookAt</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookAt</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geocoordinatesupdate" title="class in com.here.sdk.core">GeoCoordinatesUpdate</a> target,
 @NonNull
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; points,
 @NonNull
 <a href="sdk-for-android-explore-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> minMeasure,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> maxMeasure)</span></div>
<div class="block"><p>Creates an update to position the camera to look at the given target with the given
 orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.
 Such position update can possibly not be found.
 </p><p>Any target or orientation sub-element value that is not finite will be excluded from the update.
 </p><p>If the provided <code>points</code> list is empty, no update will be applied to the map camera.
 </p><p>If the <code>viewRectangle</code> parameter is invalid, fully or partially outside the map view,
 then the entire map viewport will be used as <code>viewRectangle</code>. Thus, no padding will be applied.
 A <code>viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
 coordinates (x, y) are invalid, when they are negative.
 </p><p>If map measures are not valid, no update will be applied to the map camera.
 </p><p>The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>The look-at target position in geodetic coordinates.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at look-at target.</p></dd>
<dd><code>points</code> - <p>Array of points in geodetic space that should be visible inside the given view rectangle.</p></dd>
<dd><code>viewRectangle</code> - <p>View rectangle in viewport pixel coordinates inside which the geographical points are displayed.</p></dd>
<dd><code>minMeasure</code> - <p>Minimum map measure:
     <ul>
<li>as distance: the minimum distance from map camera to earth surface at the look-at target in meters.
     The map camera should not be positioned closer to target than this.</li>
<li>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the look-at target in meters.
     Can be used to not zoom closer than a given level.</li>
<li>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the look-at target in meters.</li>
</ul></p></dd>
<dd><code>maxMeasure</code> - <p>Maximum map measure:
     <ul>
<li>as distance: the maximum distance from map camera to earth surface at the look-at target in meters.
     The map camera should not be positioned further from target than this.</li>
<li>as zoom level: the minimum zoom level for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the look-at target in meters.
     Can be used to not zoom further than a given level.</li>
<li>as scale: the maximum scale for the new map camera state. Internally converted to minimum distance
     from map camera to earth surface at the look-at target in meters.</li>
</ul></p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Rectangle2D)">
<h3>lookAt</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookAt</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target,
 @NonNull
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> orientation,
 @NonNull
 <a href="sdk-for-android-explore-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle)</span></div>
<div class="block"><p>Create an update to look at the given geo-box and fit it inside the given rectangle.
 </p><p>If geoBox is not valid, no update will be applied to the map camera.
 </p><p>If the <code>viewRectangle</code> parameter is invalid, fully or partially outside the map view,
 then the entire map viewport will be used as <code>viewRectangle</code>. Thus, no padding will be applied.
 A <code>viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
 coordinates (x, y) are invalid, when they are negative.
 </p><p>All <code>viewRectangle</code> values need to be finite to be considered as valid.
 </p><p>In cases where it is not possible to find a solution for the given parameters,
 the resulting MapCameraUpdate will not change the map camera.
 </p><p>The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic box that should be visible inside the given view rectangle.</p></dd>
<dd><code>orientation</code> - <p>Geodetic orientation at the target point.</p></dd>
<dd><code>viewRectangle</code> - <p>View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.Rectangle2D)">
<h3>lookAt</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookAt</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target,
 @NonNull
 <a href="sdk-for-android-explore-core-rectangle2d" title="class in com.here.sdk.core">Rectangle2D</a> viewRectangle)</span></div>
<div class="block"><p>Creates an update to look at the given geo-box and fit it inside the given rectangle,
 preserving current orientation and zooming at the center of view rectangle.
 </p><p>If geoBox is not valid, no update will be applied to the map camera.
 </p><p>If the <code>viewRectangle</code> parameter is invalid, fully or partially outside the map view,
 then the entire map viewport will be used as <code>viewRectangle</code>. Thus, no padding will be applied.
 A <code>viewRectangle</code> is considered invalid, when its width or height are negative or zero, its origin
 coordinates (x, y) are invalid, when they are negative.
 </p><p>In cases where it is not possible to find a solution for the given parameters,
 the resulting MapCameraUpdate will not change the map camera.
 </p><p>The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic box that should be visible inside the given view rectangle.</p></dd>
<dd><code>viewRectangle</code> - <p>View rectangle in viewport pixel coordinates.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="lookAt(com.here.sdk.core.GeoBox)">
<h3>lookAt</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">lookAt</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geobox" title="class in com.here.sdk.core">GeoBox</a> target)</span></div>
<div class="block"><p>Creates an update to look at the given geo-box,
 preserving current orientation and zooming at the center of viewport.
 </p><p>If geoBox is not valid, no update will be applied to the map camera.
 </p><p>The altitude of the target points is ignored. Any subsequent camera updates and animations
 will consider the target point as being located on the ground.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>target</code> - <p>Geodetic box that should be visible inside the viewport rectangle.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="panBy(double,double)">
<h3>panBy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">panBy</span><wbr/><span class="parameters">(double xOffset,
 double yOffset)</span></div>
<div class="block"><p>Creates an update to pan map camera over the map by the specified number of pixels
 in the x and y direction starting from current principal point position.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>xOffset</code> - <p>X offset in pixels</p></dd>
<dd><code>yOffset</code> - <p>Y offset in pixels</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="orbitBy(com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Point2D)">
<h3>orbitBy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">orbitBy</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> delta,
 @NonNull
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin)</span></div>
<div class="block"><p>Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.
 If the origin cannot be converted to geo coordinates, no update will be applied to the map camera.
 </p><p>Orientation elements that are not valid will be excluded from the update.
 Resulting bearing values are wrapped around degrees range [0, 360].
 Resulting tilt values are clamped inside degrees range [0, 180].
 Resulting roll values are wrapped around degrees range [-180, 180].</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>delta</code> - <p>Geodetic orientation delta update.</p></dd>
<dd><code>origin</code> - <p>Screen pixel origin of rotation.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="rotateBy(com.here.sdk.core.GeoOrientationUpdate)">
<h3>rotateBy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">rotateBy</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geoorientationupdate" title="class in com.here.sdk.core">GeoOrientationUpdate</a> delta)</span></div>
<div class="block"><p>Creates an update to change map camera orientation by specified geodetic orientation delta.
 Orientation elements that are not valid will be excluded from the update.
 Resulting bearing values are wrapped around degrees range [0, 360].
 Resulting tilt values are clamped inside degrees range [0, 180].
 Resulting roll values are wrapped around degrees range [-180, 180].</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>delta</code> - <p>Geodetic orientation delta update.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="zoomBy(double,com.here.sdk.core.Point2D)">
<h3>zoomBy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">zoomBy</span><wbr/><span class="parameters">(double factor,
 @NonNull
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin)</span></div>
<div class="block"><p>Creates an update to zoom map camera by a given factor preserving a given focus point.
 </p><p>Values greater than 1 zoom in map camera, by moving it closer to the ground; less than 1 - zoom out,
 which moves map camera further.
 </p><p>If factor is zero, negative or not finite, no update will be applied to the map camera.
 </p><p>If the focusPoint is not inside the viewport bounds, then the current principal point will be used.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>factor</code> - <p>Zooming factor.</p></dd>
<dd><code>origin</code> - <p>Pixel location on the screen to use as zoom origin.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="zoomTo(double)">
<h3>zoomTo</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">zoomTo</span><wbr/><span class="parameters">(double zoomLevel)</span></div>
<div class="block"><p>Creates an update to move map camera's viewpoint to a particular zoom level by adjusting its position.
 </p><p>If zoomLevel is not finite, no update will be applied to the map camera.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>zoomLevel</code> - <p>The desired zoom level.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setPrincipalPoint(com.here.sdk.core.Point2D)">
<h3>setPrincipalPoint</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">setPrincipalPoint</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> principalPoint)</span></div>
<div class="block"><p>Creates an update to change the map camera's principal point (where the view vector intersects
 the image plane - default is the center of the view). Point values are in screen coordinates
 and values that fall outside of the viewport, are clamped.
 (0,0) is top left of the viewport.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>principalPoint</code> - <p>Principal point in absolute viewport pixel coordinates.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">
<h3>setNormalizedPrincipalPoint</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">setNormalizedPrincipalPoint</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> principalPoint)</span></div>
<div class="block"><p>Creates an update to change the map camera's principal point (where the view vector
 intersects the image plane - default is (0.5, 0.5)). Point values are in normalized screen coordinates.
 </p><p>If the principalPoint is outside [0,1] interval, it is clamped.
 (0,0) is top left of the viewport, (1,1) is bottom right.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>principalPoint</code> - <p>Principal point in normalized screen coordinates.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVerticalFieldOfView(double)">
<h3>setVerticalFieldOfView</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">setVerticalFieldOfView</span><wbr/><span class="parameters">(double verticalFieldOfView)</span></div>
<div class="block"><p>Creates an update to change the vertical field of view of the map camera.
 </p><p>If verticalFieldOfView is not finite, no update will be applied to the map camera.
 </p><p>If the verticalFieldOfView is outside [1, 150] interval, it is clamped.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>verticalFieldOfView</code> - <p>Vertical field of view in degrees.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compositeUpdate(java.util.List)">
<h3>compositeUpdate</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a></span> <span class="element-name">compositeUpdate</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapcameraupdate" title="class in com.here.sdk.mapview">MapCameraUpdate</a>&gt; mapCameraUpdates)</span>
                                       throws <span class="exceptions"><a href="sdk-for-android-explore-mapcameraupdate.instantiationexception" title="class in com.here.sdk.mapview">MapCameraUpdate.InstantiationException</a></span></div>
<div class="block"><p>Creates a composite camera update from a list of camera updates. The result update will be
 equivalent to executing all given updates sequentially in the order they were provided.
 </p><p>MapCameraAnimation instances derived from the MapCameraAnimationFactory and a composite camera
 update are not supported. An AnimationListener will receive an AnimationState.Cancelled signal
 when trying to apply such animations.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>mapCameraUpdates</code> - <p>List of MapCamera updates.</p></dd>
<dt>Returns:</dt>
<dd><p>MapCameraUpdate instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-mapcameraupdate.instantiationexception" title="class in com.here.sdk.mapview">MapCameraUpdate.InstantiationException</a></code> - <p>Indicates an instantiation issue.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
