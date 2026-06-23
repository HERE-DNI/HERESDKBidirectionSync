---
title: "SchoolZoneWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarning"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SchoolZoneWarning.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.SchoolZoneWarning</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SchoolZoneWarning</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A school zone warning which notifies about a school zone presence on road with a speed limit
 different than the default speed limit applicable for cars.
 Use <code>SchoolZoneWarningListener</code> to get notifications about school zones.</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#distanceToSchoolZoneInMeters">distanceToSchoolZoneInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The distance from the current location to the school zone in meters.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#distanceType">distanceType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The distance type for the warning, e.g.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#id">id</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unique identifier for this specific school zone warning instance.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#speedLimitInMetersPerSecond">speedLimitInMetersPerSecond</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Speed limit meters/second, which applies to current school zone.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#timeRule">timeRule</a></code></div>
<div class="col-last even-row-color">
<div class="block">Time rule indicating the time periods for which the warning applies.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(double,double,com.here.sdk.navigation.DistanceType)">SchoolZoneWarning</a><wbr/>(double distanceToSchoolZoneInMeters,
 double speedLimitInMetersPerSecond,
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
<section class="detail" id="id">
<h3>id</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">id</span></div>
<div class="block"><p>Unique identifier for this specific school zone warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceToSchoolZoneInMeters">
<h3>distanceToSchoolZoneInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToSchoolZoneInMeters</span></div>
<div class="block"><p>The distance from the current location to the school zone in meters.</p></div>
</section>
</li>
<li>
<section class="detail" id="speedLimitInMetersPerSecond">
<h3>speedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">speedLimitInMetersPerSecond</span></div>
<div class="block"><p>Speed limit meters/second, which applies to current school zone.</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceType">
<h3>distanceType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span class="element-name">distanceType</span></div>
<div class="block"><p>The distance type for the warning, e.g. a warning for a new school zone ahead or a warning
 for passing a school zone.</p></div>
</section>
</li>
<li>
<section class="detail" id="timeRule">
<h3>timeRule</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span class="element-name">timeRule</span></div>
<div class="block"><p>Time rule indicating the time periods for which the warning applies.
 If the field is 'null' then the warning is applicable at anytime.</p></div>
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
<section class="detail" id="&lt;init&gt;(double,double,com.here.sdk.navigation.DistanceType)">
<h3>SchoolZoneWarning</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SchoolZoneWarning</span><wbr/><span class="parameters">(double distanceToSchoolZoneInMeters,
 double speedLimitInMetersPerSecond,
 @NonNull
 <a href="sdk-for-android-navigate-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>distanceToSchoolZoneInMeters</code> - <p>The distance from the current location to the school zone in meters.</p></dd>
<dd><code>speedLimitInMetersPerSecond</code> - <p>Speed limit meters/second, which applies to current school zone.</p></dd>
<dd><code>distanceType</code> - <p>The distance type for the warning, e.g. a warning for a new school zone ahead or a warning
 for passing a school zone.</p></dd>
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
