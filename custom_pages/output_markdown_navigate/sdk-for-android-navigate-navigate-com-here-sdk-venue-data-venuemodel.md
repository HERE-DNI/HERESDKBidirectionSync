---
title: "VenueModel (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-venue-data-venuemodel"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueModel.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-..-help-doc#class">Help</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.data</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-..-..-..-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.venue.data.VenueModel</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VenueModel</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-..-..-..-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents a building or a complex of buildings, like airports or universities.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#filterGeometry(java.lang.String,com.here.sdk.venue.data.VenueGeometryFilterType)">filterGeometry</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 <a href="sdk-for-android-navigate-venuegeometryfiltertype" title="enum class in com.here.sdk.venue.data">VenueGeometryFilterType</a> filterType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the filtered geometries in an ascending order.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-..-..-core-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBoundingBox()">getBoundingBox</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a bounding box of the venue model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-..-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCenter()">getCenter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a center of the venue model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDrawing(int)">getDrawing</a><wbr/>(int drawingId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a drawing for a given drawing id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDrawing(java.lang.String)">getDrawing</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> drawingId)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a drawing for a given drawing id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDrawings()">getDrawings</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the drawings of the venue model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeometries()">getGeometries</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a list of geometries of the venue.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeometriesByIconNames()">getGeometriesByIconNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets geometries mapped by icon names.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeometriesByName()">getGeometriesByName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the geometries ordered by the name in an ascending order.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getId()">getId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets an <code>id</code> of the venue model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getIdentifier()">getIdentifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets an <code>id</code> of the venue model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLanguage()">getLanguage</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a language of the venue model.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="sdk-for-android-navigate-property" title="class in com.here.sdk.venue.data">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getProperties()">getProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets properties of the venue model.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTopologies()">getTopologies</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a list of topologies of the drawing.</div>
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
<section class="detail" id="getDrawing(int)">
<h3>getDrawing</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span class="element-name">getDrawing</span><wbr/><span class="parameters">(int drawingId)</span></div>
<div class="block"><p>Gets a drawing for a given drawing id.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>drawingId</code> - <p>The id of the drawing.</p></dd>
<dt>Returns:</dt>
<dd><p>The drawing with the given id or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawing(java.lang.String)">
<h3>getDrawing</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span class="element-name">getDrawing</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> drawingId)</span></div>
<div class="block"><p>Gets a drawing for a given drawing id.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>drawingId</code> - <p>The id of the drawing.</p></dd>
<dt>Returns:</dt>
<dd><p>The drawing with the given id or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="filterGeometry(java.lang.String,com.here.sdk.venue.data.VenueGeometryFilterType)">
<h3>filterGeometry</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span class="element-name">filterGeometry</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 @NonNull
 <a href="sdk-for-android-navigate-venuegeometryfiltertype" title="enum class in com.here.sdk.venue.data">VenueGeometryFilterType</a> filterType)</span></div>
<div class="block"><p>Gets the filtered geometries in an ascending order.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filter</code> - <p>The filter string.</p></dd>
<dd><code>filterType</code> - <p>The filter type.</p></dd>
<dt>Returns:</dt>
<dd><p>The list of the filtered geometries or an empty list.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getId</span>()</div>
<div class="block"><p>Gets an <code>id</code> of the venue model.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <code>id</code> of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIdentifier()">
<h3>getIdentifier</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIdentifier</span>()</div>
<div class="block"><p>Gets an <code>id</code> of the venue model.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <code>id</code> of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCenter()">
<h3>getCenter</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-..-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getCenter</span>()</div>
<div class="block"><p>Gets a center of the venue model.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the center of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-..-..-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">getBoundingBox</span>()</div>
<div class="block"><p>Gets a bounding box of the venue model.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <code>GeoBox</code> of the bounding area of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawings()">
<h3>getDrawings</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a>&gt;</span> <span class="element-name">getDrawings</span>()</div>
<div class="block"><p>Gets the drawings of the venue model.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The array of the Drawing objects.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="sdk-for-android-navigate-property" title="class in com.here.sdk.venue.data">Property</a>&gt;</span> <span class="element-name">getProperties</span>()</div>
<div class="block"><p>Gets properties of the venue model.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The properties of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLanguage()">
<h3>getLanguage</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getLanguage</span>()</div>
<div class="block"><p>Gets a language of the venue model.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The language of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometriesByName()">
<h3>getGeometriesByName</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span class="element-name">getGeometriesByName</span>()</div>
<div class="block"><p>Gets the geometries ordered by the name in an ascending order.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The geometries ordered by the name in an ascending order.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometriesByIconNames()">
<h3>getGeometriesByIconNames</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;&gt;</span> <span class="element-name">getGeometriesByIconNames</span>()</div>
<div class="block"><p>Gets geometries mapped by icon names.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The map from the icon names to the geometries in the drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTopologies()">
<h3>getTopologies</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>&gt;</span> <span class="element-name">getTopologies</span>()</div>
<div class="block"><p>Gets a list of topologies of the drawing.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of topologies of the drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometries()">
<h3>getGeometries</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span class="element-name">getGeometries</span>()</div>
<div class="block"><p>Gets a list of geometries of the venue.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of geometries of the venue or an empty list if no geometry present for venue.</p></dd>
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
