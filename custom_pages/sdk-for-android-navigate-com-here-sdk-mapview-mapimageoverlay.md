---
title: "MapImageOverlay (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapimageoverlay"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapImageOverlay.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapImageOverlay</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapImageOverlay</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p><code>MapImageOverlay</code> is used to draw images over the map, at a view coordinate inside the map viewport.
 The image to be displayed is represented by a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview"><code>MapImage</code></a> object.
 By default, the overlay is centered on the given view coordinate.
 The resulting viewport area covered by the overlay is computed out of the overlay's view coordinate,
 the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.
 To display the map overlay, it needs to be added to the scene using <a href="sdk-for-android-navigate-mapscene#addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)"><code>MapScene.addMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)</code></a>.
 To stop displaying it, remove it from the scene using <a href="sdk-for-android-navigate-mapscene#removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)"><code>MapScene.removeMapImageOverlay(com.here.sdk.mapview.MapImageOverlay)</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapimageoverlay#%3Cinit%3E(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage)">MapImageOverlay</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an instance of an overlay at given view coordinates, represented by specified image.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapimageoverlay#%3Cinit%3E(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)">MapImageOverlay</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates an instance of an overlay at given view coordinates, represented by specified image,
 with anchor point specifying how the image is positioned relative to the overlay's view coordinates.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage)">
<h3>MapImageOverlay</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapImageOverlay</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image)</span></div>
<div className="block"><p>Creates an instance of an overlay at given view coordinates, represented by specified image.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>viewCoordinates</code> - <p>The overlay's view coordinates in pixels.</p></dd>
<dd><code>image</code> - <p>The image to draw on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.Point2D,com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)">
<h3>MapImageOverlay</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapImageOverlay</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> viewCoordinates,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> image,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> anchor)</span></div>
<div className="block"><p>Creates an instance of an overlay at given view coordinates, represented by specified image,
 with anchor point specifying how the image is positioned relative to the overlay's view coordinates.
 The anchor is a way of specifying position offset relative to image's dimensions on the view.
 For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates.
 (1, 1) would place the bottom-right corner of the image at the overlay's view coordinates.
 (0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.
 Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
 centered horizontally with its bottom edge above the overlay's view coordinates at the distance
 in pixels that is equal to the height of the image.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getViewCoordinates()">
<h3>getViewCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a></span> <span className="element-name">getViewCoordinates</span>()</div>
<div className="block"><p>Gets the view point in pixels on the map viewport where the overlay is drawn.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The view point in pixels on the map viewport where the map overlay is drawn.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setViewCoordinates(com.here.sdk.core.Point2D)">
<h3>setViewCoordinates</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setViewCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-point2d" title="class in com.here.sdk.core">Point2D</a> value)</span></div>
<div className="block"><p>Sets the view point in pixels on the map viewport where the overlay is drawn.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The view point in pixels on the map viewport where the map overlay is drawn.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDrawOrder()">
<h3>getDrawOrder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getDrawOrder</span>()</div>
<div className="block"><p>Gets draw order of this <code>MapImageOverlay</code>. The default value is 0.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Draw order of this <code>MapImageOverlay</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setDrawOrder(int)">
<h3>setDrawOrder</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setDrawOrder</span><wbr/><span className="parameters">(int value)</span></div>
<div className="block"><p>Sets draw order of this <code>MapImageOverlay</code>.
 Overlays with higher draw order value are drawn on top of overlays with lower draw order.
 In case multiple overlays have the same draw order value
 then the order in which they were added to the scene matters. Last added overlay is drawn on top.
 Allowed range is [0, 1023]. Values outside this range will be clamped.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Draw order of this <code>MapImageOverlay</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getImage()">
<h3>getImage</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span className="element-name">getImage</span>()</div>
<div className="block"><p>Gets currently used map image.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Image overlayed on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setImage(com.here.sdk.mapview.MapImage)">
<h3>setImage</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setImage</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a> value)</span></div>
<div className="block"><p>Sets the image overlayed on map.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>Image overlayed on the map.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getAnchor()">
<h3>getAnchor</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span className="element-name">getAnchor</span>()</div>
<div className="block"><p>Gets current anchor point for the overlay image.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The anchor point for the overlay image which specifies the position offset relative
     to the overlay's view coordinates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setAnchor(com.here.sdk.core.Anchor2D)">
<h3>setAnchor</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setAnchor</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span></div>
<div className="block"><p>Sets anchor point of the overlay image which specifies the position offset relative
 to the overlay's view coordinates.
 For example, (0, 0) places the top-left corner of the image at the overlay's view coordinates.
 (1, 1) would place the bottom-right corner of the image at the overlay's view coordinates.
 (0.5, 0.5) which is the default value would center the image at the overlay's view coordinates.
 Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
 centered horizontally with its bottom edge above the overlay's view coordinates at the distance
 in pixels that is equal to the height of the image.</p></div>
<dl className="notes">
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

</div>
</div>



</div>
`
}</HTMLBlock>
