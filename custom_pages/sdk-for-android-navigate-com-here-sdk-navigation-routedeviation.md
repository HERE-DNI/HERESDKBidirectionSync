---
title: "RouteDeviation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-routedeviation"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RouteDeviation.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.RouteDeviation</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RouteDeviation</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Contains all the relevant information on a deviation from the route.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#currentLocation">currentLocation</a></code></div>
<div class="col-last even-row-color">
<div class="block">The current location.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#lastLocationOnRoute">lastLocationOnRoute</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The last known location on the route.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#lastTraveledSectionIndex">lastTraveledSectionIndex</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates the index of the last traveled route section.</div>
</div>
<div class="col-first odd-row-color"><code>int</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#traveledDistanceOnLastSectionInMeters">traveledDistanceOnLastSectionInMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Offset in meter to the last visited position on the route section defined by the last traveled section index.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.navigation.NavigableLocation,int,int,com.here.sdk.navigation.NavigableLocation)">RouteDeviation</a><wbr/>(<a href="sdk-for-android-navigate-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> lastLocationOnRoute,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 <a href="sdk-for-android-navigate-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> currentLocation)</code></div>
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

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="lastLocationOnRoute">
<h3>lastLocationOnRoute</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></span> <span class="element-name">lastLocationOnRoute</span></div>
<div class="block"><p>The last known location on the route.</p></div>
</section>
</li>
<li>
<section class="detail" id="lastTraveledSectionIndex">
<h3>lastTraveledSectionIndex</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">lastTraveledSectionIndex</span></div>
<div class="block"><p>Indicates the index of the last traveled route section.</p></div>
</section>
</li>
<li>
<section class="detail" id="traveledDistanceOnLastSectionInMeters">
<h3>traveledDistanceOnLastSectionInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">traveledDistanceOnLastSectionInMeters</span></div>
<div class="block"><p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p></div>
</section>
</li>
<li>
<section class="detail" id="currentLocation">
<h3>currentLocation</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a></span> <span class="element-name">currentLocation</span></div>
<div class="block"><p>The current location.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.navigation.NavigableLocation,int,int,com.here.sdk.navigation.NavigableLocation)">
<h3>RouteDeviation</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RouteDeviation</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> lastLocationOnRoute,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-navigablelocation" title="class in com.here.sdk.navigation">NavigableLocation</a> currentLocation)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
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






</div>
`
}</HTMLBlock>
