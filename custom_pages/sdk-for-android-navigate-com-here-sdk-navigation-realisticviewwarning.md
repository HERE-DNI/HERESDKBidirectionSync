---
title: "RealisticViewWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RealisticViewWarning.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.RealisticViewWarning</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RealisticViewWarning</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A realistic view notification. This notification is given for complex junctions and it includes a visual
 representation of that junction, in order to help the user to better navigate it. When
 <a href="sdk-for-android-navigate-index#distanceType"><code>distanceType</code></a> is <a href="sdk-for-android-navigate-distancetype#AHEAD"><code>DistanceType.AHEAD</code></a>, the <a href="sdk-for-android-navigate-index#realisticViewVectorImage"><code>realisticViewVectorImage</code></a> object
 will be provided with the junction view and the signpost representations. For <a href="sdk-for-android-navigate-index#distanceType"><code>distanceType</code></a>
 with value <a href="sdk-for-android-navigate-distancetype#PASSED"><code>DistanceType.PASSED</code></a>, the <a href="sdk-for-android-navigate-index#realisticViewVectorImage"><code>realisticViewVectorImage</code></a> object will be null.
 Use <code>RealisticViewWarningListener</code> to get notifications about the realistic views of the upcoming junctions.
 </p><p>Realistic view notifications require an online connection in order to function properly, or that the
 junction or signpost map layer data is cached, installed or preloaded as part of a <code>Region</code>.
 This can be enabled via feature configurations.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#distanceToRealisticViewInMeters">distanceToRealisticViewInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Distance to the junction, for which the realistic view is given, expressed in meters.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#distanceType">distanceType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The distance type for the warning, e.g.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#id">id</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unique identifier for this specific realistic view warning instance.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-realisticviewrasterimage" title="class in com.here.sdk.navigation">RealisticViewRasterImage</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#realisticViewRasterImage">realisticViewRasterImage</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The realistic view object for which the warning is given.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-realisticviewvectorimage" title="class in com.here.sdk.navigation">RealisticViewVectorImage</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#realisticViewVectorImage">realisticViewVectorImage</a></code></div>
<div class="col-last even-row-color">
<div class="block">The realistic view object for which the warning is given.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(double,com.here.sdk.navigation.DistanceType)">RealisticViewWarning</a><wbr/>(double distanceToRealisticViewInMeters,
 <a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="id">
<h3>id</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">id</span></div>
<div class="block"><p>Unique identifier for this specific realistic view warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceToRealisticViewInMeters">
<h3>distanceToRealisticViewInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToRealisticViewInMeters</span></div>
<div class="block"><p>Distance to the junction, for which the realistic view is given, expressed in meters.</p></div>
</section>
</li>
<li>
<section class="detail" id="realisticViewVectorImage">
<h3>realisticViewVectorImage</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-realisticviewvectorimage" title="class in com.here.sdk.navigation">RealisticViewVectorImage</a></span> <span class="element-name">realisticViewVectorImage</span></div>
<div class="block"><p>The realistic view object for which the warning is given.
 Image resources are stored as vector graphics.
 Within <a href="sdk-for-android-navigate-realisticviewwarning" title="class in com.here.sdk.navigation"><code>RealisticViewWarning</code></a>, only one type of image, either raster or vector, will be provided.
 If this property is not <code>null</code>, then <a href="sdk-for-android-navigate-index#realisticViewRasterImage"><code>realisticViewRasterImage</code></a> will be <code>null</code>.
 </p><p><strong>Note:</strong> The realistic views for most of the countries are stored as vector images.</p></div>
</section>
</li>
<li>
<section class="detail" id="realisticViewRasterImage">
<h3>realisticViewRasterImage</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-realisticviewrasterimage" title="class in com.here.sdk.navigation">RealisticViewRasterImage</a></span> <span class="element-name">realisticViewRasterImage</span></div>
<div class="block"><p>The realistic view object for which the warning is given.
 Image resources are stored as raster graphics.
 Within <a href="sdk-for-android-navigate-realisticviewwarning" title="class in com.here.sdk.navigation"><code>RealisticViewWarning</code></a>, only one type of image, either raster or vector, will be provided.
 If this property is not <code>null</code>, then <a href="sdk-for-android-navigate-index#realisticViewVectorImage"><code>realisticViewVectorImage</code></a> will be <code>null</code>.
 <strong>Note:</strong> Certain countries support only raster images as realistic views. Currently, this is the case
 only for Japan, but in the future, more countries might support this type of realistic views.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceType">
<h3>distanceType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span class="element-name">distanceType</span></div>
<div class="block"><p>The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning
 for passing a realistic view. Since the realistic view warning is given relative to a single
 position on the route, <a href="sdk-for-android-navigate-distancetype#REACHED"><code>DistanceType.REACHED</code></a> will never be given for this warning.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.DistanceType)">
<h3>RealisticViewWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RealisticViewWarning</span><wbr/><span class="parameters">(double distanceToRealisticViewInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>distanceToRealisticViewInMeters</code> - <p>Distance to the junction, for which the realistic view is given, expressed in meters.</p></dd>
<dd><code>distanceType</code> - <p>The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning
 for passing a realistic view. Since the realistic view warning is given relative to a single
 position on the route, <a href="sdk-for-android-navigate-distancetype#REACHED"><code>DistanceType.REACHED</code></a> will never be given for this warning.</p></dd>
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
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
