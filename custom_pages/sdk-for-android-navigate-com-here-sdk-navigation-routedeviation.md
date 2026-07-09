---
title: "RouteDeviation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-routedeviation"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RouteDeviation.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.RouteDeviation</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">RouteDeviation</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Contains all the relevant information on a deviation from the route.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation#currentLocation">currentLocation</a></code></div>
<div className="col-last even-row-color">
<div className="block">The current location.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation#lastLocationOnRoute">lastLocationOnRoute</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The last known location on the route.</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation#lastTraveledSectionIndex">lastTraveledSectionIndex</a></code></div>
<div className="col-last even-row-color">
<div className="block">Indicates the index of the last traveled route section.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation#traveledDistanceOnLastSectionInMeters">traveledDistanceOnLastSectionInMeters</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Offset in meter to the last visited position on the route section defined by the last traveled section index.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation#%3Cinit%3E(com.here.sdk.navigation.NavigableLocation,int,int,com.here.sdk.navigation.NavigableLocation)">RouteDeviation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> lastLocationOnRoute,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> currentLocation)</code></div>
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
<section className="detail" id="lastLocationOnRoute">
<h3>lastLocationOnRoute</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></span> <span className="element-name">lastLocationOnRoute</span></div>
<div className="block"><p>The last known location on the route.</p></div>
</section>
</li>
<li>
<section className="detail" id="lastTraveledSectionIndex">
<h3>lastTraveledSectionIndex</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">lastTraveledSectionIndex</span></div>
<div className="block"><p>Indicates the index of the last traveled route section.</p></div>
</section>
</li>
<li>
<section className="detail" id="traveledDistanceOnLastSectionInMeters">
<h3>traveledDistanceOnLastSectionInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">traveledDistanceOnLastSectionInMeters</span></div>
<div className="block"><p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p></div>
</section>
</li>
<li>
<section className="detail" id="currentLocation">
<h3>currentLocation</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></span> <span className="element-name">currentLocation</span></div>
<div className="block"><p>The current location.</p></div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.navigation.NavigableLocation,int,int,com.here.sdk.navigation.NavigableLocation)">
<h3>RouteDeviation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">RouteDeviation</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> lastLocationOnRoute,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> currentLocation)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>lastLocationOnRoute</code> - <p>The last known location on the route.</p></dd>
<dd><code>lastTraveledSectionIndex</code> - <p>Indicates the index of the last traveled route section.</p></dd>
<dd><code>traveledDistanceOnLastSectionInMeters</code> - <p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p></dd>
<dd><code>currentLocation</code> - <p>The current location.</p></dd>
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
