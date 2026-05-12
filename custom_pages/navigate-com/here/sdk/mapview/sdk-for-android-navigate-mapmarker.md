---
title: "MapMarker (API Reference)"
slug: "sdk-for-android-navigate-mapmarker"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapMarker.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapMarker</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapMarker</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p><code>MapMarker</code> is used to draw images on the map, for example to mark a specific location.
 By default, the marker is centered on the given geographic coordinates.
 Markers keep their size regardless of the current zoom level of the map view.
 </p><p>The image to be displayed is represented by <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview"><code>MapImage</code></a> object. For performance reasons,
 it is highly recommended to reuse a single instance of the image when creating multiple
 identical markers.
 </p><p>To display the map marker, it needs to be added to the scene using <a href="sdk-for-android-navigate-mapscene#addMapMarker(com.here.sdk.mapview.MapMarker)"><code>MapScene.addMapMarker(com.here.sdk.mapview.MapMarker)</code></a>.
 To stop displaying it, remove it from the scene using <a href="sdk-for-android-navigate-mapscene#removeMapMarker(com.here.sdk.mapview.MapMarker)"><code>MapScene.removeMapMarker(com.here.sdk.mapview.MapMarker)</code></a>.
 </p><p>The display of a map marker is only guaranteed in case its origin is within the viewport.
 At the moment, this is a known limitation that mostly affects map markers which are visually
 large and cover a sizeable part of the viewport.
 </p><p><strong>Note:</strong>
 Due to technical limitations using the MapMarkers API to add a very large number of markers
 (several thousands, especially 10000+) is not recommended. Adding this many markers will have a
 negative impact on the performance leading to stuttering of the app and lower frame rates.
 To work around this limitation the following approach can be used:
 Register to map camera updates using <a href="sdk-for-android-navigate-mapcamera#addListener(com.here.sdk.mapview.MapCameraListener)"><code>MapCamera.addListener(com.here.sdk.mapview.MapCameraListener)</code></a>. Query the bounding box of the
 camera viewport using <a href="sdk-for-android-navigate-mapcamera#getBoundingBox()"><code>MapCamera.getBoundingBox()</code></a> (it may be extended)
 and then use the method <a href="sdk-for-android-navigate-core-geobox#contains(com.here.sdk.core.GeoCoordinates)"><code>GeoBox.contains(GeoCoordinates)</code></a> in combination with
 <a href="sdk-for-android-navigate-mapcamera.state#distanceToTargetInMeters"><code>MapCamera.State.distanceToTargetInMeters</code></a> to determine which MapMarkers are actually visible
 to the user in the current camera viewport and thus need to be added to the map.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-navigate-mapmarker.textstyle" title="class in com.here.sdk.mapview">MapMarker.TextStyle</a></code></div>
