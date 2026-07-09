---
title: "MapImageFactory (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapimagefactory"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapImageFactory.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.MapImageFactory</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public class </span><span className="element-name type-name-label">MapImageFactory</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block">Convenience factory class for loading marker resources from various sources.</div>
</section>
<section className="summary">
<ul className="summary-list">
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="fromResource(android.content.res.Resources,int)">
<h3>fromResource</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span className="element-name">fromResource</span><wbr/><span className="parameters">(android.content.res.Resources resources,
 int resourceID)</span></div>
<div className="block">Loads a map image from a specified bitmap resource ID. As usual on Android,
 the PNG format is preferred. Vector drawables are not supported.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>resources</code> - the application's resources</dd>
<dd><code>resourceID</code> - resource ID for the bitmap image to load</dd>
<dt>Returns:</dt>
<dd>map image representing specified image resource</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="fromFile(java.lang.String,int,int)">
<h3>fromFile</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span className="element-name">fromFile</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath,
 int width,
 int height)</span>
                         throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block">Creates a map image from a specified SVG Tiny or PNG file path. Trying to load data not
 compliant to SVG Tiny or PNG might result in undefined behavior. This method needs read
 storage permission to be granted.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>filePath</code> - the path pointing to SVG Tiny file</dd>
<dd><code>width</code> - preferred width</dd>
<dd><code>height</code> - preferred height</dd>
<dt>Returns:</dt>
<dd>map image representing specified image resource</dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - if dimension are invalid or path is empty.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="fromBitmap(android.graphics.Bitmap)">
<h3>fromBitmap</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span className="element-name">fromBitmap</span><wbr/><span className="parameters">(@NonNull
 android.graphics.Bitmap bitmap)</span></div>
<div className="block">Creates a map image from a supplied Bitmap.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>bitmap</code> - the bitmap image to use for creating the marker resource</dd>
<dt>Returns:</dt>
<dd>map image representing specified image resource</dd>
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
