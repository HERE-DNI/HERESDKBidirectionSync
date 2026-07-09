---
title: "MapPolyline (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mappolyline"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapPolyline.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapPolyline</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapPolyline</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A visual representation of a line on the map.
 The geometry to be visualized is represented by an instance of <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a>.
 Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation" title="class in com.here.sdk.mapview">MapPolyline.DashImageRepresentation</a></code></div>
<div className="col-last even-row-color">
<div className="block">Represents a dash pattern for the map polyline consisting of images rendered with certain gaps
 from each other.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashrepresentation" title="class in com.here.sdk.mapview">MapPolyline.DashRepresentation</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Represents a dash pattern for map polyline where the dash can be rendered as a colored
 line and the gap can be either empty or colored.</div>
</div>
<div className="col-first even-row-color"><code>static class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a></code></div>
<div className="col-last even-row-color">
<div className="block">Base class to represent the visual appearance of a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview"><code>MapPolyline</code></a>.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation" title="class in com.here.sdk.mapview">MapPolyline.SolidMultiColorRepresentation</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Representation allows map polyline to be colored in multiple specified color segments.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidrepresentation" title="class in com.here.sdk.mapview">MapPolyline.SolidRepresentation</a></code></div>
<div className="col-last even-row-color">
<div className="block">Representation for a solid line without outline.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline#%3Cinit%3E(com.here.sdk.core.GeoPolyline,com.here.sdk.mapview.MapPolyline.Representation)">MapPolyline</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> geometry,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a> representation)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new <code>MapPolyline</code> instance with a specified visual representation.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.GeoPolyline,com.here.sdk.mapview.MapPolyline.Representation)">
<h3>MapPolyline</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapPolyline</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> geometry,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a> representation)</span></div>
<div className="block"><p>Creates a new <code>MapPolyline</code> instance with a specified visual representation.
 Altitude component of <code>GeoPolyline</code>'s vertices is ignored.
 After creating a <code>MapPolyline</code> with this representation, the deprecated <code>MapPolyline</code>
 properties do not work and any change to them will be ignored. Any modifications to polyline's
 appearance must be done with <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline#setRepresentation(com.here.sdk.mapview.MapPolyline.Representation)"><code>setRepresentation(com.here.sdk.mapview.MapPolyline.Representation)</code></a>.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="setRepresentation(com.here.sdk.mapview.MapPolyline.Representation)">
<h3>setRepresentation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setRepresentation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview">MapPolyline.Representation</a> representation)</span></div>
<div className="block"><p>Changes the appearance of the <code>MapPolyline</code> instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>representation</code> - <p>The representation describing a new appearance of the <code>MapPolyline</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="startAnimation(com.here.sdk.animation.MapPolylineAnimation,com.here.sdk.animation.AnimationListener)">
<h3>startAnimation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">startAnimation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-mappolylineanimation" title="class in com.here.sdk.animation">MapPolylineAnimation</a> animation,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-animationlistener" title="interface in com.here.sdk.animation">AnimationListener</a> listener)</span></div>
<div className="block"><p>Starts an animation of this map polyline.
 The <code>MapPolylineAnimation</code> may be shared between multiple instances of <code>MapPolyline</code>.
 Starting animation on one polyline does not influence any ongoing animations on
 other polylines.
 Any ongoing animation of this map polyline will get cancelled.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>animation</code> - <p>The animation to start.</p></dd>
<dd><code>listener</code> - <p>The listener to receive notifications
     about animation start, completion or cancellation.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="cancelAnimation(com.here.sdk.animation.MapPolylineAnimation)">
<h3>cancelAnimation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">cancelAnimation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-animation-mappolylineanimation" title="class in com.here.sdk.animation">MapPolylineAnimation</a> animation)</span></div>
<div className="block"><p>Cancels single ongoing animation of this map polyline.
 Does nothing if the specified animation is not currently in progress for this polyline.
 Does not affect other polylines that might be running this animation.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>animation</code> - <p>The animation to cancel</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span className="element-name">getGeometry</span>()</div>
