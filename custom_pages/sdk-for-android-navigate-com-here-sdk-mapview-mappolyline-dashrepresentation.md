---
title: "MapPolyline.DashRepresentation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashrepresentation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapPolyline.DashRepresentation.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapitemrepresentation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapItemRepresentation</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapPolyline.Representation</a>
<div className="inheritance">com.here.sdk.mapview.MapPolyline.DashRepresentation</div>
</div>
</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">MapPolyline.DashRepresentation</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></span></div>
<div className="block"><p>Represents a dash pattern for map polyline where the dash can be rendered as a colored
 line and the gap can be either empty or colored.
 The length of the dash and gap are set independently, allowing for patterns
 like <code>' — — — —'</code> (dash length = gap length) or <code>' ——— ——— ———'</code> (dash length != gap length).</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="inherited-list">

<code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationErrorCode</a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code></div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashrepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color)">DashRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> dashColor)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a representation for a dashed line.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashrepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.core.Color)">DashRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> dashColor,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> gapColor)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a representation for a dashed line with both dash and the gap being colored.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color)">
<h3>DashRepresentation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DashRepresentation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> dashColor)</span>
                   throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div className="block"><p>Creates a representation for a dashed line. Gaps are not displayed.
 At map measures smaller than the smallest map measure in the <code>lineWidth</code>,
 <code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
 and equal to the value given for the smallest map measure in the
 respective <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> object.
 At map measures bigger than the biggest map measure in the <code>lineWidth</code>,
 <code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
 and equal to the value given for the biggest map measure in the
 respective <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> object.
 At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 All sizes must not be 0 (<a href="sdk-for-android-navigate-mapmeasuredependentrendersize#sizes"><code>MapMeasureDependentRenderSize.sizes</code></a> with all values set to 0.0).</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>dashLength</code> - <p>The dash length of the polyline depending on the map measure.</p></dd>
<dd><code>gapLength</code> - <p>The gap length of the polyline depending on the map measure.</p></dd>
<dd><code>dashColor</code> - <p>The dash color of the polyline.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.core.Color)">
<h3>DashRepresentation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DashRepresentation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> dashColor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> gapColor)</span>
                   throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div className="block"><p>Creates a representation for a dashed line with both dash and the gap being colored.
 At map measures smaller than the smallest map measure in the <code>lineWidth</code>,
 <code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
 and equal to the value given for the smallest map measure in the
 respective <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> object.
 At map measures bigger than the biggest map measure in the <code>lineWidth</code>,
 <code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
 and equal to the value given for the biggest map measure in the
 respective <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> object.
 At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 All sizes must not be 0 (<a href="sdk-for-android-navigate-mapmeasuredependentrendersize#sizes"><code>MapMeasureDependentRenderSize.sizes</code></a> with all values set to 0.0).</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>dashLength</code> - <p>The dash length of the polyline depending on the map measure.</p></dd>
<dd><code>gapLength</code> - <p>The gap length of the polyline depending on the map measure.</p></dd>
<dd><code>dashColor</code> - <p>The color of the dashes.</p></dd>
<dd><code>gapColor</code> - <p>The color of the gaps.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
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
<section className="detail" id="getLineWidth()">
<h3>getLineWidth</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span className="element-name">getLineWidth</span>()</div>
<div className="block"><p>Gets the map measure dependent polyline width.
 At map measures smaller than smallest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>lineWidth</code>.
 At map measures bigger than biggest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>lineWidth</code>.
 At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The width of the polyline depending on the map measure.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDashLength()">
<h3>getDashLength</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span className="element-name">getDashLength</span>()</div>
<div className="block"><p>Gets the map measure dependent polyline dash length.
 At map measures smaller than smallest map measure in the <code>dashLength</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>dashLength</code>.
 At map measures bigger than biggest map measure in the <code>dashLength</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>dashLength</code>.
 At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The dash length of the polyline depending on the map measure.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGapLength()">
<h3>getGapLength</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span className="element-name">getGapLength</span>()</div>
<div className="block"><p>Gets the map measure dependent polyline gap length.
 At map measures smaller than smallest map measure in the <code>gapLength</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>gapLength</code>.
 At map measures bigger than biggest map measure in the <code>gapLength</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>gapLength</code>.
 At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The gap length of the polyline depending on the map measure.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDashColor()">
<h3>getDashColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getDashColor</span>()</div>
<div className="block"><p>Gets the color of the dashes of the polyline.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The color of the dashes of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGapColor()">
<h3>getGapColor</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getGapColor</span>()</div>
<div className="block"><p>Gets the color for the gaps of the polyline. Returns <code>null</code> if no
 color is used.</p></div>
<dl className="notes">
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
</div>



</div>
`
}</HTMLBlock>
