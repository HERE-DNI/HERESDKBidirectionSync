---
title: "MapImageFactory (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapimagefactory"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapImageFactory.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.MapImageFactory</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">MapImageFactory</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">Convenience factory class for loading marker resources from various sources.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapimagefactory#fromBitmap(android.graphics.Bitmap)">fromBitmap</a><wbr/>(android.graphics.Bitmap bitmap)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a map image from a supplied Bitmap.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapimagefactory#fromFile(java.lang.String,int,int)">fromFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath,
 int width,
 int height)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a map image from a specified SVG Tiny or PNG file path.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapimagefactory#fromResource(android.content.res.Resources,int)">fromResource</a><wbr/>(android.content.res.Resources resources,
 int resourceID)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Loads a map image from a specified bitmap resource ID.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="fromResource(android.content.res.Resources,int)">
<h3>fromResource</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span class="element-name">fromResource</span><wbr/><span class="parameters">(android.content.res.Resources resources,
 int resourceID)</span></div>
<div class="block">Loads a map image from a specified bitmap resource ID. As usual on Android,
 the PNG format is preferred. Vector drawables are not supported.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>resources</code> - the application's resources</dd>
<dd><code>resourceID</code> - resource ID for the bitmap image to load</dd>
<dt>Returns:</dt>
<dd>map image representing specified image resource</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fromFile(java.lang.String,int,int)">
<h3>fromFile</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span class="element-name">fromFile</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> filePath,
 int width,
 int height)</span>
                         throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block">Creates a map image from a specified SVG Tiny or PNG file path. Trying to load data not
 compliant to SVG Tiny or PNG might result in undefined behavior. This method needs read
 storage permission to be granted.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>filePath</code> - the path pointing to SVG Tiny file</dd>
<dd><code>width</code> - preferred width</dd>
<dd><code>height</code> - preferred height</dd>
<dt>Returns:</dt>
<dd>map image representing specified image resource</dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - if dimension are invalid or path is empty.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fromBitmap(android.graphics.Bitmap)">
<h3>fromBitmap</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-mapimage" title="class in com.here.sdk.mapview">MapImage</a></span> <span class="element-name">fromBitmap</span><wbr/><span class="parameters">(@NonNull
 android.graphics.Bitmap bitmap)</span></div>
<div class="block">Creates a map image from a supplied Bitmap.</div>
<dl class="notes">
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
`
}</HTMLBlock>
