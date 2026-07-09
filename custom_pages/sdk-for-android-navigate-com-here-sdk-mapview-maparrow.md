---
title: "MapArrow (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-maparrow"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapArrow.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapArrow</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapArrow</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A visual representation of an arrow on the map. It consists of a tail - a polyline with an arbitrary
 number of points - and a head at its end.
 The map arrows are only visible on zoom levels &gt;= 13.
 Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-maparrow#%3Cinit%3E(com.here.sdk.core.GeoPolyline,double,com.here.sdk.core.Color)">MapArrow</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> geometry,
 double widthInPixels,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new <code>MapArrow</code> instance.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoPolyline,double,com.here.sdk.core.Color)">
<h3>MapArrow</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapArrow</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> geometry,
 double widthInPixels,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</span></div>
<div className="block"><p>Creates a new <code>MapArrow</code> instance.
 Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geometry</code> - <p>The geometry of the arrow tail. The last coordinate in the list defines the position where the
     head of the arrow is located.</p></dd>
<dd><code>widthInPixels</code> - <p>The width of the arrow tail in pixel. Negative values are clamped to 0. The tip is scaled accordingly.</p></dd>
<dd><code>color</code> - <p>The color of the arrow. The alpha channel is ignored, the color is
     interpreted as fully opaque.</p></dd>
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
<section className="detail" id="getMeasureDependentTailWidth()">
<h3>getMeasureDependentTailWidth</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt;</span> <span className="element-name">getMeasureDependentTailWidth</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> dependent arrow tail width in pixels.
 If tail width was configured without <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> dependency, then <code>measureDependentTailWidth</code>
 contains single entry with measure 0 of type <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> and width value
 equal to <code>widthInPixels</code>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The width of the arrow tail in pixels, where the key is a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> and the value is
     a tail width in pixels at this <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setMeasureDependentTailWidth(java.util.Map)">
<h3>setMeasureDependentTailWidth</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMeasureDependentTailWidth</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; value)</span></div>
<div className="block"><p>Sets the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> dependent arrow tail width in pixels.
 The width values are linearly interpolated between nearest map entries.
 Width values for <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> outside the map entries are kept constant, using the
 value of the largest/smallest key.
 Only <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> of <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type is supported.
 Other <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> types are unsupported and hence, will be ignored.
 Map with a single entry is equivalent to use of the <code>widthInPixels</code> value
 in the constructor, so a constant width setting, independent of camera.
 Empty input is ignored and existing width is maintained.
 The width values should be positive. Map entries with width values less than or equal to 0 are ignored.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The width of the arrow tail in pixels, where the key is a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a> and the value is
     a tail width in pixels at this <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure" title="class in com.here.sdk.mapview"><code>MapMeasure</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVisibilityRanges()">
<h3>getVisibilityRanges</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</span> <span className="element-name">getVisibilityRanges</span>()</div>
<div className="block"><p>Gets the list of visibility ranges.
 A range is half-open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
 is not contained in the range.
 When empty (the default), the map arrows are visible without map measure restrictions.
 Only <code>MapMeasureRange</code>(s) of <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <code>MapMeasureRange</code>(s) of other unsupported types will be ignored.}</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of visibility ranges, in which the map arrow is visible.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setVisibilityRanges(java.util.List)">
<h3>setVisibilityRanges</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setVisibilityRanges</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</span></div>
<div className="block"><p>Sets visibility ranges for this map arrow.
 A range is half-open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
 is not contained in the range.
 When empty (the default), the map arrows are visible without map measure restrictions.
 Only <code>MapMeasureRange</code>(s) of <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <code>MapMeasureRange</code>(s) of other unsupported types will be ignored.}</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The list of visibility ranges, in which the map arrow is visible.</p></dd>
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
