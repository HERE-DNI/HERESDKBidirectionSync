---
title: "VenueDrawing (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueDrawing.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.data</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.data.VenueDrawing</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VenueDrawing</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a drawing inside the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>. The drawing can be
 a separate building in a complex of buildings, or show a different
 view of a venue. For example, in an airport, one drawing can be used
 as an overview of all buildings in this venue, while other drawings
 contains details for each terminal in this airport.</p></div>
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
<div className="block"><p>Gets filtered geometries in an ascending order.</p></div>
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
<section className="detail" id="getIdentifier()">
<h3>getIdentifier</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getIdentifier</span>()</div>
<div className="block"><p>Gets an id of the drawing.
 This describes the identifier for drawing.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>id</code> of the drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="isRoot()">
<h3>isRoot</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isRoot</span>()</div>
<div className="block"><p>Checks if this is a root drawing of the venue.
 This can be used to check if this is top level
 drawing in venue.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><code>True</code> if this is the root drawing and <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVenueModel()">
<h3>getVenueModel</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data">VenueModel</a></span> <span className="element-name">getVenueModel</span>()</div>
<div className="block"><p>Gets a parent venue model.
 It can be used to get the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel" title="class in com.here.sdk.venue.data"><code>VenueModel</code></a>
 where this Drawing belong.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The parent venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLevels()">
<h3>getLevels</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a>&gt;</span> <span className="element-name">getLevels</span>()</div>
<div className="block"><p>Gets levels of the drawing.
 This describes for which all level this
 drawing belongs.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The array with Level objects.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCenter()">
<h3>getCenter</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getCenter</span>()</div>
<div className="block"><p>Gets a center of the drawing.
 It can be used to get center coordinates of drawing.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The Geographic coordinates of the center of the drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">getBoundingBox</span>()</div>
<div className="block"><p>Gets a bounding box of the drawing.
 This is used to check if at certain zoom level
 and inside view this GeoBox belongs, then need to render.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>GeoBox</code> of the bounding area of the drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getProperties()">
<h3>getProperties</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="sdk-for-android-navigate-com-here-sdk-venue-data-property" title="class in com.here.sdk.venue.data">Property</a>&gt;</span> <span className="element-name">getProperties</span>()</div>
<div className="block"><p>Gets properties of the drawing.
 This can be used to get different properties
 like name belonging to Drawing.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The key-value pairs of properties.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometriesByName()">
<h3>getGeometriesByName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span className="element-name">getGeometriesByName</span>()</div>
<div className="block"><p>Gets geometries ordered by a name in an ascending order.
 This can be used to search geometries by name.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geometries ordered by the name.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometriesByIconNames()">
<h3>getGeometriesByIconNames</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;&gt;</span> <span className="element-name">getGeometriesByIconNames</span>()</div>
<div className="block"><p>Gets geometries mapped by icon names.
 This can be used to search the geometries by icon names.</p></div>
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
<div className="block"><p>Gets a list of topologies of the drawing.
 This can be used to check for which
 all topologies are realted to Drawing.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of topologies of the drawing.</p></dd>
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
