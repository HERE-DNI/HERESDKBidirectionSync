---
title: "MapPolyline.DashRepresentation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappolyline-dashrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapPolyline.DashRepresentation.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance"><a href="sdk-for-android-explore-mapitemrepresentation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapItemRepresentation</a>
<div class="inheritance"><a href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapPolyline.Representation</a>
<div class="inheritance">com.here.sdk.mapview.MapPolyline.DashRepresentation</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">MapPolyline.DashRepresentation</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></span></div>
<div class="block"><p>Represents a dash pattern for map polyline where the dash can be rendered as a colored
 line and the gap can be either empty or colored.
 </p><p>The length of the dash and gap are set independently, allowing for patterns
 like <code>' — — — —'</code> (dash length = gap length) or <code>' ——— ——— ———'</code> (dash length != gap length).</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a href="sdk-for-android-explore-mappolyline.representation.instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationErrorCode</a>, <a href="sdk-for-android-explore-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color)">DashRepresentation</a><wbr/>(<a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> dashColor)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a representation for a dashed line.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.core.Color)">DashRepresentation</a><wbr/>(<a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> dashColor,
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> gapColor)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a representation for a dashed line with both dash and the gap being colored.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getDashColor()">getDashColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the color of the dashes of the polyline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getDashLength()">getDashLength</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the map measure dependent polyline dash length.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getGapColor()">getGapColor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the color for the gaps of the polyline.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getGapLength()">getGapLength</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the map measure dependent polyline gap length.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getLineWidth()">getLineWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the map measure dependent polyline width.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color)">
<h3>DashRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DashRepresentation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 @NonNull
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> dashColor)</span>
                   throws <span class="exceptions"><a href="sdk-for-android-explore-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div class="block"><p>Creates a representation for a dashed line. Gaps are not displayed.
 </p><p>At map measures smaller than the smallest map measure in the <code>lineWidth</code>,
 <code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
 and equal to the value given for the smallest map measure in the
 respective <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> object.
 </p><p>At map measures bigger than the biggest map measure in the <code>lineWidth</code>,
 <code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
 and equal to the value given for the biggest map measure in the
 respective <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> object.
 </p><p>At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.
 </p><p>For <a href="sdk-for-android-explore-mapmeasure.kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-explore-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 </p><p>For <a href="sdk-for-android-explore-rendersize.unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-explore-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 </p><p>All sizes must not be 0 (<a href="sdk-for-android-explore-mapmeasuredependentrendersize#sizes"><code>MapMeasureDependentRenderSize.sizes</code></a> with all values set to 0.0).</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>dashLength</code> - <p>The dash length of the polyline depending on the map measure.</p></dd>
<dd><code>gapLength</code> - <p>The gap length of the polyline depending on the map measure.</p></dd>
<dd><code>dashColor</code> - <p>The dash color of the polyline.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.core.Color)">
<h3>DashRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">DashRepresentation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 @NonNull
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> dashColor,
 @NonNull
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> gapColor)</span>
                   throws <span class="exceptions"><a href="sdk-for-android-explore-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div class="block"><p>Creates a representation for a dashed line with both dash and the gap being colored.
 </p><p>At map measures smaller than the smallest map measure in the <code>lineWidth</code>,
 <code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
 and equal to the value given for the smallest map measure in the
 respective <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> object.
 </p><p>At map measures bigger than the biggest map measure in the <code>lineWidth</code>,
 <code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
 and equal to the value given for the biggest map measure in the
 respective <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> object.
 </p><p>At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.
 </p><p>For <a href="sdk-for-android-explore-mapmeasure.kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-explore-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 </p><p>For <a href="sdk-for-android-explore-rendersize.unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-explore-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 </p><p>All sizes must not be 0 (<a href="sdk-for-android-explore-mapmeasuredependentrendersize#sizes"><code>MapMeasureDependentRenderSize.sizes</code></a> with all values set to 0.0).</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>dashLength</code> - <p>The dash length of the polyline depending on the map measure.</p></dd>
<dd><code>gapLength</code> - <p>The gap length of the polyline depending on the map measure.</p></dd>
<dd><code>dashColor</code> - <p>The color of the dashes.</p></dd>
<dd><code>gapColor</code> - <p>The color of the gaps.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span class="element-name">getLineWidth</span>()</div>
<div class="block"><p>Gets the map measure dependent polyline width.
 </p><p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>lineWidth</code>.
 </p><p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>lineWidth</code>.
 </p><p>At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The width of the polyline depending on the map measure.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDashLength()">
<h3>getDashLength</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span class="element-name">getDashLength</span>()</div>
<div class="block"><p>Gets the map measure dependent polyline dash length.
 </p><p>At map measures smaller than smallest map measure in the <code>dashLength</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>dashLength</code>.
 </p><p>At map measures bigger than biggest map measure in the <code>dashLength</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>dashLength</code>.
 </p><p>At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The dash length of the polyline depending on the map measure.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGapLength()">
<h3>getGapLength</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span class="element-name">getGapLength</span>()</div>
<div class="block"><p>Gets the map measure dependent polyline gap length.
 </p><p>At map measures smaller than smallest map measure in the <code>gapLength</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>gapLength</code>.
 </p><p>At map measures bigger than biggest map measure in the <code>gapLength</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>gapLength</code>.
 </p><p>At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The gap length of the polyline depending on the map measure.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDashColor()">
<h3>getDashColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getDashColor</span>()</div>
<div class="block"><p>Gets the color of the dashes of the polyline.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The color of the dashes of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGapColor()">
<h3>getGapColor</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getGapColor</span>()</div>
<div class="block"><p>Gets the color for the gaps of the polyline. Returns <code>null</code> if no
 color is used.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The color for the gaps of the polyline. The default value is <code>null</code> and
     no color is used.</p></dd>
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