<div class="col-last even-row-color">
<div class="block">Styling options for the text of a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage)">MapMarker</a><wbr/>(<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of a marker at given coordinates, represented by specified image.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)">MapMarker</a><wbr/>(<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 <a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates an instance of a marker at given coordinates, represented by specified image,
 with anchor point specifying how the image is positioned relative to the marker's coordinates.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,java.lang.String)">MapMarker</a><wbr/>(<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a <code>MapMarker</code> instance at given coordinates with specified image and text and a default text style.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#cancelAnimation(com.here.sdk.animation.MapMarkerAnimation)">cancelAnimation</a><wbr/>(<a href="sdk-for-android-navigate-animation-mapmarkeranimation" title="class in com.here.sdk.animation">MapMarkerAnimation</a> animation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Cancels single ongoing animation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAnchor()">getAnchor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets current anchor point for the marker image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCoordinates()">getCoordinates</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the point on the map where the marker is drawn.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDrawOrder()">getDrawOrder</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets draw order of this marker relative to other markers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFadeDuration()">getFadeDuration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getImage()">getImage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets currently used map image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-core-metadata" title="class in com.here.sdk.core">Metadata</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetadata()">getMetadata</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the Metadata instance attached to this marker.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOpacity()">getOpacity</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current opacity of the marker image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getText()">getText</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the text drawn on the map by the <code>MapMarker</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmarker.textstyle" title="class in com.here.sdk.mapview">MapMarker.TextStyle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTextStyle()">getTextStyle</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a copy of the <code>TextStyle</code> currently in use by the <code>MapMarker</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibilityRanges()">getVisibilityRanges</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of visibility ranges.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isOverlapAllowed()">isOverlapAllowed</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns <code>true</code> if the marker allows overlap with other markers, <code>false</code> otherwise.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isTextOptional()">isTextOptional</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns <code>true</code> if the marker allows text to be hidden, <code>false</code> otherwise.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAnchor(com.here.sdk.core.Anchor2D)">setAnchor</a><wbr/>(<a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets anchor point of the marker image which specifies the position offset relative
 to the marker's coordinates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setCoordinates(com.here.sdk.core.GeoCoordinates)">setCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the point on the map where the marker is drawn.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDrawOrder(int)">setDrawOrder</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets draw order of this marker relative to other markers.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFadeDuration(com.here.time.Duration)">setFadeDuration</a><wbr/>(<a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setImage(com.here.sdk.mapview.MapImage)">setImage</a><wbr/>(<a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets map image used to represent the marker on screen.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMetadata(com.here.sdk.core.Metadata)">setMetadata</a><wbr/>(<a href="sdk-for-android-navigate-core-metadata" title="class in com.here.sdk.core">Metadata</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the Metadata instance attached to this marker.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOpacity(double)">setOpacity</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the opacity of the marker image.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOverlapAllowed(boolean)">setOverlapAllowed</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether the marker is allowed to overlap with other markers.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setText(java.lang.String)">setText</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the text to be drawn on the map by the <code>MapMarker</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTextOptional(boolean)">setTextOptional</a><wbr/>(boolean value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets whether the marker is allowed to appear without text.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setTextStyle(com.here.sdk.mapview.MapMarker.TextStyle)">setTextStyle</a><wbr/>(<a href="sdk-for-android-navigate-mapmarker.textstyle" title="class in com.here.sdk.mapview">MapMarker.TextStyle</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <code>TextStyle</code> to be used by the <code>MapMarker</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisibilityRanges(java.util.List)">setVisibilityRanges</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets visibility ranges for this map marker.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#startAnimation(com.here.sdk.animation.MapMarkerAnimation,com.here.sdk.animation.AnimationListener)">startAnimation</a><wbr/>(<a href="sdk-for-android-navigate-animation-mapmarkeranimation" title="class in com.here.sdk.animation">MapMarkerAnimation</a> animation,
 <a href="sdk-for-android-navigate-animation-animationlistener" title="interface in com.here.sdk.animation">AnimationListener</a> animationListener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts animation of this map marker according to provided <a href="sdk-for-android-navigate-animation-mapmarkeranimation" title="class in com.here.sdk.animation"><code>MapMarkerAnimation</code></a>.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage)">
<h3>MapMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</span></div>
<div class="block"><p>Creates an instance of a marker at given coordinates, represented by specified image.
 </p><p>The altitude component of the coordinates is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The marker's geographical coordinates.</p></dd>
<dd><code>image</code> - <p>The image to draw on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,java.lang.String)">
<h3>MapMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block"><p>Creates a <code>MapMarker</code> instance at given coordinates with specified image and text and a default text style.
 </p><p>The altitude component of the coordinates is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The marker's geographical coordinates.</p></dd>
<dd><code>image</code> - <p>The image to draw on the map.</p></dd>
<dd><code>text</code> - <p>The text to draw on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)">
<h3>MapMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapMarker</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 @NonNull
 <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 @NonNull
 <a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor)</span></div>
<div class="block"><p>Creates an instance of a marker at given coordinates, represented by specified image,
 with anchor point specifying how the image is positioned relative to the marker's coordinates.
 </p><p>The anchor is a way of specifying position offset relative to image's dimensions on the screen.
 For example, (0, 0) places the top-left corner of the image at the marker's coordinates.
 (1, 1) would place the bottom-right corner of the image at the marker's coordinates.
 (0.5, 0.5) which is the default value would center the image at the marker's coordinates.
 Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
 centered horizontally with its bottom edge above the marker's coordinates at the distance
 in pixels that is equal to the height of the image.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The marker's geographical coordinates.</p></dd>
<dd><code>image</code> - <p>The image to draw on the map.</p></dd>
<dd><code>anchor</code> - <p>The anchor point for the marker image which specifies the position offset relative
     to the marker's coordinates.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="startAnimation(com.here.sdk.animation.MapMarkerAnimation,com.here.sdk.animation.AnimationListener)">
<h3>startAnimation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startAnimation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-animation-mapmarkeranimation" title="class in com.here.sdk.animation">MapMarkerAnimation</a> animation,
 @Nullable
 <a href="sdk-for-android-navigate-animation-animationlistener" title="interface in com.here.sdk.animation">AnimationListener</a> animationListener)</span></div>
<div class="block"><p>Starts animation of this map marker according to provided <a href="sdk-for-android-navigate-animation-mapmarkeranimation" title="class in com.here.sdk.animation"><code>MapMarkerAnimation</code></a>.
 </p><p>The <code>MapMarkerAnimation</code> may be shared between multiple instances of <code>MapMarker</code>.
 </p><p>Starting animation on one map marker does not influence any ongoing animations on other map markers.
 Any ongoing animation of this marker instance will get cancelled.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>animation</code> - <p>The animation to start, may be used for multiple different map markers.</p></dd>
