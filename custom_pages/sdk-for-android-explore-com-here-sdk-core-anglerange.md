---
title: "AngleRange (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-anglerange"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- AngleRange.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.AngleRange</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">AngleRange</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents angle ranges as a circular sector by using an absolute start angle
 and a relative range angle called extent. They both define a sector on a
 circle. All angles are in degrees and are clockwise-oriented.
 By default, the AngleRange represents the entire circle, the value is in the range of [0, 360].
 Values will be corrected during construction using normalization
 for the start angle and clamping for the extent angle, ensuring a valid range
 for all possible inputs.</p></div>
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
<div class="col-first even-row-color"><code>final double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#extent">extent</a></code></div>
<div class="col-last even-row-color">
<div class="block">The angle range extent, running clockwise, in degrees from start.</div>
</div>
<div class="col-first odd-row-color"><code>final double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#start">start</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Start angle, running clockwise, in degrees from north.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#%3Cinit%3E()">AngleRange</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a range covering a full circle.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#%3Cinit%3E(double,double)">AngleRange</a><wbr/>(double start,
 double extent)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs an AngleRange from the provided start and extent angles.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#closestInRange(double)">closestInRange</a><wbr/>(double angleClockwiseInDegreesFromNorth)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the angle that is closest to the given one and in range.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>

<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-anglerange" title="class in com.here.sdk.core">AngleRange</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#fromDirectionDegreesClockwise(double,double)">fromDirectionDegreesClockwise</a><wbr/>(double center,
 double extent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs an AngleRange from the provided center angle defining the
 direction and an angular width to extent the range by 50% clockwise and
 50% counter-clockwise from its center angle.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-anglerange" title="class in com.here.sdk.core">AngleRange</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#fromMinMaxDegreesClockwise(double,double)">fromMinMaxDegreesClockwise</a><wbr/>(double min,
 double max)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs an AngleRange from the provided minimum and maximum angles.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#hashCode()">hashCode</a>()</code></div>

<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#inRange(double)">inRange</a><wbr/>(double angleClockwiseInDegreesFromNorth)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Check if a given angle in degrees, clockwise from north is in range or not.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-core-anglerange#max()">max</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the maximum angle defined by the range in degrees, clockwise from north,
 normalized to [0,360).</div>
</div>
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
<section class="detail" id="start">
<h3>start</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">double</span> <span class="element-name">start</span></div>
<div class="block"><p>Start angle, running clockwise, in degrees from north.
 The value is in the range of [0, 360) degrees.</p></div>
</section>
</li>
<li>
<section class="detail" id="extent">
<h3>extent</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">double</span> <span class="element-name">extent</span></div>
<div class="block"><p>The angle range extent, running clockwise, in degrees from start.
 The value is in the range of [0, 360] degrees.</p></div>
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
<section class="detail" id="&lt;init&gt;(double,double)">
<h3>AngleRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AngleRange</span><wbr/><span class="parameters">(double start,
 double extent)</span></div>
<div class="block"><p>Constructs an AngleRange from the provided start and extent angles.
 Corrects values if they exceed the ranges.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>start</code> - <p>Start angle, running clockwise, in degrees from north.
     The value will be normalized to [0.0, 360.0).</p></dd>
<dd><code>extent</code> - <p>The range's extent, running clockwise, in degrees from start.
     The value will be clamped to the range of [0, 360] degrees.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>AngleRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AngleRange</span>()</div>
<div class="block"><p>Constructs a range covering a full circle.</p></div>
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
<li>
<section class="detail" id="fromMinMaxDegreesClockwise(double,double)">
<h3>fromMinMaxDegreesClockwise</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-anglerange" title="class in com.here.sdk.core">AngleRange</a></span> <span class="element-name">fromMinMaxDegreesClockwise</span><wbr/><span class="parameters">(double min,
 double max)</span></div>
<div class="block"><p>Constructs an AngleRange from the provided minimum and maximum angles.
 Corrects values if they exceed the ranges. The angles are always
 interpreted in clockwise orientation.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>min</code> - <p>Angle where to start the circular sector, running clockwise, in
     degrees from north.
     The value will be normalized to [0.0, 360.0).</p></dd>
<dd><code>max</code> - <p>Angle where the circular sector ends, running clockwise, in
     degrees from north.
     The value will be normalized to [0.0, 360.0).</p></dd>
<dt>Returns:</dt>
<dd><p>Created AngleRange from the provided minimum and maximum angles.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fromDirectionDegreesClockwise(double,double)">
<h3>fromDirectionDegreesClockwise</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-anglerange" title="class in com.here.sdk.core">AngleRange</a></span> <span class="element-name">fromDirectionDegreesClockwise</span><wbr/><span class="parameters">(double center,
 double extent)</span></div>
<div class="block"><p>Constructs an AngleRange from the provided center angle defining the
 direction and an angular width to extent the range by 50% clockwise and
 50% counter-clockwise from its center angle.
 Corrects values if they exceed the ranges.
 Example: direction = 90, extent = 10 means the circle sector is pointing
 east, with an extent of 5 degrees north-wards and 5 degrees south-wards.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>center</code> - <p>Start angle, running clockwise, in degrees from north.
     The value will be normalized to [0.0, 360.0).</p></dd>
<dd><code>extent</code> - <p>The range's extent, running clockwise, in degrees from start.
     The value will be clamped to the range of [0, 360] degrees.</p></dd>
<dt>Returns:</dt>
<dd><p>Created AngleRange from the provided center angle and the range's extent.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="inRange(double)">
<h3>inRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">inRange</span><wbr/><span class="parameters">(double angleClockwiseInDegreesFromNorth)</span></div>
<div class="block"><p>Check if a given angle in degrees, clockwise from north is in range or not.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>angleClockwiseInDegreesFromNorth</code> - <p>An angle in degrees from north. Will be normalized before testing.</p></dd>
<dt>Returns:</dt>
<dd><p><code>True</code>, if an angle is in range, <code>false</code> otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="closestInRange(double)">
<h3>closestInRange</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">closestInRange</span><wbr/><span class="parameters">(double angleClockwiseInDegreesFromNorth)</span></div>
<div class="block"><p>Get the angle that is closest to the given one and in range. If the
 angle to both ends of the range is the same, the value in the clockwise
 direction is returned. If the given angle is in range already,
 it will be returned as normalized angle.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>angleClockwiseInDegreesFromNorth</code> - <p>An angle in degrees from north. Will be normalized.</p></dd>
<dt>Returns:</dt>
<dd><p>The closest, normalized in-range angle in degrees, clockwise from north.
     If the given angle is in range already, the given angle will be returned as
     normalized angle in degree, clockwise from north.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="max()">
<h3>max</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">max</span>()</div>
<div class="block"><p>Get the maximum angle defined by the range in degrees, clockwise from north,
 normalized to [0,360).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Maximum angle of the range in degrees, clockwise from north, normalized to
     [0,360).</p></dd>
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
