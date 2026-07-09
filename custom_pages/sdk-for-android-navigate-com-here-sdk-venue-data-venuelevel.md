---
title: "VenueLevel (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueLevel.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.data</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.data.VenueLevel</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VenueLevel</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents one level of a building or a complex of buildings inside the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getGeometryByCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>getGeometryByCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span className="element-name">getGeometryByCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div className="block"><p>Gets a geometry by coordinates.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates inside the searching geometry.</p></dd>
<dt>Returns:</dt>
<dd><p>The geometry covering the coordinates or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometriesByCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>getGeometriesByCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span className="element-name">getGeometriesByCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div className="block"><p>Gets geometries by coordinates.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates inside the searching geometries.</p></dd>
<dt>Returns:</dt>
<dd><p>The list of geometries covering the coordinate or an empty list.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometryById(java.lang.String)">
<h3>getGeometryById</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span className="element-name">getGeometryById</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryId)</span></div>
<div className="block"><p>Gets a geometry by an id.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geometryId</code> - <p>The id of the geometry.</p></dd>
<dt>Returns:</dt>
<dd><p>The geometry with the given id or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometryByAddress(java.lang.String)">
<h3>getGeometryByAddress</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span className="element-name">getGeometryByAddress</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> geometryAddress)</span></div>
<div className="block"><p>Gets a geometry by the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry-internaladdress" title="class in com.here.sdk.venue.data"><code>VenueGeometry.InternalAddress</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geometryAddress</code> - <p>The internal address as a String.</p></dd>
<dt>Returns:</dt>
<dd><p>The geometry with the given address or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="filterGeometry(java.lang.String,com.here.sdk.venue.data.VenueGeometryFilterType)">
<h3>filterGeometry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span className="element-name">filterGeometry</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filter,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometryfiltertype" title="enum class in com.here.sdk.venue.data">VenueGeometryFilterType</a> filterType)</span></div>
<div className="block"><p>Gets the filtered geometries in an ascending order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>filter</code> - <p>The filter string.</p></dd>
<dd><code>filterType</code> - <p>The filter type.</p></dd>
<dt>Returns:</dt>
<dd><p>The list of the filtered geometries or an empty list.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTopologyByCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>getTopologyByCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a></span> <span className="element-name">getTopologyByCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div className="block"><p>Gets a topology by coordinates.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates inside the searching topology.</p></dd>
<dt>Returns:</dt>
<dd><p>The topology covering the coordinates or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCrosswalkByCoordinates(com.here.sdk.core.GeoCoordinates)">
<h3>getCrosswalkByCoordinates</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a></span> <span className="element-name">getCrosswalkByCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates)</span></div>
<div className="block"><p>Gets a crosswalk by coordinates.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The coordinates inside the searching crosswalk.</p></dd>
<dt>Returns:</dt>
<dd><p>The crosswalk covering the coordinates or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getIdentifier()">
<h3>getIdentifier</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getIdentifier</span>()</div>
<div className="block"><p>Gets an id of the level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>id</code> of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getZIndex()">
<h3>getZIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getZIndex</span>()</div>
<div className="block"><p>Gets an order in the z direction (altitude).
 Z index 0 represents
 a ground level, negative values represent underground levels,
 positive values - levels above ground.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The Z index of the level, an order in the z direction (altitude).</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getProperties()">
<h3>getProperties</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="sdk-for-android-navigate-com-here-sdk-venue-data-property" title="class in com.here.sdk.venue.data">Property</a>&gt;</span> <span className="element-name">getProperties</span>()</div>
<div className="block"><p>Gets properties of the level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The properties of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getName()">
<h3>getName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getName</span>()</div>
<div className="block"><p>Gets a 'name' property of the level from the level properties.
 If the 'name' property is missing in the properties, the string will be empty.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The name property of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getShortName()">
<h3>getShortName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getShortName</span>()</div>
<div className="block"><p>Gets a short name of the level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The short name of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isMainLevel()">
<h3>isMainLevel</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isMainLevel</span>()</div>
<div className="block"><p>Indicates if this level is the main level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><code>True</code> if this is the main level and <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDrawing()">
<h3>getDrawing</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span className="element-name">getDrawing</span>()</div>
<div className="block"><p>Gets a parent drawing of the level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The parent drawing of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometries()">
<h3>getGeometries</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span className="element-name">getGeometries</span>()</div>
<div className="block"><p>Gets a list of geometries of the level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of geometries of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDrawingID()">
<h3>getDrawingID</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getDrawingID</span>()</div>
<div className="block"><p>Gets drawing ID of the level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The drawing ID of level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCenter()">
<h3>getCenter</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getCenter</span>()</div>
<div className="block"><p>Gets a center of the level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the center of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">getBoundingBox</span>()</div>
<div className="block"><p>Gets a bounding box of the level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>GeoBox</code> of the bounding area.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometriesByName()">
<h3>getGeometriesByName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span className="element-name">getGeometriesByName</span>()</div>
<div className="block"><p>Gets the geometries ordered by a name in an ascending order.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geometries ordered by the name in an ascending order.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometriesByIconNames()">
<h3>getGeometriesByIconNames</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;&gt;</span> <span className="element-name">getGeometriesByIconNames</span>()</div>
<div className="block"><p>Gets the geometries mapped by icon names.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The map from the icon names to the geometries in the drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTopologies()">
<h3>getTopologies</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuetopology" title="class in com.here.sdk.venue.data">VenueTopology</a>&gt;</span> <span className="element-name">getTopologies</span>()</div>
<div className="block"><p>Gets a list of topologies of the level.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of topologies of the level.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCrosswalks()">
<h3>getCrosswalks</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-crosswalk" title="class in com.here.sdk.venue.data">Crosswalk</a>&gt;</span> <span className="element-name">getCrosswalks</span>()</div>
<div className="block"><p>Gets a list of crosswalks of the level.</p></div>
<dl className="notes">
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
</div>



</div>
`
}</HTMLBlock>
