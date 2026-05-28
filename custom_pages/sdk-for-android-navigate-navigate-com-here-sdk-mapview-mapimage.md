---
title: "MapImage (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-mapview-mapimage"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapImage.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
<li>Method</li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-..-..-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapImage</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapImage</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-..-..-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Represents a drawable resource that can be used by a <a href="sdk-for-android-navigate-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>, <a href="sdk-for-android-navigate-mapmarker3d" title="class in com.here.sdk.mapview"><code>MapMarker3D</code></a> or <a href="sdk-for-android-navigate-mapimageoverlay" title="class in com.here.sdk.mapview"><code>MapImageOverlay</code></a> to be shown on the map.
 Supported formats are listed in <a href="sdk-for-android-navigate-imageformat" title="enum class in com.here.sdk.mapview"><code>ImageFormat</code></a>.
 SVG format allows custom fonts in text using font-family attribute by prior registration via <code>AssetsManager.registerFont</code>.
 </p><p>It is recommended to associate a resource with a single <code>MapImage</code> instance in order to enable
 resource sharing and reduce the amount of needed memory.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat)">MapImage</a><wbr/>(byte[] pixelData,
 <a href="sdk-for-android-navigate-imageformat" title="enum class in com.here.sdk.mapview">ImageFormat</a> imageFormat)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new map image from the provided image data.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat,long,long)">MapImage</a><wbr/>(byte[] imageData,
 <a href="sdk-for-android-navigate-imageformat" title="enum class in com.here.sdk.mapview">ImageFormat</a> imageFormat,
 long width,
 long height)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new map image from the provided image data.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.lang.String,long,long)">MapImage</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath,
 long width,
 long height)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new map image from the provided path to the SVG Tiny or PNG image.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

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
<section class="detail" id="&lt;init&gt;(byte[],com.here.sdk.mapview.ImageFormat)">
<h3>MapImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapImage</span><wbr/><span class="parameters">(@NonNull
 byte[] pixelData,
 @NonNull
 <a href="sdk-for-android-navigate-imageformat" title="enum class in com.here.sdk.mapview">ImageFormat</a> imageFormat)</span></div>
<div class="block"><p>Creates a new map image from the provided image data. Currently only <a href="sdk-for-android-navigate-imageformat#PNG"><code>ImageFormat.PNG</code></a>
 is accepted.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pixelData</code> - <p>Data to be used for the image. The bytes of a PNG image datastream are expected as
     defined in https://www.w3.org/TR/PNG</p></dd>
<dd><code>imageFormat</code> - <p>The format of the image data to be used.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(byte[],com.here.sdk.mapview.ImageFormat,long,long)">
<h3>MapImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapImage</span><wbr/><span class="parameters">(@NonNull
 byte[] imageData,
 @NonNull
 <a href="sdk-for-android-navigate-imageformat" title="enum class in com.here.sdk.mapview">ImageFormat</a> imageFormat,
 long width,
 long height)</span></div>
<div class="block"><p>Creates a new map image from the provided image data.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>imageData</code> - <p>Data to be used for the image. For image format <a href="sdk-for-android-navigate-imageformat#SVG"><code>ImageFormat.SVG</code></a> the bytes
     of a UTF-8 encoded string in SVG Tiny format are expected. For the format specification
     see https://www.w3.org/TR/SVGTiny12</p></dd>
<dd><code>imageFormat</code> - <p>The format of the image data to be used.</p></dd>
<dd><code>width</code> - <p>The width of the image in pixels.</p></dd>
<dd><code>height</code> - <p>The height of the image in pixels.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(java.lang.String,long,long)">
<h3>MapImage</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">MapImage</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath,
 long width,
 long height)</span>
         throws <span class="exceptions"><a href="sdk-for-android-navigate-..-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new map image from the provided path to the SVG Tiny or PNG image.
 </p><p>Will throw an error if either the height or width equals zero or the path is empty.
 </p><p>Trying to load a file that is not compliant with SVG Tiny or PNG results
 in an undefined behavior. In particular, loading SVG that exceeds Tiny SVG
 specification may result in an image that exhibits unexpected artifacts.
 </p><p>The caller must ensure that the file remains accessible for the entire duration of its usage by the
 SDK. If that cannot be ensured, then it is recommended to either copy the file to a location that
 remains accessible for the entire duration of its usage by the SDK or load and pass the file content
 to one of the <code>MapImage</code> constructors that creates instances out of image data
 (<a href="#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat)"><code>MapImage(byte[], ImageFormat)</code></a>, <a href="#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat,long,long)"><code>MapImage(byte[], ImageFormat, long, long)</code></a>).}
 </p><p>This constructor needs read storage permission to be granted.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filePath</code> - <p>The path to image file.</p></dd>
<dd><code>width</code> - <p>The width of image in pixels.</p></dd>
<dd><code>height</code> - <p>The height of image in pixels.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-..-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
</div>



</div>
`
}</HTMLBlock>
