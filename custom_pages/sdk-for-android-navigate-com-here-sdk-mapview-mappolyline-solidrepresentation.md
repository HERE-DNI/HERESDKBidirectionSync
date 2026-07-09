---
title: "MapPolyline.SolidRepresentation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidrepresentation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapPolyline.SolidRepresentation.html -->






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
<div className="inheritance">com.here.sdk.mapview.MapPolyline.SolidRepresentation</div>
</div>
</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">MapPolyline.SolidRepresentation</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></span></div>
<div className="block"><p>Representation for a solid line without outline.
 Can represent polylines that have constant width or width dependent on the map zoom.
 To achieve constant width lines, use <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> with a single value.
 To achieve line width dependent on map zoom, use <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> with
 multiple values.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.</p></div>
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


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidrepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)">SolidRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a representation for a solid line without outline.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidrepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)">SolidRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> outlineWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a representation for a solid line with outline.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)">
<h3>SolidRepresentation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SolidRepresentation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape)</span>
                    throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div className="block"><p>Creates a representation for a solid line without outline.
 At map measures smaller than smallest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>lineWidth</code>.
 At map measures bigger than biggest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>lineWidth</code>.
 At map measures between two nearest given map measures line width is
 linearly interpolated between width values given for these map measures.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 <code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>color</code> - <p>The color of the polyline.</p></dd>
<dd><code>capShape</code> - <p>The cap shape applied to both ends of the polyline.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap)">
<h3>SolidRepresentation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SolidRepresentation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> outlineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape)</span>
                    throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div className="block"><p>Creates a representation for a solid line with outline.
 The total width of the polyline is <code>line width + 2 * outline width</code>.
 At map measures smaller than smallest map measure in the <code>lineWidth</code>
 and <code>outlineWidth</code>, the value is constant and equal to the width given for
 the smallest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.
 At map measures bigger than biggest map measure in the <code>lineWidth</code>
 and <code>outlineWidth</code>, the value is constant and equal to the width given for
 the biggest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.
 At map measures between two nearest given map measure is
 linearly interpolated between width values given for these map measures.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 <code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>color</code> - <p>The color of the polyline.</p></dd>
<dd><code>outlineWidth</code> - <p>The width of the outline on one side of the polyline depending on
     the map measure.</p></dd>
<dd><code>outlineColor</code> - <p>The outline color of the polyline.</p></dd>
<dd><code>capShape</code> - <p>The cap shape applied to both ends of the polyline.</p></dd>
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
<section className="detail" id="getLineColor()">
<h3>getLineColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getLineColor</span>()</div>
<div className="block"><p>Gets the color of the polyline.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The color of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOutlineWidth()">
<h3>getOutlineWidth</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span className="element-name">getOutlineWidth</span>()</div>
<div className="block"><p>Gets the map measure dependent polyline outline width.
 The total width of the polyline is <code>line width + 2 * outline width</code>.
 At map measures smaller than smallest map measure in the <code>outlineWidth</code>,
 outline width is constant and equal to the width given for the smallest
 map measure in the <code>outlineWidth</code>.
 At map measures bigger than biggest map measure in the <code>outlineWidth</code>,
 outline width is constant and equal to the width given for the biggest
 map measure in the <code>outlineWidth</code>.
 At map measures between two nearest given map measures, the values are
 linearly interpolated between values given for these map measures.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The width of the outline on one side of the polyline depending on the map measure.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOutlineColor()">
<h3>getOutlineColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getOutlineColor</span>()</div>
<div className="block"><p>Gets the color of outline of the polyline.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The outline color of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCapShape()">
<h3>getCapShape</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-linecap" title="enum class in com.here.sdk.mapview">LineCap</a></span> <span className="element-name">getCapShape</span>()</div>
<div className="block"><p>Returns the cap shape of the polyline and its outline.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
