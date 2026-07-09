---
title: "MapPolygon (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mappolygon"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapPolygon.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapPolygon</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapPolygon</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A visual representation of a polygon on the map. Can be used to visualize areas of all shapes
 and sizes.
 The geometry to be visualized is represented by an instance of <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core"><code>GeoPolygon</code></a>.
 To display circular areas (for example, a position accuracy indicator) use a GeoPolygon
 created from a <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a> using <a href="sdk-for-android-navigate-geopolygon#%3Cinit%3E(com.here.sdk.core.GeoBox)"><code>GeoPolygon(GeoCircle)</code></a>.
 Note:
 <ul>
<li>The polygon shape should not cover more than half of the globe,
 otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
 artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul></p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolygon#%3Cinit%3E(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color)">MapPolygon</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geometry,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolygon#%3Cinit%3E(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color,com.here.sdk.core.Color,double)">MapPolygon</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geometry,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 double outlineWidthInPixels)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color)">
<h3>MapPolygon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapPolygon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geometry,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</span></div>
<div className="block"><p>Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.
 The winding order of the vertices can be in clockwise or counter-clockwise order.
 It is recomended to provide the outer boundary ordered clockwise and closed.
 Note:
 <ul>
<li>The polygon shape should not cover more than half of the globe,
 otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
 artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul></p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>geometry</code> - <p>The list of vertices representing the outer boundary of polygon.</p></dd>
<dd><code>color</code> - <p>The fill color for the polygon</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoPolygon,com.here.sdk.core.Color,com.here.sdk.core.Color,double)">
<h3>MapPolygon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapPolygon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geometry,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 double outlineWidthInPixels)</span></div>
<div className="block"><p>Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.
 Transparent outlines are not supported. Any color with transparency (alpha value other than 1)
 will be rendered as fully opaque by interpreting the alpha value as 1.
 The winding order of the vertices can be in clockwise or counter-clockwise order.
 It is recomended to provide the outer boundary ordered clockwise and closed.
 Note:
 <ul>
<li>The polygon shape should not cover more than half of the globe,
 otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
 artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul></p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a></span> <span className="element-name">getGeometry</span>()</div>
<div className="block"><p>Gets the current geometry of the polygon.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The geometry of the polygon. Setting a new geometry will update the appearance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setGeometry(com.here.sdk.core.GeoPolygon)">
<h3>setGeometry</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setGeometry</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> value)</span></div>
<div className="block"><p>Sets a new geometry to update the appearance.
 The winding order of the vertices can be in clockwise or counter-clockwise order.
 It is recomended to provide the outer boundary ordered clockwise and closed.
 Note:
 <ul>
<li>The polygon shape should not cover more than half of the globe,
 otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
 artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul></p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The geometry of the polygon. Setting a new geometry will update the appearance.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMetadata()">
<h3>getMetadata</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a></span> <span className="element-name">getMetadata</span>()</div>
<div className="block"><p>Gets the Metadata instance attached to this polygon.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The Metadata instance attached to this polygon, <code>null</code> by default.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setMetadata(com.here.sdk.core.Metadata)">
<h3>setMetadata</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMetadata</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a> value)</span></div>
<div className="block"><p>Sets the Metadata instance to be attached to this polygon.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The Metadata instance attached to this polygon, <code>null</code> by default.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getFillColor()">
<h3>getFillColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getFillColor</span>()</div>
<div className="block"><p>Gets the current color of the fill.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Color of the polygon's fill.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setFillColor(com.here.sdk.core.Color)">
<h3>setFillColor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setFillColor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div className="block"><p>Sets the current color of the fill.
 Fully transparent color (alpha set to 0) disables the fill completely.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Color of the polygon's fill.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDrawOrder()">
<h3>getDrawOrder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getDrawOrder</span>()</div>
<div className="block"><p>Gets the draw order of this map polygon relative to other map polygons. Default value is 0.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The draw order of this map polygon relative to other map polygons.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDrawOrder(int)">
<h3>setDrawOrder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDrawOrder</span><wbr/><span className="parameters">(int value)</span></div>
<div className="block"><p>Sets the draw order of this map polygon relative to other map polygons.
 Polygon with higher draw order value are drawn
 on top of polygons with lower draw order.
 In case multiple polygons have the same draw order value
 then the order in which they were added to the scene matters. Last added polygon is drawn on top.
 Allowed range is 0-1023. Values outside this range will be clamped.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The draw order of this map polygon relative to other map polygons.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVisibilityRanges()">
<h3>getVisibilityRanges</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</span> <span className="element-name">getVisibilityRanges</span>()</div>
<div className="block"><p>Gets the list of visibility ranges. The map polygon is visible only inside these map measure
 ranges. When empty (the default), the map polygon is visible without map measure restrictions.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of visibility ranges. The map polygon is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setVisibilityRanges(java.util.List)">
<h3>setVisibilityRanges</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setVisibilityRanges</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</span></div>
<div className="block"><p>Sets visibility ranges for this map polygon. A range is half open -
 [minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.
 The map polygon is visible only inside these map measure ranges.
 When empty (the default), the map polygon is visible without map measure restrictions.
 Only <code>MapMeasureRange</code>(s) of <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <code>MapMeasureRange</code>(s) of other unsupported types will be ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The list of visibility ranges. The map polygon is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOutlineColor()">
<h3>getOutlineColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getOutlineColor</span>()</div>
<div className="block"><p>Gets the color of the polygon outline. The default outline color is opaque white.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The color of the polygon outline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setOutlineColor(com.here.sdk.core.Color)">
<h3>setOutlineColor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOutlineColor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div className="block"><p>Sets the color of the polygon outline.
 Transparent outlines are not supported. Any color with transparency (alpha value other than 1)
 will be rendered as fully opaque.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The color of the polygon outline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getOutlineWidth()">
<h3>getOutlineWidth</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getOutlineWidth</span>()</div>
<div className="block"><p>Gets the outline width of the polygon in pixels.
 By default, the outline width is set to zero.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The width of the polygon outline in pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setOutlineWidth(double)">
<h3>setOutlineWidth</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setOutlineWidth</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the outline width of the polygon in pixels.
 The value should be greater than or equal to 0.
 Negative values are clamped to zero.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
