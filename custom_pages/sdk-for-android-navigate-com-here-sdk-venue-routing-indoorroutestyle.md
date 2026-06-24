---
title: "IndoorRouteStyle (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- IndoorRouteStyle.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.venue.routing.IndoorRouteStyle</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">IndoorRouteStyle</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents a style of the indoor route. Contains information about route colors and widths.
 Optionally, this style allows to set <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instances that can be used for
 specific route elements.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#%3Cinit%3E()">IndoorRouteStyle</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#getDestinationMarker()">getDestinationMarker</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The destination map marker of the resulting route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#getDriveMarker()">getDriveMarker</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The drive map marker of the resulting route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#getIndoorMarkerFor(com.here.sdk.routing.IndoorLevelChangeFeatures,int)">getIndoorMarkerFor</a><wbr/>(<a href="sdk-for-android-navigate-indoorlevelchangefeatures" title="enum class in com.here.sdk.routing">IndoorLevelChangeFeatures</a> feature,
 int deltaZ)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> for a given indoor feature and
 the number of levels to change.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#getIndoorPolylineColor()">getIndoorPolylineColor</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The color of polylines for indoor route sections.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#getIndoorPolylineWidth()">getIndoorPolylineWidth</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The width in pixels of polylines for indoor route sections.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#getStartMarker()">getStartMarker</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The start map marker of the resulting route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#getWalkMarker()">getWalkMarker</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The walk map marker of the resulting route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#setDestinationMarker(com.here.sdk.mapview.MapMarker)">setDestinationMarker</a><wbr/>(<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The destination map marker of the resulting route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#setDriveMarker(com.here.sdk.mapview.MapMarker)">setDriveMarker</a><wbr/>(<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The drive map marker of the resulting route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#setIndoorMarkersFor(com.here.sdk.routing.IndoorLevelChangeFeatures,com.here.sdk.mapview.MapMarker,com.here.sdk.mapview.MapMarker,com.here.sdk.mapview.MapMarker)">setIndoorMarkersFor</a><wbr/>(<a href="sdk-for-android-navigate-indoorlevelchangefeatures" title="enum class in com.here.sdk.routing">IndoorLevelChangeFeatures</a> feature,
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> upMarker,
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> downMarker,
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> exitMarker)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets map markers for the given indoor feature.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#setIndoorPolylineColor(com.here.sdk.core.Color)">setIndoorPolylineColor</a><wbr/>(<a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The color of polylines for indoor route sections.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#setIndoorPolylineWidth(double)">setIndoorPolylineWidth</a><wbr/>(double value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The width in pixels of polylines for indoor route sections.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#setStartMarker(com.here.sdk.mapview.MapMarker)">setStartMarker</a><wbr/>(<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The start map marker of the resulting route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutestyle#setWalkMarker(com.here.sdk.mapview.MapMarker)">setWalkMarker</a><wbr/>(<a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The walk map marker of the resulting route.</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>IndoorRouteStyle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IndoorRouteStyle</span>()</div>
<div class="block"><p>Creates a new instance of this class.</p></div>
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
<section class="detail" id="getIndoorMarkerFor(com.here.sdk.routing.IndoorLevelChangeFeatures,int)">
<h3>getIndoorMarkerFor</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getIndoorMarkerFor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-indoorlevelchangefeatures" title="enum class in com.here.sdk.routing">IndoorLevelChangeFeatures</a> feature,
 int deltaZ)</span></div>
<div class="block"><p>Returns a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> for a given indoor feature and
 the number of levels to change. By default, no map markers are provided.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - <p>An indoor feature.</p></dd>
<dd><code>deltaZ</code> - <p>A number of levels to change, positive for up, negative for down.
     In the case of 0, the method returns an exit map marker.</p></dd>
<dt>Returns:</dt>
<dd><p>The result <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>, if it was set.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIndoorMarkersFor(com.here.sdk.routing.IndoorLevelChangeFeatures,com.here.sdk.mapview.MapMarker,com.here.sdk.mapview.MapMarker,com.here.sdk.mapview.MapMarker)">
<h3>setIndoorMarkersFor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndoorMarkersFor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-indoorlevelchangefeatures" title="enum class in com.here.sdk.routing">IndoorLevelChangeFeatures</a> feature,
 @Nullable
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> upMarker,
 @Nullable
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> downMarker,
 @Nullable
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> exitMarker)</span></div>
<div class="block"><p>Sets map markers for the given indoor feature.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>feature</code> - <p>An indoor feature.</p></dd>
<dd><code>upMarker</code> - <p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> to go up.</p></dd>
<dd><code>downMarker</code> - <p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> to go down.</p></dd>
<dd><code>exitMarker</code> - <p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> to exit the indoor feature.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndoorPolylineWidth()">
<h3>getIndoorPolylineWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getIndoorPolylineWidth</span>()</div>
<div class="block"><p>The width in pixels of polylines for indoor route sections.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The width in pixels. Default value is 15 pixels</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIndoorPolylineWidth(double)">
<h3>setIndoorPolylineWidth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndoorPolylineWidth</span><wbr/><span class="parameters">(double value)</span></div>
<div class="block"><p>The width in pixels of polylines for indoor route sections.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The width in pixels. Default value is 15 pixels</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getIndoorPolylineColor()">
<h3>getIndoorPolylineColor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getIndoorPolylineColor</span>()</div>
<div class="block"><p>The color of polylines for indoor route sections.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The color value. The default color is #48DAD0.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setIndoorPolylineColor(com.here.sdk.core.Color)">
<h3>setIndoorPolylineColor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIndoorPolylineColor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-color" title="class in com.here.sdk.core">Color</a> value)</span></div>
<div class="block"><p>The color of polylines for indoor route sections.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The color value. The default color is #48DAD0.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStartMarker()">
<h3>getStartMarker</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getStartMarker</span>()</div>
<div class="block"><p>The start map marker of the resulting route.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the start of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setStartMarker(com.here.sdk.mapview.MapMarker)">
<h3>setStartMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setStartMarker</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span></div>
<div class="block"><p>The start map marker of the resulting route.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the start of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDestinationMarker()">
<h3>getDestinationMarker</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getDestinationMarker</span>()</div>
<div class="block"><p>The destination map marker of the resulting route.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the destination of the route. By default, no map marker is provided</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDestinationMarker(com.here.sdk.mapview.MapMarker)">
<h3>setDestinationMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDestinationMarker</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span></div>
<div class="block"><p>The destination map marker of the resulting route.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the destination of the route. By default, no map marker is provided</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWalkMarker()">
<h3>getWalkMarker</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getWalkMarker</span>()</div>
<div class="block"><p>The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the walk point of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setWalkMarker(com.here.sdk.mapview.MapMarker)">
<h3>setWalkMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setWalkMarker</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span></div>
<div class="block"><p>The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the walk point of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDriveMarker()">
<h3>getDriveMarker</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a></span> <span class="element-name">getDriveMarker</span>()</div>
<div class="block"><p>The drive map marker of the resulting route. It signals that a user should take a transport vehicle.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the drive point of the route. By default, no map marker is provided.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDriveMarker(com.here.sdk.mapview.MapMarker)">
<h3>setDriveMarker</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDriveMarker</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview">MapMarker</a> value)</span></div>
<div class="block"><p>The drive map marker of the resulting route. It signals that a user should take a transport vehicle.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>A <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a> instance representing the drive point of the route. By default, no map marker is provided.</p></dd>
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
