---
title: "MapPolyline.SolidRepresentation (API Reference)"
slug: "sdk-for-android-navigate-mappolyline-solidrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapPolyline.SolidRepresentation.html -->
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
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li><a href="#nested-class-summary">Nested</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance"><a href="sdk-for-android-navigate-mapitemrepresentation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapItemRepresentation</a>
<div class="inheritance"><a href="sdk-for-android-navigate-mappolyline.representation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapPolyline.Representation</a>
<div class="inheritance">com.here.sdk.mapview.MapPolyline.SolidRepresentation</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">MapPolyline.SolidRepresentation</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-mappolyline.representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></span></div>
<div class="block"><p>Representation for a solid line without outline.
 <p>Can represent polylines that have constant width or width dependent on the map zoom.
 <p>To achieve constant width lines, use <a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> with a single value.
 <p>To achieve line width dependent on map zoom, use <a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> with
 multiple values.
 <p>For <a href="sdk-for-android-navigate-mapmeasure.kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-navigate-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 <p>For <a href="sdk-for-android-navigate-rendersize.unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-navigate-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.</p></p></p></p></p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a href="sdk-for-android-navigate-mappolyline.representation.instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationErrorCode</a>, <a href="sdk-for-android-navigate-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)">SolidRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a> color,
 <a href="sdk-for-android-navigate-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a representation for a solid line without outline.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)">SolidRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a> color,
 <a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> outlineWidth,
 <a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 <a href="sdk-for-android-navigate-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a representation for a solid line with outline.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-linecap" title="enum class in com.here.sdk.mapview">LineCap</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCapShape()">getCapShape</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns the cap shape of the polyline and its outline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLineColor()">getLineColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the color of the polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLineWidth()">getLineWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the map measure dependent polyline width.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutlineColor()">getOutlineColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the color of outline of the polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getOutlineWidth()">getOutlineWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the map measure dependent polyline outline width.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)">
<h3>SolidRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SolidRepresentation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a> color,
 @NonNull
 <a href="sdk-for-android-navigate-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape)</span>
                    throws <span class="exceptions"><a href="sdk-for-android-navigate-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div class="block"><p>Creates a representation for a solid line without outline.
 <p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>lineWidth</code>.
 <p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>lineWidth</code>.
 <p>At map measures between two nearest given map measures line width is
 linearly interpolated between width values given for these map measures.
 <p>For <a href="sdk-for-android-navigate-mapmeasure.kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-navigate-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 <p>For <a href="sdk-for-android-navigate-rendersize.unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-navigate-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 <p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p></p></p></p></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>color</code> - <p>The color of the polyline.</p></dd>
<dd><code>capShape</code> - <p>The cap shape applied to both ends of the polyline.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)">
<h3>SolidRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SolidRepresentation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a> color,
 @NonNull
 <a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> outlineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 @NonNull
 <a href="sdk-for-android-navigate-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape)</span>
                    throws <span class="exceptions"><a href="sdk-for-android-navigate-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div class="block"><p>Creates a representation for a solid line with outline.
 <p>The total width of the polyline is <code>line width + 2 * outline width</code>.
 <p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
 and <code>outlineWidth</code>, the value is constant and equal to the width given for
 the smallest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.
 <p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
 and <code>outlineWidth</code>, the value is constant and equal to the width given for
 the biggest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.
 <p>At map measures between two nearest given map measure is
 linearly interpolated between width values given for these map measures.
 <p>For <a href="sdk-for-android-navigate-mapmeasure.kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-navigate-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 <p>For <a href="sdk-for-android-navigate-rendersize.unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-navigate-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 <p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p></p></p></p></p></p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>color</code> - <p>The color of the polyline.</p></dd>
<dd><code>outlineWidth</code> - <p>The width of the outline on one side of the polyline depending on
     the map measure.</p></dd>
<dd><code>outlineColor</code> - <p>The outline color of the polyline.</p></dd>
<dd><code>capShape</code> - <p>The cap shape applied to both ends of the polyline.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
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
<section class="detail" id="getLineWidth()">
<h3>getLineWidth</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span class="element-name">getLineWidth</span>()</div>
<div class="block"><p>Gets the map measure dependent polyline width.
 <p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>lineWidth</code>.
 <p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>lineWidth</code>.
 <p>At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.</p></p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The width of the polyline depending on the map measure.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLineColor()">
<h3>getLineColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getLineColor</span>()</div>
<div class="block"><p>Gets the color of the polyline.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The color of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutlineWidth()">
<h3>getOutlineWidth</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span class="element-name">getOutlineWidth</span>()</div>
<div class="block"><p>Gets the map measure dependent polyline outline width.
 <p>The total width of the polyline is <code>line width + 2 * outline width</code>.
 <p>At map measures smaller than smallest map measure in the <code>outlineWidth</code>,
 outline width is constant and equal to the width given for the smallest
 map measure in the <code>outlineWidth</code>.
 <p>At map measures bigger than biggest map measure in the <code>outlineWidth</code>,
 outline width is constant and equal to the width given for the biggest
 map measure in the <code>outlineWidth</code>.
 <p>At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.</p></p></p></p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The width of the outline on one side of the polyline depending on the map measure.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getOutlineColor()">
<h3>getOutlineColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getOutlineColor</span>()</div>
<div class="block"><p>Gets the color of outline of the polyline.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The outline color of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCapShape()">
<h3>getCapShape</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-linecap" title="enum class in com.here.sdk.mapview">LineCap</a></span> <span class="element-name">getCapShape</span>()</div>
<div class="block"><p>Returns the cap shape of the polyline and its outline.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The cap shape applied to both ends of the polyline and its outline.</p></dd>
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
