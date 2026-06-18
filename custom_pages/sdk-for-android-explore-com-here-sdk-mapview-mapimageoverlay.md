---
title: "MapImageOverlay (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapimageoverlay"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapImageOverlay.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapImageOverlay</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapImageOverlay</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p><code>MapImageOverlay</code> is used to draw images over the map, at a view coordinate inside the map viewport.
 </p><p>The image to be displayed is represented by a <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview"><code>MapImage</code></a> object.
 By default, the overlay is centered on the given view coordinate.
 </p><p>The resulting viewport area covered by the overlay is computed out of the overlay's view coordinate,
 the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.
 </p><p>To display the map overlay, it needs to be added to the scene using <a href="sdk-for-android-explore-mapscene#addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)"><code>MapScene.addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)</code></a>.
 To stop displaying it, remove it from the scene using <a href="sdk-for-android-explore-mapscene#removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)"><code>MapScene.removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)</code></a>.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage)">MapImageOverlay</a><wbr/>(<a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates,
 <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an instance of an overlay at given view coordinates, represented by specified image.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)">MapImageOverlay</a><wbr/>(<a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates,
 <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 <a href="sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates an instance of an overlay at given view coordinates, represented by specified image,
 with anchor point specifying how the image is positioned relative to the overlay's view coordinates.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getAnchor()">getAnchor</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets current anchor point for the overlay image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getDrawOrder()">getDrawOrder</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets draw order of this <code>MapImageOverlay</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getImage()">getImage</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets currently used map image.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#getViewCoordinates()">getViewCoordinates</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the view point in pixels on the map viewport where the overlay is drawn.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setAnchor(com.here.sdk.core.Anchor2D)">setAnchor</a><wbr/>(<a href="sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets anchor point of the overlay image which specifies the position offset relative
 to the overlay's view coordinates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setDrawOrder(int)">setDrawOrder</a><wbr/>(int value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets draw order of this <code>MapImageOverlay</code>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setImage(com.here.sdk.mapview.MapImage)">setImage</a><wbr/>(<a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the image overlayed on map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#setViewCoordinates(com.here.sdk.core.Point2D)">setViewCoordinates</a><wbr/>(<a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the view point in pixels on the map viewport where the overlay is drawn.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage)">
<h3>MapImageOverlay</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapImageOverlay</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates,
 @NonNull
 <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</span></div>
<div class="block"><p>Creates an instance of an overlay at given view coordinates, represented by specified image.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>viewCoordinates</code> - <p>The overlay's view coordinates in pixels.</p></dd>
<dd><code>image</code> - <p>The image to draw on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)">
<h3>MapImageOverlay</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapImageOverlay</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates,
 @NonNull
 <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 @NonNull
 <a href="sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor)</span></div>
<div class="block"><p>Creates an instance of an overlay at given view coordinates, represented by specified image,
 with anchor point specifying how the image is positioned relative to the overlay's view coordinates.
 </p><p>The anchor is a way of specifying position offset relative to image's dimensions on the view.
 For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates.
 (1, 1) would place the bottom-right corner of the image at the overlay's view coordinates.
 (0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.
 </p><p>Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
 centered horizontally with its bottom edge above the overlay's view coordinates at the distance
 in pixels that is equal to the height of the image.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>viewCoordinates</code> - <p>The overlay's view coordinates in pixels.</p></dd>
<dd><code>image</code> - <p>The image to draw on the map.</p></dd>
<dd><code>anchor</code> - <p>The anchor point for the overlay image which specifies the position offset relative
     to the overlay's view coordinates.</p></dd>
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
<section class="detail" id="getViewCoordinates()">
<h3>getViewCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a></span> <span class="element-name">getViewCoordinates</span>()</div>
<div class="block"><p>Gets the view point in pixels on the map viewport where the overlay is drawn.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The view point in pixels on the map viewport where the map overlay is drawn.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setViewCoordinates(com.here.sdk.core.Point2D)">
<h3>setViewCoordinates</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setViewCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-point2d" title="class in com.here.sdk.core">Point2D</a> value)</span></div>
<div class="block"><p>Sets the view point in pixels on the map viewport where the overlay is drawn.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The view point in pixels on the map viewport where the map overlay is drawn.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDrawOrder()">
<h3>getDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDrawOrder</span>()</div>
<div class="block"><p>Gets draw order of this <code>MapImageOverlay</code>. The default value is 0.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Draw order of this <code>MapImageOverlay</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setDrawOrder(int)">
<h3>setDrawOrder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrder</span><wbr/><span class="parameters">(int value)</span></div>
<div class="block"><p>Sets draw order of this <code>MapImageOverlay</code>.
 </p><p>Overlays with higher draw order value are drawn on top of overlays with lower draw order.
 </p><p>In case multiple overlays have the same draw order value
 then the order in which they were added to the scene matters. Last added overlay is drawn on top.
 </p><p>Allowed range is [0, 1023]. Values outside this range will be clamped.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Draw order of this <code>MapImageOverlay</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getImage()">
<h3>getImage</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span class="element-name">getImage</span>()</div>
<div class="block"><p>Gets currently used map image.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Image overlayed on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setImage(com.here.sdk.mapview.MapImage)">
<h3>setImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setImage</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a> value)</span></div>
<div class="block"><p>Sets the image overlayed on map.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Image overlayed on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAnchor()">
<h3>getAnchor</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span class="element-name">getAnchor</span>()</div>
<div class="block"><p>Gets current anchor point for the overlay image.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The anchor point for the overlay image which specifies the position offset relative
     to the overlay's view coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAnchor(com.here.sdk.core.Anchor2D)">
<h3>setAnchor</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAnchor</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span></div>
<div class="block"><p>Sets anchor point of the overlay image which specifies the position offset relative
 to the overlay's view coordinates.
 </p><p>For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates.
 (1, 1) would place the bottom-right corner of the image at the overlay's view coordinates.
 (0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.
 </p><p>Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
 centered horizontally with its bottom edge above the overlay's view coordinates at the distance
 in pixels that is equal to the height of the image.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The anchor point for the overlay image which specifies the position offset relative
     to the overlay's view coordinates.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
