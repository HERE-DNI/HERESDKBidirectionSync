---
title: "MapPolyline (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappolyline"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapPolyline.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapPolyline</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapPolyline</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A visual representation of a line on the map.
 </p><p>The geometry to be visualized is represented by an instance of <a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a>.
 </p><p>Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mappolyline.dashimagerepresentation" title="class in com.here.sdk.mapview">MapPolyline.DashImageRepresentation</a></code></div>
<div class="col-last even-row-color">
<div class="block">Represents a dash pattern for the map polyline consisting of images rendered with certain gaps
 from each other.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mappolyline.dashrepresentation" title="class in com.here.sdk.mapview">MapPolyline.DashRepresentation</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Represents a dash pattern for map polyline where the dash can be rendered as a colored
 line and the gap can be either empty or colored.</div>
</div>
<div class="col-first even-row-color"><code>static class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></code></div>
<div class="col-last even-row-color">
<div class="block">Base class to represent the visual appearance of a <a href="sdk-for-android-explore-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a>.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mappolyline.solidmulticolorrepresentation" title="class in com.here.sdk.mapview">MapPolyline.SolidMultiColorRepresentation</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Representation allows map polyline to be colored in multiple specified color segments.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-mappolyline.solidrepresentation" title="class in com.here.sdk.mapview">MapPolyline.SolidRepresentation</a></code></div>
<div class="col-last even-row-color">
<div class="block">Representation for a solid line without outline.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.core.GeoPolyline,com.here.sdk.mapview.MapPolyline.Representation)">MapPolyline</a><wbr/>(<a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> geometry,
 <a href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a> representation)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new <code>MapPolyline</code> instance with a specified visual representation.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#cancelAnimation(com.here.sdk.animation.MapPolylineAnimation)">cancelAnimation</a><wbr/>(<a href="sdk-for-android-explore-mappolylineanimation" title="class in com.here.sdk.animation">MapPolylineAnimation</a> animation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Cancels single ongoing animation of this map polyline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getDrawOrder()">getDrawOrder</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the draw order of the polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getDrawOrderType()">getDrawOrderType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the draw order type of the polyline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getGeometry()">getGeometry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the geometry of the polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapcontentcategory" title="enum class in com.here.sdk.mapview">MapContentCategory</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getMapContentCategoriesToBlock()">getMapContentCategoriesToBlock</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets list of map content categories this polyline should block.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-metadata" title="class in com.here.sdk.core">Metadata</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getMetadata()">getMetadata</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <code>Metadata</code> instance attached to this polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getProgress()">getProgress</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the progress of the polyline, 0 by default.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getProgressColor()">getProgressColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the progress color of the polyline, opaque white by default.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getProgressGradientLength()">getProgressGradientLength</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getProgressOutlineColor()">getProgressOutlineColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the progress outline color of the polyline, opaque white by default.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getVisibilityRanges()">getVisibilityRanges</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of visibility ranges.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setDrawOrder(int)">setDrawOrder</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the draw order of the polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setDrawOrderType(com.here.sdk.mapview.DrawOrderType)">setDrawOrderType</a><wbr/>(<a href="sdk-for-android-explore-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the draw order type of the polyline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setGeometry(com.here.sdk.core.GeoPolyline)">setGeometry</a><wbr/>(<a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the geometry of the polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setMapContentCategoriesToBlock(java.util.List)">setMapContentCategoriesToBlock</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapcontentcategory" title="enum class in com.here.sdk.mapview">MapContentCategory</a>&gt; value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets list of map content categories this polyline should block.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setMetadata(com.here.sdk.core.Metadata)">setMetadata</a><wbr/>(<a href="sdk-for-android-explore-metadata" title="class in com.here.sdk.core">Metadata</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the <code>Metadata</code> instance attached to this polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setProgress(double)">setProgress</a><wbr/>(double value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the progress of the polyline from its starting point as a ratio of its total length
 clamped to the range [0; 1].</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setProgressColor(com.here.sdk.core.Color)">setProgressColor</a><wbr/>(<a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the progress color of the polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setProgressGradientLength(com.here.sdk.mapview.MapMeasureDependentRenderSize)">setProgressGradientLength</a><wbr/>(<a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setProgressOutlineColor(com.here.sdk.core.Color)">setProgressOutlineColor</a><wbr/>(<a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the progress outline color of the polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setRepresentation(com.here.sdk.mapview.MapPolyline.Representation)">setRepresentation</a><wbr/>(<a href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a> representation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Changes the appearance of the <code>MapPolyline</code> instance.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setVisibilityRanges(java.util.List)">setVisibilityRanges</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets visibility ranges for this map polyline.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#startAnimation(com.here.sdk.animation.MapPolylineAnimation,com.here.sdk.animation.AnimationListener)">startAnimation</a><wbr/>(<a href="sdk-for-android-explore-mappolylineanimation" title="class in com.here.sdk.animation">MapPolylineAnimation</a> animation,
 <a href="sdk-for-android-explore-animationlistener" title="interface in com.here.sdk.animation">AnimationListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts an animation of this map polyline.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoPolyline,com.here.sdk.mapview.MapPolyline.Representation)">
<h3>MapPolyline</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapPolyline</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> geometry,
 @NonNull
 <a href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a> representation)</span></div>
<div class="block"><p>Creates a new <code>MapPolyline</code> instance with a specified visual representation.
 </p><p>Altitude component of <code>GeoPolyline</code>'s vertices is ignored.
 </p><p>After creating a <code>MapPolyline</code> with this representation, the deprecated <code>MapPolyline</code>
 properties do not work and any change to them will be ignored. Any modifications to polyline's
 appearance must be done with <a href="sdk-for-android-explore-index#setRepresentation(com.here.sdk.mapview.MapPolyline.Representation)"><code>setRepresentation(com.here.sdk.mapview.MapPolyline.Representation)</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometry</code> - <p>The list of vertices representing the polyline.</p></dd>
<dd><code>representation</code> - <p>The styling properties of the polyline.</p></dd>
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
<section class="detail" id="setRepresentation(com.here.sdk.mapview.MapPolyline.Representation)">
<h3>setRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setRepresentation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a> representation)</span></div>
<div class="block"><p>Changes the appearance of the <code>MapPolyline</code> instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>representation</code> - <p>The representation describing a new appearance of the <code>MapPolyline</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="startAnimation(com.here.sdk.animation.MapPolylineAnimation,com.here.sdk.animation.AnimationListener)">
<h3>startAnimation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">startAnimation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mappolylineanimation" title="class in com.here.sdk.animation">MapPolylineAnimation</a> animation,
 @NonNull
 <a href="sdk-for-android-explore-animationlistener" title="interface in com.here.sdk.animation">AnimationListener</a> listener)</span></div>