<dd><code>animationListener</code> - <p>The listener to receive notifications about animation start, completion or cancellation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cancelAnimation(com.here.sdk.animation.MapMarkerAnimation)">
<h3>cancelAnimation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">cancelAnimation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-animation-mapmarkeranimation" title="class in com.here.sdk.animation">MapMarkerAnimation</a> animation)</span></div>
<div class="block"><p>Cancels single ongoing animation.
 </p><p>Does nothing if animation was not started for this map marker.
 </p><p>Does not cancel other animations if the same <a href="sdk-for-android-navigate-animation-mapmarkeranimation" title="class in com.here.sdk.animation"><code>MapMarkerAnimation</code></a> object was applied to multiple <code>MapMarker</code>s.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>animation</code> - <p>The animation to cancel.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCoordinates()">
<h3>getCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getCoordinates</span>()</div>
<div class="block"><p>Gets the point on the map where the marker is drawn.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The point on the map where the map marker is drawn.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>setCoordinates</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> value)</span></div>
<div class="block"><p>Sets the point on the map where the marker is drawn.
 The altitude component of the coordinates is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The point on the map where the map marker is drawn.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadata()">
<h3>getMetadata</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-metadata" title="class in com.here.sdk.core">Metadata</a></span> <span class="element-name">getMetadata</span>()</div>
<div class="block"><p>Gets the Metadata instance attached to this marker.
 This will be <code>null</code> if nothing has been attached before.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The Metadata instance attached to this marker, see <a href="sdk-for-android-navigate-core-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMetadata(com.here.sdk.core.Metadata)">
<h3>setMetadata</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMetadata</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-core-metadata" title="class in com.here.sdk.core">Metadata</a> value)</span></div>
<div class="block"><p>Sets the Metadata instance attached to this marker.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The Metadata instance attached to this marker, see <a href="sdk-for-android-navigate-core-metadata" title="class in com.here.sdk.core"><code>Metadata</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isOverlapAllowed()">
<h3>isOverlapAllowed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isOverlapAllowed</span>()</div>
<div class="block"><p>Returns <code>true</code> if the marker allows overlap with other markers, <code>false</code> otherwise.
 Defaults to <code>true</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Determines whether or not the marker can overlap other markers.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOverlapAllowed(boolean)">
<h3>setOverlapAllowed</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOverlapAllowed</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether the marker is allowed to overlap with other markers.
 </p><p>If <code>false</code>, it will disappear the moment it overlaps another marker that has
 a higher visibility priority. A marker that allows overlap will always be drawn.
 Among markers that don't allow overlap, the one with the highest draw order has
 priority. Marker that is hidden due to overlapping with other markers is not pickable.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Determines whether or not the marker can overlap other markers.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isTextOptional()">
<h3>isTextOptional</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTextOptional</span>()</div>
<div class="block"><p>Returns <code>true</code> if the marker allows text to be hidden, <code>false</code> otherwise.
 Defaults to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Determines if the marker can be displayed with icon and without text.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTextOptional(boolean)">
<h3>setTextOptional</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTextOptional</span><wbr/><span class="parameters">(boolean value)</span></div>
<div class="block"><p>Sets whether the marker is allowed to appear without text.
 </p><p>Controls whenever <code>MapMarker</code> can be shown as icon only when <a href="#isOverlapAllowed()"><code>isOverlapAllowed()</code></a>
 is <code>false</code>, has no effect otherwise. If <code>false</code> then the <code>MapMarker</code> will not appear
 when icon or text are blocked by other labels.
 If <code>true</code>, icon will appear even if the text part is blocked by other labels.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Determines if the marker can be displayed with icon and without text.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawOrder()">
<h3>getDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDrawOrder</span>()</div>
<div class="block"><p>Gets draw order of this marker relative to other markers. The default value is 0.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The draw order of this marker relative to other markers.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDrawOrder(int)">
<h3>setDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrder</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>Sets draw order of this marker relative to other markers.
 </p><p>Markers with higher draw order value are drawn on top of markers with lower draw order.
 In case multiple markers have the same draw order value
 then the order in which they were added to the scene matters. Last added marker is drawn on top.
 </p><p>Allowed range is [0, 1023]. Values outside this range will be clamped. The default value is 0.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The draw order of this marker relative to other markers.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImage()">
