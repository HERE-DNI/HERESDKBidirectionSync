---
title: "MapSceneLights.Direction (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapSceneLights.Direction.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.MapSceneLights.Direction</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-mapscenelights" title="class in com.here.sdk.mapview">MapSceneLights</a></dd>
</dl>

<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">MapSceneLights.Direction</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>The direction of lights as a pair of azimuth and altitude angles.
 See https://en.wikipedia.org/wiki/Horizontal_coordinate_system</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#altitude">altitude</a></code></div>
<div class="col-last even-row-color">
<div class="block">Direction altitude value in degrees in the range [0, 90].</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#azimuth">azimuth</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Direction azimuth value in degrees in the range [0, 360).</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#%3Cinit%3E()">Direction</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a Direction with default values: azimuth = 0.0, altitude = 0.0.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#%3Cinit%3E(double,double)">Direction</a><wbr/>(double azimuth,
 double altitude)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a Direction from the values.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapscenelights-direction#hashCode()">hashCode</a>()</code></div>

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
<section class="detail" id="azimuth">
<h3>azimuth</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">azimuth</span></div>
<div class="block"><p>Direction azimuth value in degrees in the range [0, 360).
 The default value is 0.0.
 The azimuth range is half-open, meaning the maximum value is not included in the range.
 If the azimuth value falls outside the range, it is wrapped to stay within [0, 360).
 Specifically, values less than 0 will be increased by 360 until they fall within the range,
 and values greater than or equal to 360 will be reduced by 360 until they fall within the range.
 By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise.
 Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.</p></div>
</section>
</li>
<li>
<section class="detail" id="altitude">
<h3>altitude</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">altitude</span></div>
<div class="block"><p>Direction altitude value in degrees in the range [0, 90].
 The default value is 0.0.
 The altitude value is clamped to this range.
 If the value falls outside its supported range, it will be adjusted to stay within the range.
 Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90.
 Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly.
 For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90.
 When both azimuth and altitude values are provided, they are adjusted independently:
 For instance, (0, -10) is changed to (0, 0) rather than (180, 10).</p></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>Direction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Direction</span>()</div>
<div class="block"><p>Constructs a Direction with default values: azimuth = 0.0, altitude = 0.0.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double)">
<h3>Direction</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Direction</span><wbr/><span class="parameters">(double azimuth,
 double altitude)</span></div>
<div class="block"><p>Constructs a Direction from the values.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>azimuth</code> - <p>Direction azimuth value in degrees in the range [0, 360).
 The default value is 0.0.
 The azimuth range is half-open, meaning the maximum value is not included in the range.
 If the azimuth value falls outside the range, it is wrapped to stay within [0, 360).
 Specifically, values less than 0 will be increased by 360 until they fall within the range,
 and values greater than or equal to 360 will be reduced by 360 until they fall within the range.
 By convention, an azimuth of 0 degrees corresponds to North, and azimuth values increase clockwise.
 Thus, 90 degrees corresponds to East, 180 degrees to South, and 270 degrees to West.</p></dd>
<dd><code>altitude</code> - <p>Direction altitude value in degrees in the range [0, 90].
 The default value is 0.0.
 The altitude value is clamped to this range.
 If the value falls outside its supported range, it will be adjusted to stay within the range.
 Specifically, values less than 0 will be set to 0, and values greater than 90 will be set to 90.
 Note: Unlike azimuth, altitude values are not wrapped around; they are clamped directly.
 For example, an altitude value of -10 will be adjusted to 0, and an altitude value of 100 will be adjusted to 90.
 When both azimuth and altitude values are provided, they are adjusted independently:
 For instance, (0, -10) is changed to (0, 0) rather than (180, 10).</p></dd>
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