<div class="block"><p>Starts an animation of this map polyline.
 </p><p>The <code>MapPolylineAnimation</code> may be shared between multiple instances of <code>MapPolyline</code>.
 </p><p>Starting animation on one polyline does not influence any ongoing animations on
 other polylines.
 Any ongoing animation of this map polyline will get cancelled.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>animation</code> - <p>The animation to start.</p></dd>
<dd><code>listener</code> - <p>The listener to receive notifications
     about animation start, completion or cancellation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="cancelAnimation(com.here.sdk.animation.MapPolylineAnimation)">
<h3>cancelAnimation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">cancelAnimation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mappolylineanimation" title="class in com.here.sdk.animation">MapPolylineAnimation</a> animation)</span></div>
<div class="block"><p>Cancels single ongoing animation of this map polyline.
 </p><p>Does nothing if the specified animation is not currently in progress for this polyline.
 Does not affect other polylines that might be running this animation.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>animation</code> - <p>The animation to cancel</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span class="element-name">getGeometry</span>()</div>
<div class="block"><p>Gets the geometry of the polyline.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of vertices that represent the geometry of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGeometry(com.here.sdk.core.GeoPolyline)">
<h3>setGeometry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGeometry</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> value)</span></div>
<div class="block"><p>Sets the geometry of the polyline. Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The list of vertices that represent the geometry of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMetadata()">
<h3>getMetadata</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-metadata" title="class in com.here.sdk.core">Metadata</a></span> <span class="element-name">getMetadata</span>()</div>
<div class="block"><p>Gets the <code>Metadata</code> instance attached to this polyline.
 This will be <code>null</code> if nothing has been attached before.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <code>Metadata</code> instance attached to this polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMetadata(com.here.sdk.core.Metadata)">
<h3>setMetadata</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMetadata</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-metadata" title="class in com.here.sdk.core">Metadata</a> value)</span></div>
<div class="block"><p>Sets the <code>Metadata</code> instance attached to this polyline.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The <code>Metadata</code> instance attached to this polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawOrder()">
<h3>getDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDrawOrder</span>()</div>
<div class="block"><p>Gets the draw order of the polyline.
 </p><p>The default draw order is 0.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The draw order of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDrawOrder(int)">
<h3>setDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrder</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>Sets the draw order of the polyline.
 </p><p>Polylines with a higher draw order are drawn on top
 of polylines with a lower draw order.
 </p><p>In case multiple polylines have the same draw
 order, they can be rendered in different ways depending on the <a href="sdk-for-android-explore-index#getDrawOrderType()"><code>getDrawOrderType()</code></a> set.
 </p><p>Supplied value is clamped to the range [0; 1023].</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The draw order of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawOrderType()">
<h3>getDrawOrderType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a></span> <span class="element-name">getDrawOrderType</span>()</div>
<div class="block"><p>Gets the draw order type of the polyline.
 </p><p>The default value is <a href="sdk-for-android-explore-drawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The draw order type of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDrawOrderType(com.here.sdk.mapview.DrawOrderType)">