<h3>getImage</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span class="element-name">getImage</span>()</div>
<div class="block"><p>Gets currently used map image.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Image representing the marker on the screen.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImage(com.here.sdk.mapview.MapImage)">
<h3>setImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImage</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapimage" title="class in com.here.sdk.mapview">MapImage</a> value)</span></div>
<div class="block"><p>Sets map image used to represent the marker on screen.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Image representing the marker on the screen.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnchor()">
<h3>getAnchor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span class="element-name">getAnchor</span>()</div>
<div class="block"><p>Gets current anchor point for the marker image.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The anchor point for the marker image which specifies the position offset relative
     to the marker's coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAnchor(com.here.sdk.core.Anchor2D)">
<h3>setAnchor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAnchor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span></div>
<div class="block"><p>Sets anchor point of the marker image which specifies the position offset relative
 to the marker's coordinates.
 </p><p>For example, (0, 0) places the top-left corner of the image at the marker's coordinates.
 (1, 1) would place the bottom-right corner of the image at the marker's coordinates.
 (0.5, 0.5) which is the default value would center the image at the marker's coordinates.
 Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
 centered horizontally with its bottom edge above the marker's coordinates at the distance
 in pixels that is equal to the height of the image.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The anchor point for the marker image which specifies the position offset relative
     to the marker's coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOpacity()">
<h3>getOpacity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOpacity</span>()</div>
<div class="block"><p>Gets the current opacity of the marker image. Value is in the range of [0.0, 1.0].
 Default value is 1.0.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Opacity, the factor applied to the alpha channel of the marker image.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOpacity(double)">
<h3>setOpacity</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOpacity</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the opacity of the marker image.
 </p><p>Provided value is clamped to the range of [0.0, 1.0]. Default value is 1.0,
 which means marker is displayed with the default opacity of the image.
 </p><p>Markers with opacity value set to 0.0 are still on the map and are considered for picking.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Opacity, the factor applied to the alpha channel of the marker image.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFadeDuration()">
<h3>getFadeDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getFadeDuration</span>()</div>
<div class="block"><p>Gets the current duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFadeDuration(com.here.time.Duration)">
<h3>setFadeDuration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFadeDuration</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a> value)</span></div>
<div class="block"><p>Sets duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.
 </p><p>Provided value is clamped in range [0.0, 10.0] seconds. Default value is 0 seconds which means the effect is disabled
 and marker is added/removed immediately without any animation.
 Fade-in effect is also applied when marker leaves and then re-enters screen area.
 </p><p>Change to this property is made asynchronously and is not guaranteed
 to take effect on the next rendered frame. In particular, changing fade duration and removing
 the marker immediately after may result in the new value being ignored for this removal.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getText()">
<h3>getText</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getText</span>()</div>
<div class="block"><p>Gets the text drawn on the map by the <code>MapMarker</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The text to be drawn on the map along with the image of the <code>MapMarker</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setText(java.lang.String)">
<h3>setText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setText</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>Sets the text to be drawn on the map by the <code>MapMarker</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The text to be drawn on the map along with the image of the <code>MapMarker</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTextStyle()">
<h3>getTextStyle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmarker.textstyle" title="class in com.here.sdk.mapview">MapMarker.TextStyle</a></span> <span class="element-name">getTextStyle</span>()</div>
<div class="block"><p>Gets a copy of the <code>TextStyle</code> currently in use by the <code>MapMarker</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <code>TextStyle</code> applied to the text of the <code>MapMarker</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTextStyle(com.here.sdk.mapview.MapMarker.TextStyle)">
<h3>setTextStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTextStyle</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmarker.textstyle" title="class in com.here.sdk.mapview">MapMarker.TextStyle</a> value)</span></div>
<div class="block"><p>Sets the <code>TextStyle</code> to be used by the <code>MapMarker</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The <code>TextStyle</code> applied to the text of the <code>MapMarker</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibilityRanges()">
<h3>getVisibilityRanges</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</span> <span class="element-name">getVisibilityRanges</span>()</div>
<div class="block"><p>Gets the list of visibility ranges. The map marker is visible only inside these map measure
 ranges. When empty (the default), the map marker is visible without map measure restrictions.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of visibility ranges. The map marker is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisibilityRanges(java.util.List)">
<h3>setVisibilityRanges</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibilityRanges</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</span></div>
<div class="block"><p>Sets visibility ranges for this map marker.
 </p><p>A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.
 The map marker is visible only inside these map measure ranges.
 </p><p>When empty (the default), the map marker is visible without map measure restrictions.
 Only <code>MapMeasureRange</code>(s) of <a href="sdk-for-android-navigate-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <code>MapMeasureRange</code>(s) of other unsupported types will be ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The list of visibility ranges. The map marker is visible only inside these map measure ranges.</p></dd>
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