<div className="block"><p>Gets the geometry of the polyline.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of vertices that represent the geometry of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setGeometry(com.here.sdk.core.GeoPolyline)">
<h3>setGeometry</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setGeometry</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a> value)</span></div>
<div className="block"><p>Sets the geometry of the polyline. Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The list of vertices that represent the geometry of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMetadata()">
<h3>getMetadata</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a></span> <span className="element-name">getMetadata</span>()</div>
<div className="block"><p>Gets the <code>Metadata</code> instance attached to this polyline.
 This will be <code>null</code> if nothing has been attached before.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <code>Metadata</code> instance attached to this polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setMetadata(com.here.sdk.core.Metadata)">
<h3>setMetadata</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMetadata</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a> value)</span></div>
<div className="block"><p>Sets the <code>Metadata</code> instance attached to this polyline.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The <code>Metadata</code> instance attached to this polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDrawOrder()">
<h3>getDrawOrder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getDrawOrder</span>()</div>
<div className="block"><p>Gets the draw order of the polyline.
 The default draw order is 0.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The draw order of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDrawOrder(int)">
<h3>setDrawOrder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDrawOrder</span><wbr/><span className="parameters">(int value)</span></div>
<div className="block"><p>Sets the draw order of the polyline.
 Polylines with a higher draw order are drawn on top
 of polylines with a lower draw order.
 In case multiple polylines have the same draw
 order, they can be rendered in different ways depending on the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline#getDrawOrderType()"><code>getDrawOrderType()</code></a> set.
 Supplied value is clamped to the range [0; 1023].</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The draw order of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDrawOrderType()">
<h3>getDrawOrderType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a></span> <span className="element-name">getDrawOrderType</span>()</div>
<div className="block"><p>Gets the draw order type of the polyline.
 The default value is <a href="sdk-for-android-navigate-drawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The draw order type of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDrawOrderType(com.here.sdk.mapview.DrawOrderType)">