<h3>setDrawOrderType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrderType</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a> value)</span></div>
<div class="block"><p>Sets the draw order type of the polyline.
 </p><p>For <a href="sdk-for-android-explore-drawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT</code></a>, map polylines with outlines having
 the same draw order are drawn as a whole in the order of addition to a map scene. There
 is no possibility that parts of another polyline, regardless of its draw order value,
 are drawn between outline and mainline of another polyline.
 </p><p>With <a href="sdk-for-android-explore-drawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT</code></a>, polylines are rendered one by one.
 </p><p>For <a href="sdk-for-android-explore-drawordertype#MAP_SCENE_ADDITION_ORDER_INDEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_INDEPENDENT</code></a>, for multiple polylines with
 outlines having the same draw order, all outlines are rendered first in an arbitrary order
 and then all mainlines are drawn on top of those polylines in an arbitrary order.
 </p><p><a href="sdk-for-android-explore-drawordertype#MAP_SCENE_ADDITION_ORDER_INDEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_INDEPENDENT</code></a> allows speeding up the rendering
 process and keeping high frame rates when many similar polylines (with same styling
 attributes and <a href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview"><code>MapPolyline.Representation</code></a>) are present in a map scene.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The draw order type of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getVisibilityRanges()">
<h3>getVisibilityRanges</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</span> <span class="element-name">getVisibilityRanges</span>()</div>
<div class="block"><p>Gets the list of visibility ranges. The map polyline is visible only inside these map measure
 ranges. When empty (the default), the map polyline is visible without map measure restrictions.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of visibility ranges. The map polyline is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setVisibilityRanges(java.util.List)">
<h3>setVisibilityRanges</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibilityRanges</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</span></div>
<div class="block"><p>Sets visibility ranges for this map polyline. A range is half open -
 [minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.
 The map polyline is visible only inside these map measure ranges.
 </p><p>When empty (the default), the map polyline is visible without map measure restrictions.
 Only <code>MapMeasureRange</code>(s) of <a href="sdk-for-android-explore-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <code>MapMeasureRange</code>(s) of other unsupported types will be ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The list of visibility ranges. The map polyline is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProgress()">
<h3>getProgress</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getProgress</span>()</div>
<div class="block"><p>Gets the progress of the polyline, 0 by default.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The progress from the polyline's starting point, as a ratio of its total length clamped to
     the range [0, 1].</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProgress(double)">
<h3>setProgress</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProgress</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>Sets the progress of the polyline from its starting point as a ratio of its total length
 clamped to the range [0; 1].
 </p><p>As the progress varies, the equivalent part of the
 polyline gets covered by the progress color and progress outline color. The rest of the
 polyline until its end point retains the line color and outline color along with an
 optional dash pattern.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The progress from the polyline's starting point, as a ratio of its total length clamped to
     the range [0, 1].</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProgressColor()">
<h3>getProgressColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getProgressColor</span>()</div>
<div class="block"><p>Gets the progress color of the polyline, opaque white by default.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The color used for the progress part of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProgressColor(com.here.sdk.core.Color)">
<h3>setProgressColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProgressColor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div class="block"><p>Sets the progress color of the polyline.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The color used for the progress part of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProgressOutlineColor()">
<h3>getProgressOutlineColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getProgressOutlineColor</span>()</div>
<div class="block"><p>Gets the progress outline color of the polyline, opaque white by default.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The color used for outline of the progress part of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProgressOutlineColor(com.here.sdk.core.Color)">
<h3>setProgressOutlineColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProgressOutlineColor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div class="block"><p>Sets the progress outline color of the polyline.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The color used for outline of the progress part of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getProgressGradientLength()">
<h3>getProgressGradientLength</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span class="element-name">getProgressGradientLength</span>()</div>
<div class="block"><p>Gets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setProgressGradientLength(com.here.sdk.mapview.MapMeasureDependentRenderSize)">
<h3>setProgressGradientLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setProgressGradientLength</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> value)</span></div>
<div class="block"><p>Sets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.
 To achieve a constant gradient length, use <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a>
 with a single value. To achieve a gradient length dependent on map zoom,
 use <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> with multiple values. The default value is a constant
 gradient length of zero pixels. The gradient is guaranteed to fit into polyline, i.e. the
 actual gradient can be shorter then <code>progressGradientLength</code>.
 </p><p>For <a href="sdk-for-android-explore-mapmeasure.kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-explore-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 For <a href="sdk-for-android-explore-rendersize.unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-explore-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 A parameter with unsupported values is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMapContentCategoriesToBlock()">
<h3>getMapContentCategoriesToBlock</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapcontentcategory" title="enum class in com.here.sdk.mapview">MapContentCategory</a>&gt;</span> <span class="element-name">getMapContentCategoriesToBlock</span>()</div>
<div class="block"><p>Gets list of map content categories this polyline should block.
 </p><p>Default value is an empty list meaning none of the map categories will be blocked.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>List of map content categories this polyline should block.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMapContentCategoriesToBlock(java.util.List)">
<h3>setMapContentCategoriesToBlock</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMapContentCategoriesToBlock</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-mapcontentcategory" title="enum class in com.here.sdk.mapview">MapContentCategory</a>&gt; value)</span></div>
<div class="block"><p>Sets list of map content categories this polyline should block.
 </p><p>Map content categories overlapping the polyline geometry
 (progress and non-progress) will be discarded from being rendered.
 </p><p>Duplicate entries will be ignored and will have no additional effect.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>List of map content categories this polyline should block.</p></dd>
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
