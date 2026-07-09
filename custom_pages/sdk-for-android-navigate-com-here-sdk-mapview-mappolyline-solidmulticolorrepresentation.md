---
title: "MapPolyline.SolidMultiColorRepresentation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapPolyline.SolidMultiColorRepresentation.html -->






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
<div className="inheritance">com.here.sdk.mapview.MapPolyline.SolidMultiColorRepresentation</div>
</div>
</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>

<div className="type-signature"><span className="modifiers">public static final class </span><span className="element-name type-name-label">MapPolyline.SolidMultiColorRepresentation</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></span></div>
<div className="block"><p>Representation allows map polyline to be colored in multiple specified color segments.
 Color segment is defined by color stops. Color stop is specified as a polyline
 length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
 Color stop represents a color change starting at that exact point up until
 either the next color stop (if one exists) or the end of the polyline.
 Progress color <code>MapPolyline.progressColor</code> overrides any of the multiple color.
 Examples:
 The following configuration will color map polyline as follows:
 - from the start to the middle of it at the 0.5 point - in Red
 - from the middle point 0.5 to the 0.7 point - in Green
 - from 0.7 to 1.0 - in Red
 'colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}'
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
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


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)">SolidMultiColorRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a>&gt; colors,
 double gradientLength)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a representation for a multicolored line without an outline.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)">SolidMultiColorRepresentation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> outlineWidth,
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a>&gt; colors,
 double gradientLength)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a representation for a multicolored line with an outline.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)">
<h3>SolidMultiColorRepresentation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SolidMultiColorRepresentation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a>&gt; colors,
 double gradientLength)</span>
                              throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div className="block"><p>Creates a representation for a multicolored line without an outline.
 Color segment is defined by color stops. Color stop is specified as a polyline
 length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
 Color stop represents a color change starting at that exact point up until
 either the next color stop (if one exists) or the end of the polyline.
 Progress color <code>MapPolyline.progressColor</code> overrides any of the multiple color.
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
 <code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>capShape</code> - <p>The cap shape applied to both ends of the polyline.</p></dd>
<dd><code>colorStops</code> - <p>List containing color stop values indicating a change of color on a polyline.
     Color stops must be in the range of [0.0, 1.0].
     Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed.
     Color stop list must be of the same size as color indices list.
     Maximum size is 100 color stops.
     An empty list is not allowed. The first color stop value in the list must be 0.0.</p></dd>
<dd><code>colorIndices</code> - <p>List of color indices (from the color list) corresponding to the color stops.
     Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed.
     Color indices list must be of the same size as color stop list.
     Maximum size is 100 color indices.</p></dd>
<dd><code>colors</code> - <p>List of colors.
     Maximum size is 16 colors.
     An empty list is not allowed.</p></dd>
<dd><code>gradientLength</code> - <p>Multiple color segment gradient length.
     Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color
     gradient of specific length which is part of the color segment being blended.
     Start of the segment is blended with a color from the previous segment.
     Blending length is specified as a ratio of the smallest color segment length (from the list of color stops).
     E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment.
     For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the
     smallest segment's size to other segment size ratio.
     Length of '0.0' is the default value which means blending will not be applied.
     Valid value range is [0.0, 1.0]. Out of range values are not supported.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)">
<h3>SolidMultiColorRepresentation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SolidMultiColorRepresentation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> outlineWidth,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a>&gt; colors,
 double gradientLength)</span>
                              throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div className="block"><p>Creates a representation for a multicolored line with an outline.
 Color segment is defined by color stops. Color stop is specified as a polyline
 length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
 Color stop represents a color change starting at that exact point up until
 either the next color stop (if one exists) or the end of the polyline.
 Progress color <code>MapPolyline.progressColor</code> overrides any of the multiple color.
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
 <code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lineWidth</code> - <p>The width of the polyline depending on the map measure.</p></dd>
