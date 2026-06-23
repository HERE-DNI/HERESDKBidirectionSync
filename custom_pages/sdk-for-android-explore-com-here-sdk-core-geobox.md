---
title: "GeoBox (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-geobox"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- GeoBox.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.GeoBox</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">GeoBox</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents a bounding rectangle aligned with latitude and longitude.
 Geographic area represented by this would be visualised as a rectangle
 when using a normal cylindrical projection (such as Mercator).
 The box has a maximum span of 360 degrees in longitude and 180 degrees in latitude direction.
 The box with equal values in longitude for the corners is considered as a span of 360 degrees.
 The box is considered empty if the latitude of the <a href="sdk-for-android-explore-index#southWestCorner"><code>southWestCorner</code></a> is larger than the the
 latitude of the <a href="sdk-for-android-explore-index#northEastCorner"><code>northEastCorner</code></a>.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>final <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#northEastCorner">northEastCorner</a></code></div>
<div class="col-last even-row-color">
<div class="block">North east corner coordinates.</div>
</div>
<div class="col-first odd-row-color"><code>final <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#southWestCorner">southWestCorner</a></code></div>
<div class="col-last odd-row-color">
<div class="block">South west corner coordinates.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates)">GeoBox</a><wbr/>(<a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> southWestCorner,
 <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> northEastCorner)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#containing(java.util.List)">containing</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; geoCoordinates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a <code>GeoBox</code> which encompases all coordinates from the list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#contains(com.here.sdk.core.GeoBox)">contains</a><wbr/>(<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether the specified <code>GeoBox</code> is covered entirely by this <code>GeoBox</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#contains(com.here.sdk.core.GeoCoordinates)">contains</a><wbr/>(<a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether the specified GeoCoordinates is contained within this <code>GeoBox</code>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#envelope(com.here.sdk.core.GeoBox)">envelope</a><wbr/>(<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Envelopes two <code>GeoBox</code> areas by returning the smallest <code>GeoBox</code> covering both this
 GeoBox and the specified <code>GeoBox</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#envelopeGeoBoxes(java.util.List)">envelopeGeoBoxes</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt; geoBoxes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Envelopes the list of <code>GeoBox</code> areas by returning the smallest
 <code>GeoBox</code> covering all specified <code>GeoBox</code> objects.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#expandedBy(double,double,double,double)">expandedBy</a><wbr/>(double southMeters,
 double westMeters,
 double northMeters,
 double eastMeters)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates a <code>GeoBox</code> which is expanded by a fixed distance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#hashCode()">hashCode</a>()</code></div>

<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#intersection(com.here.sdk.core.GeoBox)">intersection</a><wbr/>(<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Computes the intersection with the passed <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#intersection(java.util.List)">intersection</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt; geoBoxes)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Computes intersection of list of <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> instances.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#intersects(com.here.sdk.core.GeoBox)">intersects</a><wbr/>(<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Determines whether this <code>GeoBox</code> intersects with the passed <code>GeoBox</code>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="southWestCorner">
<h3>southWestCorner</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">southWestCorner</span></div>
<div class="block"><p>South west corner coordinates.</p></div>
</section>
</li>
<li>
<section class="detail" id="northEastCorner">
<h3>northEastCorner</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">northEastCorner</span></div>
<div class="block"><p>North east corner coordinates.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCoordinates)">
<h3>GeoBox</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GeoBox</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> southWestCorner,
 @NonNull
 <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> northEastCorner)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="containing(java.util.List)">
<h3>containing</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">containing</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; geoCoordinates)</span></div>
<div class="block"><p>Creates a <code>GeoBox</code> which encompases all coordinates from the list.
 The provided list must contain at least two points.
 The altitude values of the input coordinates are not considered for the result.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoCoordinates</code> - <p>List of coordinates to encompass inside bounding box.</p></dd>
<dt>Returns:</dt>
<dd><p><code>GeoBox</code> containing all supplied coordinates, or <code>null</code> if less than two coordinates were provided.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="envelope(com.here.sdk.core.GeoBox)">
<h3>envelope</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">envelope</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div class="block"><p>Envelopes two <code>GeoBox</code> areas by returning the smallest <code>GeoBox</code> covering both this
 GeoBox and the specified <code>GeoBox</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>Another <code>GeoBox</code> to envelope with.</p></dd>
