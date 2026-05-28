---
title: "Duration (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-time-duration"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Duration.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.time</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.time.Duration</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a>&gt;</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Duration</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a>&gt;</span></div>
<div class="block">Represents duration in time (both positive and negative).
 <p>
     The duration is represented as number of seconds (see <a href="#getSeconds()"><code>getSeconds()</code></a>)
     and number of nanonseconds in a second (see <a href="#getNano()"><code>getNano()</code></a>).
 </p><p>
     Duration can be created from various units of time by calling on of
     <code>of*</code> methods. The <code>to*</code> family of methods convert duration
     to a value expressed in desired unit of time.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#compareTo(com.here.time.Duration)">compareTo</a><wbr/>(<a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNano()">getNano</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSeconds()">getSeconds</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ofDays(long)">ofDays</a><wbr/>(long days)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a duration representing specified number of days.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ofHours(long)">ofHours</a><wbr/>(long hours)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a duration representing specified number of hours.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ofMillis(long)">ofMillis</a><wbr/>(long milliseconds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a duration representing specified number of milliseconds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ofMinutes(long)">ofMinutes</a><wbr/>(long minutes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a duration representing specified number of hours.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ofNanos(long)">ofNanos</a><wbr/>(long nanoseconds)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a duration representing specified number of nanoseconds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ofSeconds(long)">ofSeconds</a><wbr/>(long seconds)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a duration representing specified number of seconds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#ofSeconds(long,long)">ofSeconds</a><wbr/>(long seconds,
 long nanoAdjustment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Creates a duration representing specified number of seconds and an adjustment in nanoseconds.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toDays()">toDays</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Converts this duration to days.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toDaysPart()">toDaysPart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Same as <a href="#toDays()"><code>toDays()</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toHours()">toHours</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Converts this duration to hours.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toHoursPart()">toHoursPart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the hours part of this duration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toMillis()">toMillis</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Converts this duration to milliseconds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toMillisPart()">toMillisPart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the milliseconds part of this duration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toMinutes()">toMinutes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Converts this duration to minutes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toMinutesPart()">toMinutesPart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the minutes part of this duration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toNanos()">toNanos</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Converts this duration to nanoseconds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toNanosPart()">toNanosPart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the nanoseconds part of this duration.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>long</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toSeconds()">toSeconds</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Converts this duration to seconds.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#toSecondsPart()">toSecondsPart</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the seconds part of this duration.</div>
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getNano()">
<h3>getNano</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getNano</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The nanoseconds component of this duration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSeconds()">
<h3>getSeconds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getSeconds</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The seconds component of this duration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ofDays(long)">
<h3>ofDays</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">ofDays</span><wbr/><span class="parameters">(long days)</span>
                       throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div class="block">Creates a duration representing specified number of days.
 A Day is assumed to always be 24 hours.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>days</code> - The number of days.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of days.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the input is outside the range possible to
                             represent by a Duration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ofHours(long)">
<h3>ofHours</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">ofHours</span><wbr/><span class="parameters">(long hours)</span>
                        throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div class="block">Creates a duration representing specified number of hours.
 An hour is assumed to always be 60 minutes.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>hours</code> - The number of hours.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of hours.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the input is outside the range possible to
                             represent by a Duration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ofMinutes(long)">
<h3>ofMinutes</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">ofMinutes</span><wbr/><span class="parameters">(long minutes)</span>
                          throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div class="block">Creates a duration representing specified number of hours.
 A minute is assumed to always be 60 seconds.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>minutes</code> - The number of minutes.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of minutes.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the input is outside the range possible to
                             represent by a Duration</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ofSeconds(long)">
<h3>ofSeconds</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">ofSeconds</span><wbr/><span class="parameters">(long seconds)</span></div>
<div class="block">Creates a duration representing specified number of seconds.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>seconds</code> - The number of seconds.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of seconds.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ofSeconds(long,long)">
<h3>ofSeconds</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">ofSeconds</span><wbr/><span class="parameters">(long seconds,
 long nanoAdjustment)</span></div>
