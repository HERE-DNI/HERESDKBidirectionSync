---
title: "VenueModel (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-data-venuemodel"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- VenueModel.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.data</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.data.VenueModel</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">VenueModel</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a building or a complex of buildings, like airports or universities.</p></div>
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
<section className="detail" id="getDrawing(int)">
<h3>getDrawing</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span className="element-name">getDrawing</span><wbr/><span className="parameters">(int drawingId)</span></div>
<div className="block"><p>Gets a drawing for a given drawing id.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>drawingId</code> - <p>The id of the drawing.</p></dd>
<dt>Returns:</dt>
<dd><p>The drawing with the given id or <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDrawing(java.lang.String)">
<h3>getDrawing</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a></span> <span className="element-name">getDrawing</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> drawingId)</span></div>
<div className="block"><p>Gets a drawing for a given drawing id.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>drawingId</code> - <p>The id of the drawing.</p></dd>
<dt>Returns:</dt>
<dd><p>The drawing with the given id or <code>null</code>.</p></dd>
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
<section className="detail" id="getId()">
<h3>getId</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getId</span>()</div>
<div className="block"><p>Gets an <code>id</code> of the venue model.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>id</code> of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getIdentifier()">
<h3>getIdentifier</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getIdentifier</span>()</div>
<div className="block"><p>Gets an <code>id</code> of the venue model.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>id</code> of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCenter()">
<h3>getCenter</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">getCenter</span>()</div>
<div className="block"><p>Gets a center of the venue model.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geographic coordinates of the center of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBoundingBox()">
<h3>getBoundingBox</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">getBoundingBox</span>()</div>
<div className="block"><p>Gets a bounding box of the venue model.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>GeoBox</code> of the bounding area of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDrawings()">
<h3>getDrawings</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a>&gt;</span> <span className="element-name">getDrawings</span>()</div>
<div className="block"><p>Gets the drawings of the venue model.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The array of the Drawing objects.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getProperties()">
<h3>getProperties</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>,<wbr/><a href="sdk-for-android-navigate-com-here-sdk-venue-data-property" title="class in com.here.sdk.venue.data">Property</a>&gt;</span> <span className="element-name">getProperties</span>()</div>
<div className="block"><p>Gets properties of the venue model.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The properties of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLanguage()">
<h3>getLanguage</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getLanguage</span>()</div>
<div className="block"><p>Gets a language of the venue model.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The language of the venue model.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometriesByName()">
<h3>getGeometriesByName</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span className="element-name">getGeometriesByName</span>()</div>
<div className="block"><p>Gets the geometries ordered by the name in an ascending order.</p></div>
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
<div className="block"><p>Gets geometries mapped by icon names.</p></div>
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
<div className="block"><p>Gets a list of topologies of the drawing.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of topologies of the drawing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometries()">
<h3>getGeometries</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-venue-data-venuegeometry" title="class in com.here.sdk.venue.data">VenueGeometry</a>&gt;</span> <span className="element-name">getGeometries</span>()</div>
<div className="block"><p>Gets a list of geometries of the venue.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
