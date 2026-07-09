---
title: "GeoBox (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-geobox"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- GeoBox.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.core.GeoBox</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">GeoBox</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a bounding rectangle aligned with latitude and longitude.
 Geographic area represented by this would be visualised as a rectangle
 when using a normal cylindrical projection (such as Mercator).
 The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction.
 The box with equal values in longitude for the corners is considered as a span of 360 degrees.
 The box is considered empty if the latitude of the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox#southWestCorner"><code>southWestCorner</code></a> is larger than the the
 latitude of the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox#northEastCorner"><code>northEastCorner</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geobox#northEastCorner">northEastCorner</a></code></div>
<div className="col-last even-row-color">
<div className="block">North east corner coordinates.</div>
</div>
<div className="col-first odd-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geobox#southWestCorner">southWestCorner</a></code></div>
<div className="col-last odd-row-color">
<div className="block">South west corner coordinates.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geobox#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates)">GeoBox</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> southWestCorner,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> northEastCorner)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="southWestCorner">
<h3>southWestCorner</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">southWestCorner</span></div>
<div className="block"><p>South west corner coordinates.</p></div>
</section>
</li>
<li>
<section className="detail" id="northEastCorner">
<h3>northEastCorner</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span className="element-name">northEastCorner</span></div>
<div className="block"><p>North east corner coordinates.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates)">
<h3>GeoBox</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">GeoBox</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> southWestCorner,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> northEastCorner)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>southWestCorner</code> - <p>South west corner coordinates.</p></dd>
<dd><code>northEastCorner</code> - <p>North east corner coordinates.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="containing(java.util.List)">
<h3>containing</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">containing</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; geoCoordinates)</span></div>
<div className="block"><p>Creates a <code>GeoBox</code> which encompases all coordinates from the list.
 The provided list must contain at least two points.
 The altitude values of the input coordinates are not considered for the result.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoCoordinates</code> - <p>List of coordinates to encompass inside bounding box.</p></dd>
<dt>Returns:</dt>
<dd><p><code>GeoBox</code> containing all supplied coordinates, or <code>null</code> if less than two coordinates were provided.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="envelope(com.here.sdk.core.GeoBox)">
<h3>envelope</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">envelope</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div className="block"><p>Envelopes two <code>GeoBox</code> areas by returning the smallest <code>GeoBox</code> covering both this
 GeoBox and the specified <code>GeoBox</code>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>Another <code>GeoBox</code> to envelope with.</p></dd>
<dt>Returns:</dt>
<dd><p><code>GeoBox</code> covering two<code>GeoBox</code> areas</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="envelopeGeoBoxes(java.util.List)">
<h3>envelopeGeoBoxes</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">envelopeGeoBoxes</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt; geoBoxes)</span></div>
<div className="block"><p>Envelopes the list of <code>GeoBox</code> areas by returning the smallest
 <code>GeoBox</code> covering all specified <code>GeoBox</code> objects.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoBoxes</code> - <p>List of <code>GeoBox</code> objects.</p></dd>
<dt>Returns:</dt>
<dd><p><code>GeoBox</code> covering all <code>GeoBox</code> areas, or <code>null</code>
     if input is empty.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="intersects(com.here.sdk.core.GeoBox)">
<h3>intersects</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">intersects</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div className="block"><p>Determines whether this <code>GeoBox</code> intersects with the passed <code>GeoBox</code>.
 The altitude values are ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>A <code>GeoBox</code> to check for intersection.</p></dd>
<dt>Returns:</dt>
<dd><p><code>true</code> if intersects with the <code>GeoBox</code>, <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="intersection(com.here.sdk.core.GeoBox)">
<h3>intersection</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt;</span> <span className="element-name">intersection</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div className="block"><p>Computes the intersection with the passed <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.
 The altitude values are ignored.
 Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>Another geo box to check intersection with.</p></dd>
<dt>Returns:</dt>
<dd><p>It will be empty if there is no overlap.
     Otherwise, 1 or more geo boxes covering common area by this and passed <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="intersection(java.util.List)">
<h3>intersection</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public static</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt;</span> <span className="element-name">intersection</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt; geoBoxes)</span></div>
<div className="block"><p>Computes intersection of list of <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> instances.
 The altitude values are ignored.
 Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoBoxes</code> - <p>List of <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> instances.</p></dd>
<dt>Returns:</dt>
<dd><p>It will be empty if there is no overlap between all the passed <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> instances.
     Otherwise, 1 or more geo boxes covering common area by all the passed <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> instances.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="contains(com.here.sdk.core.GeoBox)">
<h3>contains</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">contains</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div className="block"><p>Determines whether the specified <code>GeoBox</code> is covered entirely by this <code>GeoBox</code>.
 The altitude values are ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>A <code>GeoBox</code> to check for containment within this <code>GeoBox</code>.</p></dd>
<dt>Returns:</dt>
<dd><p><code>true</code> if covered by the <code>GeoBox</code>, <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="contains(com.here.sdk.core.GeoCoordinates)">
<h3>contains</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">contains</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</span></div>
<div className="block"><p>Determines whether the specified GeoCoordinates is contained within this <code>GeoBox</code>.
 The altitude values are ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geoCoordinates</code> - <p>A GeoCoordinates to check for containment within this <code>GeoBox</code>.</p></dd>
<dt>Returns:</dt>
<dd><p><code>true</code> if contained within the <code>GeoBox</code>, <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="expandedBy(double,double,double,double)">
<h3>expandedBy</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span className="element-name">expandedBy</span><wbr/><span className="parameters">(double southMeters,
 double westMeters,
 double northMeters,
 double eastMeters)</span>
                  throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a <code>GeoBox</code> which is expanded by a fixed distance.
 Throws an InstantiationError if it is not possible to create a valid
 <code>GeoBox</code> with the given arguments.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>southMeters</code> - <p>Distance in the south direction in meters to expand the <code>GeoBox</code>.</p></dd>
<dd><code>westMeters</code> - <p>Distance in the west direction in meters to expand the <code>GeoBox</code>.</p></dd>
<dd><code>northMeters</code> - <p>Distance in the north direction in meters to expand the <code>GeoBox</code>.</p></dd>
<dd><code>eastMeters</code> - <p>Distance in the east direction in meters to expand the <code>GeoBox</code>.</p></dd>
<dt>Returns:</dt>
<dd><p>The expanded <code>GeoBox</code>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
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
