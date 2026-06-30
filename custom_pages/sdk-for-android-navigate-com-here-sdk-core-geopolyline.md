---
title: "GeoPolyline (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-geopolyline"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- GeoPolyline.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.GeoPolyline</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">GeoPolyline</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A list of geographic coordinates representing the vertices of a polyline.
 An instance of this class, initialized with appropriate vertices.
 Represents a <code>GeoPolyline</code> as a series of geographic coordinates.</p></div>
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
<div class="col-first even-row-color"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#vertices">vertices</a></code></div>
<div class="col-last even-row-color">
<div class="block">The list of vertices representing the polyline.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#%3Cinit%3E(com.here.sdk.core.GeoBox)">GeoPolyline</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs an instance of this class from <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#%3Cinit%3E(java.util.List)">GeoPolyline</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a GeoPolyline from the provided vertices.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#coordinatesAtOffsetInMeters(double,com.here.sdk.core.GeoPolylineDirection)">coordinatesAtOffsetInMeters</a><wbr/>(double offsetInMeters,
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolylinedirection" title="enum class in com.here.sdk.core">GeoPolylineDirection</a> direction)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the coordinates at the given distance along the polyline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#getNearestIndexTo(com.here.sdk.core.GeoCoordinates)">getNearestIndexTo</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> point)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the index of the nearest vertex to the given point.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-geopolyline#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
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
<section class="detail" id="vertices">
<h3>vertices</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</span> <span class="element-name">vertices</span></div>
<div class="block"><p>The list of vertices representing the polyline.</p></div>
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
<section class="detail" id="&lt;init&gt;(java.util.List)">
<h3>GeoPolyline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GeoPolyline</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices)</span>
            throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Constructs a GeoPolyline from the provided vertices.
 Throws an InstantiationError if the number of vertices is less than two.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vertices</code> - <p>List of vertices representing the polyline.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoBox)">
<h3>GeoPolyline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GeoPolyline</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div class="block"><p>Constructs an instance of this class from <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>A rectangle defined by the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> to be converted into <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a>.
     The corner coordinates of the <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> will define the points of the resulting <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a>.</p></dd>
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
<section class="detail" id="getNearestIndexTo(com.here.sdk.core.GeoCoordinates)">
<h3>getNearestIndexTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getNearestIndexTo</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> point)</span></div>
<div class="block"><p>Returns the index of the nearest vertex to the given point.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>point</code> - <p>Coordinates of the point.</p></dd>
<dt>Returns:</dt>
<dd><p>Index of the closest vertex of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="coordinatesAtOffsetInMeters(double,com.here.sdk.core.GeoPolylineDirection)">
<h3>coordinatesAtOffsetInMeters</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">coordinatesAtOffsetInMeters</span><wbr/><span class="parameters">(double offsetInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolylinedirection" title="enum class in com.here.sdk.core">GeoPolylineDirection</a> direction)</span></div>
<div class="block"><p>Returns the coordinates at the given distance along the polyline. When the polyline is
 traversed from the beginning, the distance is calculated from the start of the
 polyline; while a direction from the end indicates a distance from the last vertex.
 The offset is expected to be non-negative and smaller than the length of the polyline.
 When the offset is negative, the function returns the starting end point of the polyline,
 i.e. the first vertex in positive direction and the last vertex in the negative direction.
 Similarly, when the offset is larger than the length of the polyline, then the function
 returns the opposite end point of the polyline.
 The distance between two consecutive vertices is calculated using the
 <a href="sdk-for-android-navigate-geocoordinates#distanceTo(com.here.sdk.core.GeoCoordinates)"><code>GeoCoordinates.distanceTo(com.here.sdk.core.GeoCoordinates)</code></a> function. Therefore, it computes the distance (in meters) along
 the great circle between the two vertices. Similarly, the full length of the polyline is the
 sum of the distances between its vertices. The interpolation coordinates between two vertices
 is calculated using the <a href="sdk-for-android-navigate-geocoordinates#interpolate(com.here.sdk.core.GeoCoordinates,double)"><code>GeoCoordinates.interpolate(com.here.sdk.core.GeoCoordinates, double)</code></a> function.
 Note: the result may different from the analogue result from other matching components since
 they may adapt the result to the length of the underlying object described by the polyline.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>offsetInMeters</code> - <p>The distance along the polyline in meters</p></dd>
<dd><code>direction</code> - <p>The direction in which the polyline is traversed.</p></dd>
<dt>Returns:</dt>
<dd><p>The coordinates of the point at the given distance</p></dd>
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
