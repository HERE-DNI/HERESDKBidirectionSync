---
title: "RealisticViewWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RealisticViewWarning.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.RealisticViewWarning</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RealisticViewWarning</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A realistic view notification. This notification is given for complex junctions and it includes a visual
 representation of that junction, in order to help the user to better navigate it. When
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#distanceType"><code>distanceType</code></a> is <a href="sdk-for-android-navigate-distancetype#AHEAD"><code>DistanceType.AHEAD</code></a>, the <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#realisticViewVectorImage"><code>realisticViewVectorImage</code></a> object
 will be provided with the junction view and the signpost representations. For <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#distanceType"><code>distanceType</code></a>
 with value <a href="sdk-for-android-navigate-distancetype#PASSED"><code>DistanceType.PASSED</code></a>, the <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#realisticViewVectorImage"><code>realisticViewVectorImage</code></a> object will be null.
 Use <code>RealisticViewWarningListener</code> to get notifications about the realistic views of the upcoming junctions.
 Realistic view notifications require an online connection in order to function properly, or that the
 junction or signpost map layer data is cached, installed or preloaded as part of a <code>Region</code>.
 This can be enabled via feature configurations.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#distanceToRealisticViewInMeters">distanceToRealisticViewInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">Distance to the junction, for which the realistic view is given, expressed in meters.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#distanceType">distanceType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The distance type for the warning, e.g.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#id">id</a></code></div>
<div className="col-last even-row-color">
<div className="block">Unique identifier for this specific realistic view warning instance.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewrasterimage" title="class in com.here.sdk.navigation">RealisticViewRasterImage</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#realisticViewRasterImage">realisticViewRasterImage</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The realistic view object for which the warning is given.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewvectorimage" title="class in com.here.sdk.navigation">RealisticViewVectorImage</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#realisticViewVectorImage">realisticViewVectorImage</a></code></div>
<div className="col-last even-row-color">
<div className="block">The realistic view object for which the warning is given.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#%3Cinit%3E(double,com.here.sdk.navigation.DistanceType)">RealisticViewWarning</a><wbr/>(double distanceToRealisticViewInMeters,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="id">
<h3>id</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">id</span></div>
<div className="block"><p>Unique identifier for this specific realistic view warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceToRealisticViewInMeters">
<h3>distanceToRealisticViewInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">distanceToRealisticViewInMeters</span></div>
<div className="block"><p>Distance to the junction, for which the realistic view is given, expressed in meters.</p></div>
</section>
</li>
<li>
<section className="detail" id="realisticViewVectorImage">
<h3>realisticViewVectorImage</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewvectorimage" title="class in com.here.sdk.navigation">RealisticViewVectorImage</a></span> <span className="element-name">realisticViewVectorImage</span></div>
<div className="block"><p>The realistic view object for which the warning is given.
 Image resources are stored as vector graphics.
 Within <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation"><code>RealisticViewWarning</code></a>, only one type of image, either raster or vector, will be provided.
 If this property is not <code>null</code>, then <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#realisticViewRasterImage"><code>realisticViewRasterImage</code></a> will be <code>null</code>.
 <strong>Note:</strong> The realistic views for most of the countries are stored as vector images.</p></div>
</section>
</li>
<li>
<section className="detail" id="realisticViewRasterImage">
<h3>realisticViewRasterImage</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewrasterimage" title="class in com.here.sdk.navigation">RealisticViewRasterImage</a></span> <span className="element-name">realisticViewRasterImage</span></div>
<div className="block"><p>The realistic view object for which the warning is given.
 Image resources are stored as raster graphics.
 Within <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation"><code>RealisticViewWarning</code></a>, only one type of image, either raster or vector, will be provided.
 If this property is not <code>null</code>, then <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning#realisticViewVectorImage"><code>realisticViewVectorImage</code></a> will be <code>null</code>.
 <strong>Note:</strong> Certain countries support only raster images as realistic views. Currently, this is the case
 only for Japan, but in the future, more countries might support this type of realistic views.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceType">
<h3>distanceType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span className="element-name">distanceType</span></div>
<div className="block"><p>The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning
 for passing a realistic view. Since the realistic view warning is given relative to a single
 position on the route, <a href="sdk-for-android-navigate-distancetype#REACHED"><code>DistanceType.REACHED</code></a> will never be given for this warning.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.DistanceType)">
<h3>RealisticViewWarning</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RealisticViewWarning</span><wbr/><span className="parameters">(double distanceToRealisticViewInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
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
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
