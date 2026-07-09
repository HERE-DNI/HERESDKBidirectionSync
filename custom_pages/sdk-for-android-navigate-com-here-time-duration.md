---
title: "Duration (API Reference)"
slug: "sdk-for-android-navigate-com-here-time-duration"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Duration.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.time</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.time.Duration</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a>&gt;</code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Duration</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a>&gt;</span></div>
<div className="block">Represents duration in time (both positive and negative).
 <p>
     The duration is represented as number of seconds (see <a href="sdk-for-android-navigate-com-here-time-duration#getSeconds()"><code>getSeconds()</code></a>)
     and number of nanonseconds in a second (see <a href="sdk-for-android-navigate-com-here-time-duration#getNano()"><code>getNano()</code></a>).
 
     Duration can be created from various units of time by calling on of
     <code>of*</code> methods. The <code>to*</code> family of methods convert duration
     to a value expressed in desired unit of time.</p></div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section className="detail" id="getNano()">
<h3>getNano</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getNano</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The nanoseconds component of this duration.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSeconds()">
<h3>getSeconds</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">getSeconds</span>()</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The seconds component of this duration.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ofDays(long)">
<h3>ofDays</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">ofDays</span><wbr/><span className="parameters">(long days)</span>
                       throws <span className="exceptions"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div className="block">Creates a duration representing specified number of days.
 A Day is assumed to always be 24 hours.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>days</code> - The number of days.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of days.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the input is outside the range possible to
                             represent by a Duration</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ofHours(long)">
<h3>ofHours</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">ofHours</span><wbr/><span className="parameters">(long hours)</span>
                        throws <span className="exceptions"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div className="block">Creates a duration representing specified number of hours.
 An hour is assumed to always be 60 minutes.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>hours</code> - The number of hours.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of hours.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the input is outside the range possible to
                             represent by a Duration</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ofMinutes(long)">
<h3>ofMinutes</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">ofMinutes</span><wbr/><span className="parameters">(long minutes)</span>
                          throws <span className="exceptions"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div className="block">Creates a duration representing specified number of hours.
 A minute is assumed to always be 60 seconds.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>minutes</code> - The number of minutes.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of minutes.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the input is outside the range possible to
                             represent by a Duration</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ofSeconds(long)">
<h3>ofSeconds</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">ofSeconds</span><wbr/><span className="parameters">(long seconds)</span></div>
<div className="block">Creates a duration representing specified number of seconds.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>seconds</code> - The number of seconds.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of seconds.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ofSeconds(long,long)">
<h3>ofSeconds</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">ofSeconds</span><wbr/><span className="parameters">(long seconds,
 long nanoAdjustment)</span></div>
<div className="block">Creates a duration representing specified number of seconds and an adjustment in nanoseconds.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>seconds</code> - The number of seconds.</dd>
<dd><code>nanoAdjustment</code> - The nanosecond adjustment to the number of seconds.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of seconds, adjusted.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ofMillis(long)">
<h3>ofMillis</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">ofMillis</span><wbr/><span className="parameters">(long milliseconds)</span></div>
<div className="block">Creates a duration representing specified number of milliseconds.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>milliseconds</code> - The number of milliseconds.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of milliseconds.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="ofNanos(long)">
<h3>ofNanos</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a></span> <span className="element-name">ofNanos</span><wbr/><span className="parameters">(long nanoseconds)</span></div>
<div className="block">Creates a duration representing specified number of nanoseconds.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>nanoseconds</code> - The number of nanoseconds.</dd>
<dt>Returns:</dt>
<dd>The Duration representing the specified number of nanoseconds.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toNanos()">
<h3>toNanos</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">toNanos</span>()
             throws <span className="exceptions"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div className="block">Converts this duration to nanoseconds.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>Total number of nanoseconds in this duration.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the resulting value cannot be represented
                             by <code>long</code> type.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toNanosPart()">
<h3>toNanosPart</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">toNanosPart</span>()</div>
<div className="block">Gets the nanoseconds part of this duration. Equals to <a href="sdk-for-android-navigate-com-here-time-duration#getNano()"><code>getNano()</code></a>.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The nanoseconds part of this duration, value from 0 to 999999999.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toMillis()">
<h3>toMillis</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">toMillis</span>()
              throws <span className="exceptions"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></span></div>
<div className="block">Converts this duration to milliseconds. Any data past milliseconds precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 999999 nanoseconds will still be converted to 0 milliseconds.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>Total number of milliseconds in this duration.</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ArithmeticException.html" title="class or interface in java.lang">ArithmeticException</a></code> - if the resulting value cannot be represented
                             by <code>long</code> type.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toMillisPart()">
<h3>toMillisPart</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">toMillisPart</span>()</div>
<div className="block">Gets the milliseconds part of this duration.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The milliseconds part of this duration.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toSeconds()">
<h3>toSeconds</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">toSeconds</span>()</div>
<div className="block">Converts this duration to seconds. Any data past seconds precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 999 milliseconds will still be converted to 0 seconds.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>Total number of seconds in this duration.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toSecondsPart()">
<h3>toSecondsPart</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">toSecondsPart</span>()</div>
<div className="block">Gets the seconds part of this duration.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The seconds part of this duration, value from 0 to 59.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toMinutes()">
<h3>toMinutes</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">toMinutes</span>()</div>
<div className="block">Converts this duration to minutes. Any data past minute precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 59 seconds and 999 milliseconds will still be converted to 0 minutes.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>Total number of minutes in this duration.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toMinutesPart()">
<h3>toMinutesPart</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">toMinutesPart</span>()</div>
<div className="block">Gets the minutes part of this duration.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The minutes part of this duration, value from 0 to 59.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toHours()">
<h3>toHours</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">toHours</span>()</div>
<div className="block">Converts this duration to hours. Any data past hour precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 59 minutes and 59 seconds will still be converted to 0 hours.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The number of full hours in this duration.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toHoursPart()">
<h3>toHoursPart</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">toHoursPart</span>()</div>
<div className="block">Gets the hours part of this duration.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The hours part of this duration, value from 0 to 23.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toDays()">
<h3>toDays</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">toDays</span>()</div>
<div className="block">Converts this duration to days. Any data past day precision is
 simply discarded. There is no mathematical rounding, so a duration
 of 23 hours 59 minutes and 59 seconds will still be converted to 0 days.
 Day is always assumed to be 24 hours.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The number of full days in this duration.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="toDaysPart()">
<h3>toDaysPart</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">long</span> <span className="element-name">toDaysPart</span>()</div>
<div className="block">Same as <a href="sdk-for-android-navigate-com-here-time-duration#toDays()"><code>toDays()</code></a>.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>The number of full days in this duration.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="compareTo(com.here.time.Duration)">
<h3>compareTo</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">compareTo</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a> duration)</span></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html#compareTo(T)" title="class or interface in java.lang">compareTo</a></code> in interface <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-time-duration" title="class in com.here.time">Duration</a>&gt;</code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> o)</span></div>
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
