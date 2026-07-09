---
title: "MapMeasureDependentRenderSize (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapMeasureDependentRenderSize.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.MapMeasureDependentRenderSize</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapMeasureDependentRenderSize</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents a render size, described as map measure dependent values.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationerrorcode" title="enum class in com.here.sdk.mapview">MapMeasureDependentRenderSize.InstantiationErrorCode</a></code></div>
<div className="col-last even-row-color">
<div className="block">Describes a reason for failing to create a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize.InstantiationException</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Thrown when a problem occurs while trying to create <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview">MapMeasure.Kind</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#measureKind">measureKind</a></code></div>
<div className="col-last even-row-color">
<div className="block">The unit used for the key in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#sizes"><code>sizes</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>final <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#sizes">sizes</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The dictionary describing the size (value) per map measure (key).</div>
</div>
<div className="col-first even-row-color"><code>final <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#sizeUnit">sizeUnit</a></code></div>
<div className="col-last even-row-color">
<div className="block">The unit used for the value in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#sizes"><code>sizes</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#%3Cinit%3E(com.here.sdk.mapview.MapMeasure.Kind,com.here.sdk.mapview.RenderSize.Unit,java.util.Map)">MapMeasureDependentRenderSize</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview">MapMeasure.Kind</a> measureKind,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> sizeUnit,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; sizes)</code></div>
<div className="col-last even-row-color">
<div className="block">Constructs a <code>MapMeasureDependentRenderSize</code> from given parameters.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#%3Cinit%3E(com.here.sdk.mapview.RenderSize.Unit,double)">MapMeasureDependentRenderSize</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> sizeUnit,
 double size)</code></div>
<div className="col-last odd-row-color">
<div className="block">Constructs a <code>MapMeasureDependentRenderSize</code> from single size value which is constant across all map measures.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="measureKind">
<h3>measureKind</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview">MapMeasure.Kind</a></span> <span className="element-name">measureKind</span></div>
<div className="block"><p>The unit used for the key in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#sizes"><code>sizes</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="sizeUnit">
<h3>sizeUnit</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a></span> <span className="element-name">sizeUnit</span></div>
<div className="block"><p>The unit used for the value in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#sizes"><code>sizes</code></a>.</p></div>
</section>
</li>
<li>
<section className="detail" id="sizes">
<h3>sizes</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public final</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt;</span> <span className="element-name">sizes</span></div>
<div className="block"><p>The dictionary describing the size (value) per map measure (key).
 Units of keys and values are defined in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#measureKind"><code>measureKind</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#sizeUnit"><code>sizeUnit</code></a>.
 <code>sizes</code> with a single entry indicates using a fixed size value across all map measures.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasure.Kind,com.here.sdk.mapview.RenderSize.Unit,java.util.Map)">
<h3>MapMeasureDependentRenderSize</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMeasureDependentRenderSize</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview">MapMeasure.Kind</a> measureKind,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> sizeUnit,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; sizes)</span>
                              throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize.InstantiationException</a></span></div>
<div className="block"><p>Constructs a <code>MapMeasureDependentRenderSize</code> from given parameters.
 Supplying <code>sizes</code> map with a single entry indicates using a fixed size value across all map measures.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>measureKind</code> - <p>The unit used for the key in <code>sizes</code>.</p></dd>
<dd><code>sizeUnit</code> - <p>The unit used for the value in <code>sizes</code>.</p></dd>
<dd><code>sizes</code> - <p>The dictionary describing the size (value) per map measure (key).</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize.InstantiationException</a></code> - <p>Instantiation error if <code>sizes</code> map is empty or contains negative keys or values.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.RenderSize.Unit,double)">
<h3>MapMeasureDependentRenderSize</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapMeasureDependentRenderSize</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview">RenderSize.Unit</a> sizeUnit,
 double size)</span>
                              throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize.InstantiationException</a></span></div>
<div className="block"><p>Constructs a <code>MapMeasureDependentRenderSize</code> from single size value which is constant across all map measures.
 The given <code>size</code> value is stored in <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#sizes"><code>sizes</code></a> map at key 0 and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize#measureKind"><code>measureKind</code></a> is set to <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sizeUnit</code> - <p>The unit used for the value in <code>size</code>.</p></dd>
<dd><code>size</code> - <p>The size independent of map measure. Must not be negative.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize.InstantiationException</a></code> - <p>Instantiation error if <code>size</code> is negative.</p></dd>
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
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