<h3>setDrawOrderType</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDrawOrderType</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-drawordertype" title="enum class in com.here.sdk.mapview">DrawOrderType</a> value)</span></div>
<div className="block"><p>Sets the draw order type of the polyline.
 For <a href="sdk-for-android-navigate-drawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT</code></a>, map polylines with outlines having
 the same draw order are drawn as a whole in the order of addition to a map scene. There
 is no possibility that parts of another polyline, regardless of its draw order value,
 are drawn between outline and mainline of another polyline.
 With <a href="sdk-for-android-navigate-drawordertype#MAP_SCENE_ADDITION_ORDER_DEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_DEPENDENT</code></a>, polylines are rendered one by one.
 For <a href="sdk-for-android-navigate-drawordertype#MAP_SCENE_ADDITION_ORDER_INDEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_INDEPENDENT</code></a>, for multiple polylines with
 outlines having the same draw order, all outlines are rendered first in an arbitrary order
 and then all mainlines are drawn on top of those polylines in an arbitrary order.
 <a href="sdk-for-android-navigate-drawordertype#MAP_SCENE_ADDITION_ORDER_INDEPENDENT"><code>DrawOrderType.MAP_SCENE_ADDITION_ORDER_INDEPENDENT</code></a> allows speeding up the rendering
 process and keeping high frame rates when many similar polylines (with same styling
 attributes and <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation" title="class in com.here.sdk.mapview"><code>MapPolyline.Representation</code></a>) are present in a map scene.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The draw order type of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getVisibilityRanges()">
<h3>getVisibilityRanges</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt;</span> <span className="element-name">getVisibilityRanges</span>()</div>
<div className="block"><p>Gets the list of visibility ranges. The map polyline is visible only inside these map measure
 ranges. When empty (the default), the map polyline is visible without map measure restrictions.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of visibility ranges. The map polyline is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setVisibilityRanges(java.util.List)">
<h3>setVisibilityRanges</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setVisibilityRanges</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>&gt; value)</span></div>
<div className="block"><p>Sets visibility ranges for this map polyline. A range is half open -
 [minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.
 The map polyline is visible only inside these map measure ranges.
 When empty (the default), the map polyline is visible without map measure restrictions.
 Only <code>MapMeasureRange</code>(s) of <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> type are supported.
 <code>MapMeasureRange</code>(s) of other unsupported types will be ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The list of visibility ranges. The map polyline is visible only inside these map measure ranges.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getProgress()">
<h3>getProgress</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getProgress</span>()</div>
<div className="block"><p>Gets the progress of the polyline, 0 by default.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The progress from the polyline's starting point, as a ratio of its total length clamped to
     the range [0, 1].</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setProgress(double)">
<h3>setProgress</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setProgress</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>Sets the progress of the polyline from its starting point as a ratio of its total length
 clamped to the range [0; 1].
 As the progress varies, the equivalent part of the
 polyline gets covered by the progress color and progress outline color. The rest of the
 polyline until its end point retains the line color and outline color along with an
 optional dash pattern.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The progress from the polyline's starting point, as a ratio of its total length clamped to
     the range [0, 1].</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getProgressColor()">
<h3>getProgressColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getProgressColor</span>()</div>
<div className="block"><p>Gets the progress color of the polyline, opaque white by default.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The color used for the progress part of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setProgressColor(com.here.sdk.core.Color)">
<h3>setProgressColor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setProgressColor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div className="block"><p>Sets the progress color of the polyline.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The color used for the progress part of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getProgressOutlineColor()">
<h3>getProgressOutlineColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getProgressOutlineColor</span>()</div>
<div className="block"><p>Gets the progress outline color of the polyline, opaque white by default.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The color used for outline of the progress part of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setProgressOutlineColor(com.here.sdk.core.Color)">
<h3>setProgressOutlineColor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setProgressOutlineColor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div className="block"><p>Sets the progress outline color of the polyline.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The color used for outline of the progress part of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getProgressGradientLength()">
<h3>getProgressGradientLength</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a></span> <span className="element-name">getProgressGradientLength</span>()</div>
<div className="block"><p>Gets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setProgressGradientLength(com.here.sdk.mapview.MapMeasureDependentRenderSize)">
<h3>setProgressGradientLength</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setProgressGradientLength</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview">MapMeasureDependentRenderSize</a> value)</span></div>
<div className="block"><p>Sets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.
 To achieve a constant gradient length, use <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a>
 with a single value. To achieve a gradient length dependent on map zoom,
 use <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasuredependentrendersize" title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize</code></a> with multiple values. The default value is a constant
 gradient length of zero pixels. The gradient is guaranteed to fit into polyline, i.e. the
 actual gradient can be shorter then <code>progressGradientLength</code>.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasure-kind" title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a> only <a href="sdk-for-android-navigate-mapmeasure-kind#ZOOM_LEVEL"><code>MapMeasure.Kind.ZOOM_LEVEL</code></a> is supported.
 For <a href="sdk-for-android-navigate-com-here-sdk-mapview-rendersize-unit" title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a> only <a href="sdk-for-android-navigate-rendersize-unit#PIXELS"><code>RenderSize.Unit.PIXELS</code></a> is supported.
 A parameter with unsupported values is ignored.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMapContentCategoriesToBlock()">
<h3>getMapContentCategoriesToBlock</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentcategory" title="enum class in com.here.sdk.mapview">MapContentCategory</a>&gt;</span> <span className="element-name">getMapContentCategoriesToBlock</span>()</div>
<div className="block"><p>Gets list of map content categories this polyline should block.
 Default value is an empty list meaning none of the map categories will be blocked.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>List of map content categories this polyline should block.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setMapContentCategoriesToBlock(java.util.List)">
<h3>setMapContentCategoriesToBlock</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMapContentCategoriesToBlock</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontentcategory" title="enum class in com.here.sdk.mapview">MapContentCategory</a>&gt; value)</span></div>
<div className="block"><p>Sets list of map content categories this polyline should block.
 Map content categories overlapping the polyline geometry
 (progress and non-progress) will be discarded from being rendered.
 Duplicate entries will be ignored and will have no additional effect.</p></div>
<dl className="notes">
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
</div>



</div>
`
}</HTMLBlock>
