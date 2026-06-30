---
title: "GeoPolygon (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-geopolygon"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- GeoPolygon.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.GeoPolygon</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">GeoPolygon</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents a <code>GeoPolygon</code> area as a series of geographic coordinates, and optionally,
 a list of inner boundaries (also known as holes).
 An instance of this class, initialized with appropriate vertices.</p></div>
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
<div class="col-first even-row-color"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-geopolygon#innerBoundaries">innerBoundaries</a></code></div>
<div class="col-last even-row-color">
<div class="block">The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.</div>
</div>
<div class="col-first odd-row-color"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-geopolygon#vertices">vertices</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The list of geographic coordinates representing the outer boundary vertices of polygon.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-geopolygon#%3Cinit%3E(com.here.sdk.core.GeoBox)">GeoPolygon</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs an instance of this class from <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-geopolygon#%3Cinit%3E(com.here.sdk.core.GeoCircle)">GeoPolygon</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> geoCircle)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs an instance of this class from <a href="sdk-for-android-explore-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a>.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-geopolygon#%3Cinit%3E(java.util.List)">GeoPolygon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs an instance of this class from the provided vertices.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-geopolygon#%3Cinit%3E(java.util.List,java.util.List)">GeoPolygon</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;&gt; innerBoundaries)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs an instance of this class from the provided vertices and inner boundaries (holes).</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-geopolygon#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-geopolygon#hashCode()">hashCode</a>()</code></div>

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
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;</span> <span class="element-name">vertices</span></div>
<div class="block"><p>The list of geographic coordinates representing the outer boundary vertices of polygon.</p></div>
</section>
</li>
<li>
<section class="detail" id="innerBoundaries">
<h3>innerBoundaries</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;&gt;</span> <span class="element-name">innerBoundaries</span></div>
<div class="block"><p>The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.</p></div>
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
<h3>GeoPolygon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices)</span>
           throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Constructs an instance of this class from the provided vertices.
 Throws InstantiationError if the number of vertices is less than three.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vertices</code> - <p>List of vertices representing the polygon outer boundary in clockwise order.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List)">
<h3>GeoPolygon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt; vertices,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a>&gt;&gt; innerBoundaries)</span>
           throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Constructs an instance of this class from the provided vertices and inner boundaries (holes).
 Throws InstantiationError if the number of vertices is less than three.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>vertices</code> - <p>List of vertices representing the polygon outer boundary in clockwise order.</p></dd>
<dd><code>innerBoundaries</code> - <p>List of polygon inner boundaries (holes), each in counterclockwise order.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Instantiation error.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCircle)">
<h3>GeoPolygon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> geoCircle)</span></div>
<div class="block"><p>Constructs an instance of this class from <a href="sdk-for-android-explore-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoCircle</code> - <p>A <a href="sdk-for-android-explore-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a> to be converted into <a href="sdk-for-android-explore-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core"><code>GeoPolygon</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoBox)">
<h3>GeoPolygon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> geoBox)</span></div>
<div class="block"><p>Constructs an instance of this class from <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geoBox</code> - <p>A rectangle defined by the <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> to be converted into <a href="sdk-for-android-explore-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core"><code>GeoPolygon</code></a>.
     The corner coordinates defined by the <a href="sdk-for-android-explore-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a> will define the outer boundary verticies of the <a href="sdk-for-android-explore-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core"><code>GeoPolygon</code></a>.</p></dd>
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
