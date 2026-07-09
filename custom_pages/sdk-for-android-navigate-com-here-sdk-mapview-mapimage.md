---
title: "MapImage (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapimage"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapImage.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapImage</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapImage</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Represents a drawable resource that can be used by a <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker" title="class in com.here.sdk.mapview"><code>MapMarker</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmarker3d" title="class in com.here.sdk.mapview"><code>MapMarker3D</code></a> or <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimageoverlay" title="class in com.here.sdk.mapview"><code>MapImageOverlay</code></a> to be shown on the map.
 Supported formats are listed in <a href="sdk-for-android-navigate-com-here-sdk-mapview-imageformat" title="enum class in com.here.sdk.mapview"><code>ImageFormat</code></a>.
 SVG format allows custom fonts in text using font-family attribute by prior registration via <code>AssetsManager.registerFont</code>.
 It is recommended to associate a resource with a single <code>MapImage</code> instance in order to enable
 resource sharing and reduce the amount of needed memory.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat)">MapImage</a><wbr/>(byte[] pixelData,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-imageformat" title="enum class in com.here.sdk.mapview">ImageFormat</a> imageFormat)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new map image from the provided image data.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat,long,long)">MapImage</a><wbr/>(byte[] imageData,
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-imageformat" title="enum class in com.here.sdk.mapview">ImageFormat</a> imageFormat,
 long width,
 long height)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new map image from the provided image data.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage#%3Cinit%3E(java.lang.String,long,long)">MapImage</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath,
 long width,
 long height)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new map image from the provided path to the SVG Tiny or PNG image.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

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
<section className="detail" id="&lt;init&gt;(byte[],com.here.sdk.mapview.ImageFormat)">
<h3>MapImage</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapImage</span><wbr/><span className="parameters">(@NonNull
 byte[] pixelData,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-imageformat" title="enum class in com.here.sdk.mapview">ImageFormat</a> imageFormat)</span></div>
<div className="block"><p>Creates a new map image from the provided image data. Currently only <a href="sdk-for-android-navigate-imageformat#PNG"><code>ImageFormat.PNG</code></a>
 is accepted.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>pixelData</code> - <p>Data to be used for the image. The bytes of a PNG image datastream are expected as
     defined in https://www.w3.org/TR/PNG</p></dd>
<dd><code>imageFormat</code> - <p>The format of the image data to be used.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(byte[],com.here.sdk.mapview.ImageFormat,long,long)">
<h3>MapImage</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapImage</span><wbr/><span className="parameters">(@NonNull
 byte[] imageData,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-imageformat" title="enum class in com.here.sdk.mapview">ImageFormat</a> imageFormat,
 long width,
 long height)</span></div>
<div className="block"><p>Creates a new map image from the provided image data.</p></div>
<dl className="notes">
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
<section className="detail" id="&lt;init&gt;(java.lang.String,long,long)">
<h3>MapImage</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MapImage</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath,
 long width,
 long height)</span>
         throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new map image from the provided path to the SVG Tiny or PNG image.
 Will throw an error if either the height or width equals zero or the path is empty.
 Trying to load a file that is not compliant with SVG Tiny or PNG results
 in an undefined behavior. In particular, loading SVG that exceeds Tiny SVG
 specification may result in an image that exhibits unexpected artifacts.
 The caller must ensure that the file remains accessible for the entire duration of its usage by the
 SDK. If that cannot be ensured, then it is recommended to either copy the file to a location that
 remains accessible for the entire duration of its usage by the SDK or load and pass the file content
 to one of the <code>MapImage</code> constructors that creates instances out of image data
 (<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat)"><code>MapImage(byte[], ImageFormat)</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage#%3Cinit%3E(byte%5B%5D,com.here.sdk.mapview.ImageFormat,long,long)"><code>MapImage(byte[], ImageFormat, long, long)</code></a>).}
 This constructor needs read storage permission to be granted.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>filePath</code> - <p>The path to image file.</p></dd>
<dd><code>width</code> - <p>The width of image in pixels.</p></dd>
<dd><code>height</code> - <p>The height of image in pixels.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
