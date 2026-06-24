---
title: "MapPolyline.SolidMultiColorRepresentation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapPolyline.SolidMultiColorRepresentation.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance"><a href="sdk-for-android-explore-mapitemrepresentation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapItemRepresentation</a>
<div class="inheritance"><a href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview">com.here.sdk.mapview.MapPolyline.Representation</a>
<div class="inheritance">com.here.sdk.mapview.MapPolyline.SolidMultiColorRepresentation</div>
</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">MapPolyline.SolidMultiColorRepresentation</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-mappolyline.representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></span></div>
<div class="block"><p>Representation allows map polyline to be colored in multiple specified color segments.
 </p><p>Color segment is defined by color stops. Color stop is specified as a polyline
 length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
 Color stop represents a color change starting at that exact point up until
 either the next color stop (if one exists) or the end of the polyline.
 </p><p>Progress color <code>MapPolyline.progressColor</code> overrides any of the multiple color.
 </p><p>Examples:
 The following configuration will color map polyline as follows:
 - from the start to the middle of it at the 0.5 point - in Red
 - from the middle point 0.5 to the 0.7 point - in Green
 - from 0.7 to 1.0 - in Red
 'colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}'
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)">SolidMultiColorRepresentation</a><wbr/>(<a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-explore-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a>&gt; colors,
 double gradientLength)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a representation for a multicolored line without an outline.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation#%3Cinit%3E(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)">SolidMultiColorRepresentation</a><wbr/>(<a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> outlineWidth,
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 <a href="sdk-for-android-explore-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a>&gt; colors,
 double gradientLength)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a representation for a multicolored line with an outline.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation#setMultiColorGradientLength(double)">setMultiColorGradientLength</a><wbr/>(double length)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the multiple color segment gradient length.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation#setMultiColors(java.util.List,java.util.List,java.util.List)">setMultiColors</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a>&gt; colors)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets lists of colors and multiple color segment stops for the polyline to be colored in.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)">
<h3>SolidMultiColorRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SolidMultiColorRepresentation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-explore-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a>&gt; colors,
 double gradientLength)</span>
                              throws <span class="exceptions"><a href="sdk-for-android-explore-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div class="block"><p>Creates a representation for a multicolored line without an outline.
 </p><p>Color segment is defined by color stops. Color stop is specified as a polyline
 length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
 Color stop represents a color change starting at that exact point up until
 either the next color stop (if one exists) or the end of the polyline.
 </p><p>Progress color <code>MapPolyline.progressColor</code> overrides any of the multiple color.
 </p><p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the smallest
 map measure in the <code>lineWidth</code>.
 </p><p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
 line width is constant and equal to the width given for the biggest
 map measure in the <code>lineWidth</code>.
 </p><p>At map measures between two nearest given map measures line width is
 linearly interpolated between width values given for these map measures.
 </p><p>For <a href="sdk-for-android-explore-mapmeasure.kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-explore-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 </p><p>For <a href="sdk-for-android-explore-rendersize.unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-explore-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 </p><p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
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
     </p><p>Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color
     gradient of specific length which is part of the color segment being blended.
     </p><p>Start of the segment is blended with a color from the previous segment.
     Blending length is specified as a ratio of the smallest color segment length (from the list of color stops).
     E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment.
     For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the
     smallest segment's size to other segment size ratio.
     </p><p>Length of '0.0' is the default value which means blending will not be applied.
     Valid value range is [0.0, 1.0]. Out of range values are not supported.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></code> - <p>In case of invalid input parameters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.mapview.LineCap,java.util.List,java.util.List,java.util.List,double)">
<h3>SolidMultiColorRepresentation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SolidMultiColorRepresentation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> lineWidth,
 @NonNull
 <a href="sdk-for-android-explore-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> outlineWidth,
 @NonNull
 <a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a> outlineColor,
 @NonNull
 <a href="sdk-for-android-explore-linecap" title="enum class in com.here.sdk.mapview">LineCap</a> capShape,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a>&gt; colors,
 double gradientLength)</span>
                              throws <span class="exceptions"><a href="sdk-for-android-explore-mappolyline.representation.instantiationexception" title="class in com.here.sdk.mapview">MapPolyline.Representation.InstantiationException</a></span></div>
<div class="block"><p>Creates a representation for a multicolored line with an outline.
 </p><p>Color segment is defined by color stops. Color stop is specified as a polyline
 length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
 Color stop represents a color change starting at that exact point up until
 either the next color stop (if one exists) or the end of the polyline.
 </p><p>Progress color <code>MapPolyline.progressColor</code> overrides any of the multiple color.
 </p><p>The total width of the polyline is <code>line width + 2 * outline width</code>.
 </p><p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
 and <code>outlineWidth</code>, the value is constant and equal to the width given for
 the smallest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.
 </p><p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
 and <code>outlineWidth</code>, the value is constant and equal to the width given for
 the biggest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.
 </p><p>At map measures between two nearest given map measure is
 linearly interpolated between width values given for these map measures.
 </p><p>For <a href="sdk-for-android-explore-mapmeasure.kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-explore-mapmeasure.kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 </p><p>For <a href="sdk-for-android-explore-rendersize.unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-explore-rendersize.unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 </p><p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
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
     </p><p>Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color
     gradient of specific length which is part of the color segment being blended.
     </p><p>Start of the segment is blended with a color from the previous segment.
     Blending length is specified as a ratio of the smallest color segment length (from the list of color stops).
     E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment.
     For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the
     smallest segment's size to other segment size ratio.
     </p><p>Length of '0.0' is the default value which means blending will not be applied.
     Valid value range is [0.0, 1.0]. Out of range values are not supported.</p></dd>
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
<section class="detail" id="setMultiColors(java.util.List,java.util.List,java.util.List)">
<h3>setMultiColors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setMultiColors</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; colorStops,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html" title="class or interface in java.lang">Long</a>&gt; colorIndices,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-color" title="class in com.here.sdk.core">Color</a>&gt; colors)</span></div>
<div class="block"><p>Sets lists of colors and multiple color segment stops for the polyline to be colored in.
 When this representation is already set on any <code>MapPolyline</code>, values will be applied on that <code>MapPolyline</code> right away.
 If this representation is not set on any <code>MapPolyline</code>, values will be applied once representation is set on a <code>MapPolyline</code>.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
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
<section class="detail" id="setMultiColorGradientLength(double)">
<h3>setMultiColorGradientLength</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">setMultiColorGradientLength</span><wbr/><span class="parameters">(double length)</span></div>
<div class="block"><p>Sets the multiple color segment gradient length.
 </p><p>Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color
 gradient of specific length which is part of the color segment being blended.
 </p><p>Start of the segment is blended with a color from the previous segment.
 Blending length is specified as a ratio of the smallest color segment length (from the list of color stops).
 E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment.
 For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the
 smallest segment's size to other segment size ratio.
 </p><p>Length of '0.0' is the default value which means blending will not be applied.
 Valid value range is [0.0, 1.0]. Out of range values are not supported.
 When this representation is already set on any <code>MapPolyline</code>, value will be applied on that <code>MapPolyline</code> right away.
 If this representation is not set on any <code>MapPolyline</code>, value will be applied once representation is set on a <code>MapPolyline</code>.
 </p><p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>
