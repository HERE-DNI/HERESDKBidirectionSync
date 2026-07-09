---
title: "MapPolyline.DashImageRepresentation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapPolyline.DashImageRepresentation.html -->






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
<div className="inheritance">com.here.sdk.mapview.MapPolyline.DashImageRepresentation</div>
</div>
</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">MapPolyline.DashImageRepresentation</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></span></div>
<div className="block"><p>Represents a dash pattern for the map polyline consisting of images rendered with certain gaps
 from each other.
 This dash pattern representation consists only of images rendered at certain
 points along the polyline. For rendering them without any distortions, polyline gets sliced into
 series of straight segments that are multiple of sum of dash and gap lengths. For this
 reason, the new polyline geometry might not align fully with original geometry.
 The <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation#getDashImage()"><code>getDashImage()</code></a> is stretched according to <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation#getDashLength()"><code>getDashLength()</code></a>
 and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation#getDashWidth()"><code>getDashWidth()</code></a>, with image's width matched to <code>dashLength</code> and
 image's height matched to <code>dashWidth</code>. The image is oriented so that its bottom is on the
 left-hand side between vertices <code>n</code> and <code>n+1</code>.
 The spacing between images is specified by <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation#getGapLength()"><code>getGapLength()</code></a>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)">DashImageRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a uniform dash pattern in which the length of a gap is the same as the length of
 a dash.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)">DashImageRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a simple dash pattern in which the lengths of a dash and gap can be different.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)">
<h3>DashImageRepresentation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DashImageRepresentation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</span>
                        throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div className="block"><p>Creates a uniform dash pattern in which the length of a gap is the same as the length of
 a dash. Dashes are rendered as image.
 This allows for patterns like <code>' — — — —'</code> or <code>' —— —— ——'</code>.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> supplied for <code>dashLength</code> and <code>dashWidth</code>,
 only <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported for <a href="sdk-for-android-navigate-mapmeasuredependentrendersize#measureKind"><code>MapMeasureDependentRenderSize.measureKind</code></a>
 and only <a href="sdk-for-android-navigate-rendersize-unit#METERS"><code>RenderSize.Unit.METERS</code></a> is supported for <a href="sdk-for-android-navigate-mapmeasuredependentrendersize#sizeUnit"><code>MapMeasureDependentRenderSize.sizeUnit</code></a>.
 Only map measure values in range [3-19] are supported.
 The value of the keys in <a href="sdk-for-android-navigate-mapmeasuredependentrendersize#sizes"><code>MapMeasureDependentRenderSize.sizes</code></a> is truncated to integer values,
 hence only a single value can be provided per zoom level.
 The values are interpolated linearly between zoom levels.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>dashLength</code> - <p>The map measure dependent length of a dash, to which image width is stretched.</p></dd>
<dd><code>dashWidth</code> - <p>The map measure dependent width of a dash, to which image height is stretched.</p></dd>
<dd><code>image</code> - <p>Image to be rendered in place of dash space. It is stretched to match <code>dashWidth</code> and <code>dashLength</code>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapImage)">
<h3>DashImageRepresentation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DashImageRepresentation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashLength,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> gapLength,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> dashWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</span>
                        throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div className="block"><p>Creates a simple dash pattern in which the lengths of a dash and gap can be different.
 Dashes are rendered as image.
 This allows for patterns like <code>' — — — —'</code> or <code>' ——— ——— ———'</code>.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> supplied for <code>dashLength</code>, <code>gapLength</code> and <code>dashWidth</code>,
 only <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported for <a href="sdk-for-android-navigate-mapmeasuredependentrendersize#measureKind"><code>MapMeasureDependentRenderSize.measureKind</code></a>
 and only <a href="sdk-for-android-navigate-rendersize-unit#METERS"><code>RenderSize.Unit.METERS</code></a> is supported for <a href="sdk-for-android-navigate-mapmeasuredependentrendersize#sizeUnit"><code>MapMeasureDependentRenderSize.sizeUnit</code></a>.
 Only map measure values in range [3-19] are supported.
 The value of the keys in <a href="sdk-for-android-navigate-mapmeasuredependentrendersize#sizes"><code>MapMeasureDependentRenderSize.sizes</code></a> is truncated to integer values,
 hence only a single value can be provided per zoom level.
 The values are interpolated linearly between zoom levels.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>dashLength</code> - <p>The map measure dependent length of a dash, to which image width is stretched.</p></dd>
<dd><code>gapLength</code> - <p>The map measure dependent length of a gap between dash images.</p></dd>
<dd><code>dashWidth</code> - <p>The map measure dependent width of a dash, to which image height is stretched.</p></dd>
<dd><code>image</code> - <p>Image to be rendered in place of dash space. It is stretched to match <code>dashWidth</code> and <code>dashLength</code>.</p></dd>
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
<section className="detail" id="getDashImage()">
<h3>getDashImage</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span className="element-name">getDashImage</span>()</div>
<div className="block"><p>Gets the image that is rendered in place of dash space.
 It is stretched to fill whole polyline width and length of each dash.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Image to be rendered in place of dash space.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDashLength()">
<h3>getDashLength</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span className="element-name">getDashLength</span>()</div>
<div className="block"><p>Gets the map measure dependent length of a dash, to which image width is stretched.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The map measure dependent length of a dash, to which image width is stretched.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGapLength()">
<h3>getGapLength</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span className="element-name">getGapLength</span>()</div>
<div className="block"><p>Gets the map measure dependent length of a gap between dash images.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The map measure dependent length of a gap between dash images.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDashWidth()">
<h3>getDashWidth</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span className="element-name">getDashWidth</span>()</div>
<div className="block"><p>Gets the map measure dependent width of a dash, to which image height is stretched.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The map measure dependent width of a dash, to which image height is stretched.</p></dd>
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