<div class="block">Creates a duration representing specified number of seconds and an adjustment in nanoseconds.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>seconds</code> - The number of seconds.</dd>
<dd><code>nanoAdjustment</code> - The nanosecond adjustment to the number of seconds.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of seconds, adjusted.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ofMillis(long)">
<h3>ofMillis</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">ofMillis</span><wbr/><span class="parameters">(long milliseconds)</span></div>
<div class="block">Creates a duration representing specified number of milliseconds.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>milliseconds</code> - The number of milliseconds.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of milliseconds.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="ofNanos(long)">
<h3>ofNanos</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">ofNanos</span><wbr/><span class="parameters">(long nanoseconds)</span></div>
<div class="block">Creates a duration representing specified number of nanoseconds.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>nanoseconds</code> - The number of nanoseconds.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of nanoseconds.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toNanos()">
<h3>toNanos</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toNanos</span>()
             throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div class="block">Converts this duration to nanoseconds.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Total number of nanoseconds in this duration.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the resulting value cannot be represented
                             by <code>long</code> type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toNanosPart()">
<h3>toNanosPart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toNanosPart</span>()</div>
<div class="block">Gets the nanoseconds part of this duration. Equals to <a href="#getNano()"><code>getNano()</code></a>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The nanoseconds part of this duration, value from 0 to 999999999.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toMillis()">
<h3>toMillis</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toMillis</span>()
              throws <span class="exceptions"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div class="block">Converts this duration to milliseconds. Any data past milliseconds precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 999999 nanoseconds will still be converted to 0 milliseconds.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Total number of milliseconds in this duration.</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the resulting value cannot be represented
                             by <code>long</code> type.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toMillisPart()">
<h3>toMillisPart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toMillisPart</span>()</div>
<div class="block">Gets the milliseconds part of this duration.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The milliseconds part of this duration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toSeconds()">
<h3>toSeconds</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toSeconds</span>()</div>
<div class="block">Converts this duration to seconds. Any data past seconds precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 999 milliseconds will still be converted to 0 seconds.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Total number of seconds in this duration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toSecondsPart()">
<h3>toSecondsPart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toSecondsPart</span>()</div>
<div class="block">Gets the seconds part of this duration.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The seconds part of this duration, value from 0 to 59.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toMinutes()">
<h3>toMinutes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toMinutes</span>()</div>
<div class="block">Converts this duration to minutes. Any data past minute precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 59 seconds and 999 milliseconds will still be converted to 0 minutes.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>Total number of minutes in this duration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toMinutesPart()">
<h3>toMinutesPart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toMinutesPart</span>()</div>
<div class="block">Gets the minutes part of this duration.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The minutes part of this duration, value from 0 to 59.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toHours()">
<h3>toHours</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toHours</span>()</div>
<div class="block">Converts this duration to hours. Any data past hour precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 59 minutes and 59 seconds will still be converted to 0 hours.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The number of full hours in this duration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toHoursPart()">
<h3>toHoursPart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">toHoursPart</span>()</div>
<div class="block">Gets the hours part of this duration.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The hours part of this duration, value from 0 to 23.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toDays()">
<h3>toDays</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toDays</span>()</div>
<div class="block">Converts this duration to days. Any data past day precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 23 hours 59 minutes and 59 seconds will still be converted to 0 days.
 Day is always assumed to be 24 hours.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The number of full days in this duration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="toDaysPart()">
<h3>toDaysPart</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">toDaysPart</span>()</div>
<div class="block">Same as <a href="#toDays()"><code>toDays()</code></a>.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>The number of full days in this duration.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="compareTo(com.here.time.Duration)">
<h3>compareTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">compareTo</span><wbr/><span class="parameters">(<a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code> in interface <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-duration" title="class in com.here.time">Duration</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
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
</div>



</div>
`
}</HTMLBlock>