<dt>Returns:</dt>
<dd><p><code>GeoBox</code> covering two<code>GeoBox</code> areas</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="envelopeGeoBoxes(java.util.List)">
<h3>envelopeGeoBoxes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">envelopeGeoBoxes</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt; geoBoxes)</span></div>
<div class="block"><p>Envelopes the list of <code>GeoBox</code> areas by returning the smallest
 <code>GeoBox</code> covering all specified <code>GeoBox</code> objects.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoBoxes</code> - <p>List of <code>GeoBox</code> objects.</p></dd>
<dt>Returns:</dt>
<dd><p><code>GeoBox</code> covering all <code>GeoBox</code> areas, or <code>null</code>
     if input is empty.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersects(com.here.sdk.core.GeoBox)">
<h3>intersects</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">intersects</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div class="block"><p>Determines whether this <code>GeoBox</code> intersects with the passed <code>GeoBox</code>.
 The altitude values are ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>A <code>GeoBox</code> to check for intersection.</p></dd>
<dt>Returns:</dt>
<dd><p><code>true</code> if intersects with the <code>GeoBox</code>, <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersection(com.here.sdk.core.GeoBox)">
<h3>intersection</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt;</span> <span class="element-name">intersection</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div class="block"><p>Computes the intersection with the passed <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.
 The altitude values are ignored.
 Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>Another geo box to check intersection with.</p></dd>
<dt>Returns:</dt>
<dd><p>It will be empty if there is no overlap.
     Otherwise, 1 or more geo boxes covering common area by this and passed <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="intersection(java.util.List)">
<h3>intersection</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt;</span> <span class="element-name">intersection</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a>&gt; geoBoxes)</span></div>
<div class="block"><p>Computes intersection of list of <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> instances.
 The altitude values are ignored.
 Limitation: Geo boxes are considered as non-intersecting if they overlap only on a single point, horizontal line or vertical line.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoBoxes</code> - <p>List of <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> instances.</p></dd>
<dt>Returns:</dt>
<dd><p>It will be empty if there is no overlap between all the passed <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> instances.
     Otherwise, 1 or more geo boxes covering common area by all the passed <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> instances.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contains(com.here.sdk.core.GeoBox)">
<h3>contains</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div class="block"><p>Determines whether the specified <code>GeoBox</code> is covered entirely by this <code>GeoBox</code>.
 The altitude values are ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>A <code>GeoBox</code> to check for containment within this <code>GeoBox</code>.</p></dd>
<dt>Returns:</dt>
<dd><p><code>true</code> if covered by the <code>GeoBox</code>, <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="contains(com.here.sdk.core.GeoCoordinates)">
<h3>contains</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">contains</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> geoCoordinates)</span></div>
<div class="block"><p>Determines whether the specified GeoCoordinates is contained within this <code>GeoBox</code>.
 The altitude values are ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoCoordinates</code> - <p>A GeoCoordinates to check for containment within this <code>GeoBox</code>.</p></dd>
<dt>Returns:</dt>
<dd><p><code>true</code> if contained within the <code>GeoBox</code>, <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="expandedBy(double,double,double,double)">
<h3>expandedBy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">expandedBy</span><wbr/><span class="parameters">(double southMeters,
 double westMeters,
 double northMeters,
 double eastMeters)</span>
                  throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a <code>GeoBox</code> which is expanded by a fixed distance.
 Throws an InstantiationError if it is not possible to create a valid
 <code>GeoBox</code> with the given arguments.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>southMeters</code> - <p>Distance in the south direction in meters to expand the <code>GeoBox</code>.</p></dd>
<dd><code>westMeters</code> - <p>Distance in the west direction in meters to expand the <code>GeoBox</code>.</p></dd>
<dd><code>northMeters</code> - <p>Distance in the north direction in meters to expand the <code>GeoBox</code>.</p></dd>
<dd><code>eastMeters</code> - <p>Distance in the east direction in meters to expand the <code>GeoBox</code>.</p></dd>
<dt>Returns:</dt>
<dd><p>The expanded <code>GeoBox</code>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
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
