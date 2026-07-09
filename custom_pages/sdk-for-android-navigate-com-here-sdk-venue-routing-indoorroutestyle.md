---
title: "IndoorRouteStyle (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- IndoorRouteStyle.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.routing.IndoorRouteStyle</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">IndoorRouteStyle</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a style of the indoor route. Contains information about route colors and widths.
 Optionally, this style allows to set <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instances that can be used for
 specific route elements.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#%3Cinit%3E()">IndoorRouteStyle</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>IndoorRouteStyle</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">IndoorRouteStyle</span>()</div>
<div className="block"><p>Creates a new instance of this class.</p></div>
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
<section className="detail" id="getIndoorMarkerFor(com.here.sdk.routing.IndoorLevelChangeFeatures,int)">
<h3>getIndoorMarkerFor</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span className="element-name">getIndoorMarkerFor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-indoorlevelchangefeatures" title="enum class in com.here.sdk.routing">IndoorLevelChangeFeatures</a> feature,
 int deltaZ)</span></div>
<div className="block"><p>Returns a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> for a given indoor feature and
 the number of levels to change. By default, no map markers are provided.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - <p>An indoor feature.</p></dd>
<dd><code>deltaZ</code> - <p>A number of levels to change, positive for up, negative for down.
     In the case of 0, the method returns an exit map marker.</p></dd>
<dt>Returns:</dt>
<dd><p>The result <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>, if it was set.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setIndoorMarkersFor(com.here.sdk.routing.IndoorLevelChangeFeatures,com.here.sdk.mapview.MapMarker,com.here.sdk.mapview.MapMarker,com.here.sdk.mapview.MapMarker)">
<h3>setIndoorMarkersFor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setIndoorMarkersFor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-indoorlevelchangefeatures" title="enum class in com.here.sdk.routing">IndoorLevelChangeFeatures</a> feature,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> upMarker,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> downMarker,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> exitMarker)</span></div>
<div className="block"><p>Sets map markers for the given indoor feature.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - <p>An indoor feature.</p></dd>
<dd><code>upMarker</code> - <p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> to go up.</p></dd>
<dd><code>downMarker</code> - <p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> to go down.</p></dd>
<dd><code>exitMarker</code> - <p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> to exit the indoor feature.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getIndoorPolylineWidth()">
<h3>getIndoorPolylineWidth</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">getIndoorPolylineWidth</span>()</div>
<div className="block"><p>The width in pixels of polylines for indoor route sections.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The width in pixels. Default value is 15 pixels</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setIndoorPolylineWidth(double)">
<h3>setIndoorPolylineWidth</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setIndoorPolylineWidth</span><wbr/><span className="parameters">(double value)</span></div>
<div className="block"><p>The width in pixels of polylines for indoor route sections.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The width in pixels. Default value is 15 pixels</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getIndoorPolylineColor()">
<h3>getIndoorPolylineColor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span className="element-name">getIndoorPolylineColor</span>()</div>
<div className="block"><p>The color of polylines for indoor route sections.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The color value. The default color is #48DAD0.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setIndoorPolylineColor(com.here.sdk.core.Color)">
<h3>setIndoorPolylineColor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setIndoorPolylineColor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div className="block"><p>The color of polylines for indoor route sections.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The color value. The default color is #48DAD0.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getStartMarker()">
<h3>getStartMarker</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span className="element-name">getStartMarker</span>()</div>
<div className="block"><p>The start map marker of the resulting route.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the start of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setStartMarker(com.here.sdk.mapview.MapMarker)">
<h3>setStartMarker</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setStartMarker</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span></div>
<div className="block"><p>The start map marker of the resulting route.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the start of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDestinationMarker()">
<h3>getDestinationMarker</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span className="element-name">getDestinationMarker</span>()</div>
<div className="block"><p>The destination map marker of the resulting route.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the destination of the route. By default, no map marker is provided</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDestinationMarker(com.here.sdk.mapview.MapMarker)">
<h3>setDestinationMarker</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDestinationMarker</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span></div>
<div className="block"><p>The destination map marker of the resulting route.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the destination of the route. By default, no map marker is provided</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getWalkMarker()">
<h3>getWalkMarker</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span className="element-name">getWalkMarker</span>()</div>
<div className="block"><p>The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the walk point of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setWalkMarker(com.here.sdk.mapview.MapMarker)">
<h3>setWalkMarker</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setWalkMarker</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span></div>
<div className="block"><p>The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the walk point of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDriveMarker()">
<h3>getDriveMarker</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span className="element-name">getDriveMarker</span>()</div>
<div className="block"><p>The drive map marker of the resulting route. It signals that a user should take a transport vehicle.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the drive point of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDriveMarker(com.here.sdk.mapview.MapMarker)">
<h3>setDriveMarker</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDriveMarker</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span></div>
<div className="block"><p>The drive map marker of the resulting route. It signals that a user should take a transport vehicle.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the drive point of the route. By default, no map marker is provided.</p></dd>
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
