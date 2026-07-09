---
title: "VenueGeometry (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueGeometry.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.data</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.data.VenueGeometry</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VenueGeometry</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a geometry inside the <a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>. The geometry can be any object
 inside the level, like a room, a wall or a table. Also the geometry can represent virtual
 objects, like a team area in an open space.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry-geometrytype" title="enum class in com.here.sdk.venue.data">VenueGeometry.GeometryType</a></code></div>
<div className="col-last even-row-color">
<div className="block">Geometry types.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry-internaladdress" title="class in com.here.sdk.venue.data">VenueGeometry.InternalAddress</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Represents an internal addresses of the geometry inside the venue.</div>
</div>
<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry-lookuptype" title="enum class in com.here.sdk.venue.data">VenueGeometry.LookupType</a></code></div>
<div className="col-last even-row-color">
<div className="block">Defines how the geometry will be presented.</div>
</div>
</div>
</section>
</li>
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
<section className="detail" id="getIdentifier()">
<h3>getIdentifier</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getIdentifier</span>()</div>
<div className="block"><p>Gets an id of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>id</code> of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLevel()">
<h3>getLevel</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a></span> <span className="element-name">getLevel</span>()</div>
<div className="block"><p>Gets a parent level of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The parent level of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometryType()">
<h3>getGeometryType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry-geometrytype" title="enum class in com.here.sdk.venue.data">VenueGeometry.GeometryType</a></span> <span className="element-name">getGeometryType</span>()</div>
<div className="block"><p>Gets a type of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The type of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCenter()">
<h3>getCenter</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getCenter</span>()</div>
<div className="block"><p>Gets a center of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the center of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">getBoundingBox</span>()</div>
<div className="block"><p>Gets a bounding box of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>GeoBox</code> of the bounding area of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getProperties()">
<h3>getProperties</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="sdk-for-android-navigate-com-here-sdk-venue-data-property" title="class in com.here.sdk.venue.data">Property</a>&gt;</span> <span className="element-name">getProperties</span>()</div>
<div className="block"><p>Gets the properties of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The properties of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getInternalAddress()">
<h3>getInternalAddress</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry-internaladdress" title="class in com.here.sdk.venue.data">VenueGeometry.InternalAddress</a></span> <span className="element-name">getInternalAddress</span>()</div>
<div className="block"><p>Gets an internal address of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The internal address of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getName()">
<h3>getName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getName</span>()</div>
<div className="block"><p>Gets a name of the geometry.
 If no name has been set, returns a label name.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The name of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLabelName()">
<h3>getLabelName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getLabelName</span>()</div>
<div className="block"><p>Gets a label name of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The label name of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLookupType()">
<h3>getLookupType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry-lookuptype" title="enum class in com.here.sdk.venue.data">VenueGeometry.LookupType</a></span> <span className="element-name">getLookupType</span>()</div>
<div className="block"><p>Gets a lookup type of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The lookup type of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getParentGeometry()">
<h3>getParentGeometry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a></span> <span className="element-name">getParentGeometry</span>()</div>
<div className="block"><p>Gets a parent geometry on which the current geometry is located.
 Defaults to <code>null</code>, if the geometry represents a base shape.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The parent geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStyle()">
<h3>getStyle</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuegeometrystyle" title="class in com.here.sdk.venue.style">VenueGeometryStyle</a></span> <span className="element-name">getStyle</span>()</div>
<div className="block"><p>Gets a style of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The style of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLabelStyle()">
<h3>getLabelStyle</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-style-venuelabelstyle" title="class in com.here.sdk.venue.style">VenueLabelStyle</a></span> <span className="element-name">getLabelStyle</span>()</div>
<div className="block"><p>Gets a label style of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The label style of the geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLevelID()">
<h3>getLevelID</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getLevelID</span>()</div>
<div className="block"><p>Gets level ID of the geometry.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The level ID of geometry.</p></dd>
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