<dd><code>outlineWidth</code> - <p>The width of the outline on one side of the polyline depending on the map measure.</p></dd>
<dd><code>outlineColor</code> - <p>The outline color of the polyline.</p></dd>
<dd><code>capShape</code> - <p>The cap shape applied to both ends of the polyline.</p></dd>
<dd><code>colorStops</code> - <p>List containing color stop values indicating a change of color on a polyline.
     Color stops must be in the range of [0.0, 1.0].
     Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed.
     Color stop list must be of the same size as color indices list.
     Maximum size is 100 color stops.
     An empty list is not allowed. The first color stop value in the list must be 0.0.</p></dd>
<dd><code>colorIndices</code> - <p>List of color indices (from the color list) corresponding to the color stops.
     Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed.
     Color indices list must be of the same size as color stop list.
     Maximum size is 100 color indices.</p></dd>
<dd><code>colors</code> - <p>List of colors.
     Maximum size is 16 colors.
     An empty list is not allowed.</p></dd>
<dd><code>gradientLength</code> - <p>Multiple color segment gradient length.
     Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color
     gradient of specific length which is part of the color segment being blended.
     Start of the segment is blended with a color from the previous segment.
     Blending length is specified as a ratio of the smallest color segment length (from the list of color stops).
     E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment.
     For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the
     smallest segment's size to other segment size ratio.
     Length of '0.0' is the default value which means blending will not be applied.
     Valid value range is [0.0, 1.0]. Out of range values are not supported.</p></dd>
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
<section className="detail" id="setMultiColors(java.util.List,java.util.List,java.util.List)">
<h3>setMultiColors</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">setMultiColors</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a>&gt; colors)</span></div>
<div className="block"><p>Sets lists of colors and multiple color segment stops for the polyline to be colored in.
 When this representation is already set on any <code>MapPolyline</code>, values will be applied on that <code>MapPolyline</code> right away.
 If this representation is not set on any <code>MapPolyline</code>, values will be applied once representation is set on a <code>MapPolyline</code>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>colorStops</code> - <p>List containing color stop values indicating a change of color on a polyline.
     Color stops must be in the range of [0.0, 1.0].
     Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed.
     Color stop list must be of the same size as color indices list.
     Maximum size is 100 color stops.
     An empty list is not allowed. The first color stop value in the list must be 0.0.</p></dd>
<dd><code>colorIndices</code> - <p>List of color indices (from the color list) corresponding to the color stops.
     Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed.
     Color indices list must be of the same size as color stop list.
     Maximum size is 100 color indices.</p></dd>
<dd><code>colors</code> - <p>List of colors.
     Maximum size is 16 colors.
     An empty list is not allowed.</p></dd>
<dt>Returns:</dt>
<dd><p>Value indicating whether parameters are valid and can be applied.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setMultiColorGradientLength(double)">
<h3>setMultiColorGradientLength</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">setMultiColorGradientLength</span><wbr/><span className="parameters">(double length)</span></div>
<div className="block"><p>Sets the multiple color segment gradient length.
 Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color
 gradient of specific length which is part of the color segment being blended.
 Start of the segment is blended with a color from the previous segment.
 Blending length is specified as a ratio of the smallest color segment length (from the list of color stops).
 E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment.
 For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the
 smallest segment's size to other segment size ratio.
 Length of '0.0' is the default value which means blending will not be applied.
 Valid value range is [0.0, 1.0]. Out of range values are not supported.
 When this representation is already set on any <code>MapPolyline</code>, value will be applied on that <code>MapPolyline</code> right away.
 If this representation is not set on any <code>MapPolyline</code>, value will be applied once representation is set on a <code>MapPolyline</code>.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>length</code> - <p>Multiple color segment gradient length. Length of '0.0' is the default value which means blending will not be applied.
     Valid value range is [0.0, 1.0]. Out of range values are not supported.</p></dd>
<dt>Returns:</dt>
<dd><p>Value indicating whether specified value is valid and can be applied.</p></dd>
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
