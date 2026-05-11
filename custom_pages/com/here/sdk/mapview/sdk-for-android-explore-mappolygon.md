---
title: "MapPolygon (API Reference)"
slug: "sdk-for-android-explore-mappolygon"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapPolygon.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="../../../../index.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../../index-all.html">Index</a></li>
<li><a href="../../../../help-doc.html#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="../../NativeBase.html" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapPolygon</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapPolygon</span>
<span class="extends-implements">extends <a href="../../NativeBase.html" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A visual representation of a polygon on the map. Can be used to visualize areas of all shapes
 and sizes.
 <p>The geometry to be visualized is represented by an instance of <a href="../core/GeoPolygon.html" title="class in com.here.sdk.core"><code>GeoPolygon</code></a>.
 To display circular areas (for example, a position accuracy indicator) use a GeoPolygon
 created from a <a href="../core/GeoCircle.html" title="class in com.here.sdk.core"><code>GeoCircle</code></a> using <a href="../core/GeoPolygon.html#%3Cinit%3E(com.here.sdk.core.GeoBox)"><code>GeoPolygon(GeoCircle)</code></a>.
 <p>Note:
 <ul>
<li>The polygon shape should not cover more than half of the globe,
 otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
 artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul></p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color)">MapPolygon</a><wbr/>(<a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a> geometry,
 <a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> color)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color,com.here.sdk.core.Color,double)">MapPolygon</a><wbr/>(<a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a> geometry,
 <a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> color,
 <a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> outlineColor,
 double outlineWidthInPixels)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDrawOrder()">getDrawOrder</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the draw order of this map polygon relative to other map polygons.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Color.html" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFillColor()">getFillColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current color of the fill.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeometry()">getGeometry</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the current geometry of the polygon.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Metadata.html" title="class in com.here.sdk.core">Metadata</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getMetadata()">getMetadata</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the Metadata instance attached to this polygon.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="../core/Color.html" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutlineColor()">getOutlineColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the color of the polygon outline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutlineWidth()">getOutlineWidth</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the outline width of the polygon in pixels.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMeasureRange.html" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getVisibilityRanges()">getVisibilityRanges</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of visibility ranges.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setDrawOrder(int)">setDrawOrder</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the draw order of this map polygon relative to other map polygons.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setFillColor(com.here.sdk.core.Color)">setFillColor</a><wbr/>(<a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the current color of the fill.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGeometry(com.here.sdk.core.GeoPolygon)">setGeometry</a><wbr/>(<a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a new geometry to update the appearance.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setMetadata(com.here.sdk.core.Metadata)">setMetadata</a><wbr/>(<a href="../core/Metadata.html" title="class in com.here.sdk.core">Metadata</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the Metadata instance to be attached to this polygon.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOutlineColor(com.here.sdk.core.Color)">setOutlineColor</a><wbr/>(<a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the color of the polygon outline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setOutlineWidth(double)">setOutlineWidth</a><wbr/>(double value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the outline width of the polygon in pixels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setVisibilityRanges(java.util.List)">setVisibilityRanges</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMeasureRange.html" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets visibility ranges for this map polygon.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color)">
<h3>MapPolygon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapPolygon</span><wbr/><span class="parameters">(@NonNull
 <a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a> geometry,
 @NonNull
 <a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> color)</span></div>
<div class="block"><p>Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.
 <p>The winding order of the vertices can be in clockwise or counter-clockwise order.
 It is recomended to provide the outer boundary ordered clockwise and closed.
 <p>Note:
 <ul>
<li>The polygon shape should not cover more than half of the globe,
 otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
 artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometry</code> - <p>The list of vertices representing the outer boundary of polygon.</p></dd>
<dd><code>color</code> - <p>The fill color for the polygon</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color,com.here.sdk.core.Color,double)">
<h3>MapPolygon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapPolygon</span><wbr/><span class="parameters">(@NonNull
 <a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a> geometry,
 @NonNull
 <a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> color,
 @NonNull
 <a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> outlineColor,
 double outlineWidthInPixels)</span></div>
<div class="block"><p>Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.
 <p>Transparent outlines are not supported. Any color with transparency (alpha value other than 1)
 will be rendered as fully opaque by interpreting the alpha value as 1.
 <p>The winding order of the vertices can be in clockwise or counter-clockwise order.
 It is recomended to provide the outer boundary ordered clockwise and closed.
 <p>Note:
 <ul>
<li>The polygon shape should not cover more than half of the globe,
 otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
 artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul></p></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometry</code> - <p>The list of vertices representing the outer boundary of polygon.</p></dd>
<dd><code>color</code> - <p>The fill color for the polygon.</p></dd>
<dd><code>outlineColor</code> - <p>The color of the polygon outline, alpha channel is ignored and treated as 1.</p></dd>
<dd><code>outlineWidthInPixels</code> - <p>The width of the polygon outline (in pixels). Negative values are clamped to 0.</p></dd>
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
<section class="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a></span> <span class="element-name">getGeometry</span>()</div>
<div class="block"><p>Gets the current geometry of the polygon.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The geometry of the polygon. Setting a new geometry will update the appearance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGeometry(com.here.sdk.core.GeoPolygon)">
<h3>setGeometry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGeometry</span><wbr/><span class="parameters">(@NonNull
 <a href="../core/GeoPolygon.html" title="class in com.here.sdk.core">GeoPolygon</a> value)</span></div>
<div class="block"><p>Sets a new geometry to update the appearance.
 <p>The winding order of the vertices can be in clockwise or counter-clockwise order.
 It is recomended to provide the outer boundary ordered clockwise and closed.
 <p>Note:
 <ul>
<li>The polygon shape should not cover more than half of the globe,
 otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
 artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The geometry of the polygon. Setting a new geometry will update the appearance.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadata()">
<h3>getMetadata</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="../core/Metadata.html" title="class in com.here.sdk.core">Metadata</a></span> <span class="element-name">getMetadata</span>()</div>
<div class="block"><p>Gets the Metadata instance attached to this polygon.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The Metadata instance attached to this polygon, <code>null</code> by default.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMetadata(com.here.sdk.core.Metadata)">
<h3>setMetadata</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMetadata</span><wbr/><span class="parameters">(@Nullable
 <a href="../core/Metadata.html" title="class in com.here.sdk.core">Metadata</a> value)</span></div>
<div class="block"><p>Sets the Metadata instance to be attached to this polygon.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The Metadata instance attached to this polygon, <code>null</code> by default.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFillColor()">
<h3>getFillColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../core/Color.html" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getFillColor</span>()</div>
<div class="block"><p>Gets the current color of the fill.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Color of the polygon's fill.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setFillColor(com.here.sdk.core.Color)">
<h3>setFillColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFillColor</span><wbr/><span class="parameters">(@NonNull
 <a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div class="block"><p>Sets the current color of the fill.
 <p>Fully transparent color (alpha set to 0) disables the fill completely.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Color of the polygon's fill.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawOrder()">
<h3>getDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDrawOrder</span>()</div>
<div class="block"><p>Gets the draw order of this map polygon relative to other map polygons. Default value is 0.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The draw order of this map polygon relative to other map polygons.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDrawOrder(int)">
<h3>setDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrder</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>Sets the draw order of this map polygon relative to other map polygons.
 <p>Polygon with higher draw order value are drawn
 on top of polygons with lower draw order.
 <p>In case multiple polygons have the same draw order value
 then the order in which they were added to the scene matters. Last added polygon is drawn on top.
 <p>Allowed range is 0-1023. Values outside this range will be clamped.</p></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The draw order of this map polygon relative to other map polygons.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibilityRanges()">
<h3>getVisibilityRanges</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMeasureRange.html" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</span> <span class="element-name">getVisibilityRanges</span>()</div>
<div class="block"><p>Gets the list of visibility ranges. The map polygon is visible only inside these map measure
 ranges. When empty (the default), the map polygon is visible without map measure restrictions.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of visibility ranges. The map polygon is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisibilityRanges(java.util.List)">
<h3>setVisibilityRanges</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibilityRanges</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="MapMeasureRange.html" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</span></div>
<div class="block"><p>Sets visibility ranges for this map polygon. A range is half open -
 [minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.
 The map polygon is visible only inside these map measure ranges.
 <p>When empty (the default), the map polygon is visible without map measure restrictions.
 Only <code>MapMeasureRange</code>(s) of <a href="MapMeasure.Kind.html#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <code>MapMeasureRange</code>(s) of other unsupported types will be ignored.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The list of visibility ranges. The map polygon is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutlineColor()">
<h3>getOutlineColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="../core/Color.html" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getOutlineColor</span>()</div>
<div class="block"><p>Gets the color of the polygon outline. The default outline color is opaque white.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The color of the polygon outline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOutlineColor(com.here.sdk.core.Color)">
<h3>setOutlineColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOutlineColor</span><wbr/><span class="parameters">(@NonNull
 <a href="../core/Color.html" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div class="block"><p>Sets the color of the polygon outline.
 <p>Transparent outlines are not supported. Any color with transparency (alpha value other than 1)
 will be rendered as fully opaque.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The color of the polygon outline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutlineWidth()">
<h3>getOutlineWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOutlineWidth</span>()</div>
<div class="block"><p>Gets the outline width of the polygon in pixels.
 <p>By default, the outline width is set to zero.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The width of the polygon outline in pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setOutlineWidth(double)">
<h3>setOutlineWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOutlineWidth</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the outline width of the polygon in pixels.
 <p>The value should be greater than or equal to 0.
 Negative values are clamped to zero.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The width of the polygon outline in pixels.</p></dd>
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
</body>
</html>

</div>
`
}</HTMLBlock>
