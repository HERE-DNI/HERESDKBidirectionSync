---
title: "VenueLevel (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueLevel.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.venue.data.VenueLevel</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">VenueLevel</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents one level of a building or a complex of buildings inside the <a href="sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#filterGeometry(java.lang.String,com.here.sdk.venue.data.VenueGeometryFilterType)">filterGeometry</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 <a href="sdk-for-android-navigate-venuegeometryfiltertype" title="enum class in com.here.sdk.venue.data">VenueGeometryFilterType</a> filterType)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the filtered geometries in an ascending order.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getBoundingBox()">getBoundingBox</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a bounding box of the level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getCenter()">getCenter</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a center of the level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getCrosswalkByCoordinates(com.here.sdk.core.GeoCoordinates)">getCrosswalkByCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a crosswalk by coordinates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getCrosswalks()">getCrosswalks</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a list of crosswalks of the level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getDrawing()">getDrawing</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a parent drawing of the level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getDrawingID()">getDrawingID</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets drawing ID of the level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getGeometries()">getGeometries</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a list of geometries of the level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getGeometriesByCoordinates(com.here.sdk.core.GeoCoordinates)">getGeometriesByCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets geometries by coordinates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getGeometriesByIconNames()">getGeometriesByIconNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the geometries mapped by icon names.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getGeometriesByName()">getGeometriesByName</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the geometries ordered by a name in an ascending order.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getGeometryByAddress(java.lang.String)">getGeometryByAddress</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryAddress)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a geometry by the <a href="sdk-for-android-navigate-venuegeometry.internaladdress" title="class in com.here.sdk.venue.data"><code>VenueGeometry.InternalAddress</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getGeometryByCoordinates(com.here.sdk.core.GeoCoordinates)">getGeometryByCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a geometry by coordinates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getGeometryById(java.lang.String)">getGeometryById</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a geometry by an id.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getIdentifier()">getIdentifier</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets an id of the level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getName()">getName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a 'name' property of the level from the level properties.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="sdk-for-android-navigate-property" title="class in com.here.sdk.venue.data">Property</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getProperties()">getProperties</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets properties of the level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getShortName()">getShortName</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a short name of the level.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getTopologies()">getTopologies</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a list of topologies of the level.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getTopologyByCoordinates(com.here.sdk.core.GeoCoordinates)">getTopologyByCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets a topology by coordinates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#getZIndex()">getZIndex</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets an order in the z direction (altitude).</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel#isMainLevel()">isMainLevel</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Indicates if this level is the main level.</div>
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
<section class="detail" id="getGeometryByCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>getGeometryByCoordinates</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span class="element-name">getGeometryByCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div class="block"><p>Gets a geometry by coordinates.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates inside the searching geometry.</p></dd>
<dt>Returns:</dt>
<dd><p>The geometry covering the coordinates or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometriesByCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>getGeometriesByCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span class="element-name">getGeometriesByCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div class="block"><p>Gets geometries by coordinates.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates inside the searching geometries.</p></dd>
<dt>Returns:</dt>
<dd><p>The list of geometries covering the coordinate or an empty list.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometryById(java.lang.String)">
<h3>getGeometryById</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span class="element-name">getGeometryById</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryId)</span></div>
<div class="block"><p>Gets a geometry by an id.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometryId</code> - <p>The id of the geometry.</p></dd>
<dt>Returns:</dt>
<dd><p>The geometry with the given id or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometryByAddress(java.lang.String)">
<h3>getGeometryByAddress</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span class="element-name">getGeometryByAddress</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryAddress)</span></div>
<div class="block"><p>Gets a geometry by the <a href="sdk-for-android-navigate-venuegeometry.internaladdress" title="class in com.here.sdk.venue.data"><code>VenueGeometry.InternalAddress</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometryAddress</code> - <p>The internal address as a String.</p></dd>
<dt>Returns:</dt>
<dd><p>The geometry with the given address or <code>null</code>.</p></dd>
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
<section class="detail" id="getTopologyByCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>getTopologyByCoordinates</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a></span> <span class="element-name">getTopologyByCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div class="block"><p>Gets a topology by coordinates.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates inside the searching topology.</p></dd>
<dt>Returns:</dt>
<dd><p>The topology covering the coordinates or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCrosswalkByCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>getCrosswalkByCoordinates</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a></span> <span class="element-name">getCrosswalkByCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div class="block"><p>Gets a crosswalk by coordinates.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates inside the searching crosswalk.</p></dd>
<dt>Returns:</dt>
<dd><p>The crosswalk covering the coordinates or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIdentifier()">
<h3>getIdentifier</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getIdentifier</span>()</div>
<div class="block"><p>Gets an id of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <code>id</code> of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getZIndex()">
<h3>getZIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getZIndex</span>()</div>
<div class="block"><p>Gets an order in the z direction (altitude).
 </p><p>Z index 0 represents
 a ground level, negative values represent underground levels,
 positive values - levels above ground.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The Z index of the level, an order in the z direction (altitude).</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProperties()">
<h3>getProperties</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="sdk-for-android-navigate-property" title="class in com.here.sdk.venue.data">Property</a>&gt;</span> <span class="element-name">getProperties</span>()</div>
<div class="block"><p>Gets properties of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The properties of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getName()">
<h3>getName</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getName</span>()</div>
<div class="block"><p>Gets a 'name' property of the level from the level properties.
 </p><p>If the 'name' property is missing in the properties, the string will be empty.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The name property of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getShortName()">
<h3>getShortName</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getShortName</span>()</div>
<div class="block"><p>Gets a short name of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The short name of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isMainLevel()">
<h3>isMainLevel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isMainLevel</span>()</div>
<div class="block"><p>Indicates if this level is the main level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p><code>True</code> if this is the main level and <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawing()">
<h3>getDrawing</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span class="element-name">getDrawing</span>()</div>
<div class="block"><p>Gets a parent drawing of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The parent drawing of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometries()">
<h3>getGeometries</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span class="element-name">getGeometries</span>()</div>
<div class="block"><p>Gets a list of geometries of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of geometries of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawingID()">
<h3>getDrawingID</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getDrawingID</span>()</div>
<div class="block"><p>Gets drawing ID of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The drawing ID of level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCenter()">
<h3>getCenter</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">getCenter</span>()</div>
<div class="block"><p>Gets a center of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the center of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">getBoundingBox</span>()</div>
<div class="block"><p>Gets a bounding box of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <code>GeoBox</code> of the bounding area.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometriesByName()">
<h3>getGeometriesByName</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span class="element-name">getGeometriesByName</span>()</div>
<div class="block"><p>Gets the geometries ordered by a name in an ascending order.</p></div>
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
<div class="block"><p>Gets the geometries mapped by icon names.</p></div>
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
<div class="block"><p>Gets a list of topologies of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of topologies of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCrosswalks()">
<h3>getCrosswalks</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a>&gt;</span> <span class="element-name">getCrosswalks</span>()</div>
<div class="block"><p>Gets a list of crosswalks of the level.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of crosswalks of the level.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
