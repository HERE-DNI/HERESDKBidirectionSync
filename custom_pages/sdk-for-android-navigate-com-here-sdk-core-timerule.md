---
title: "TimeRule (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-timerule"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TimeRule.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.core.TimeRule</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TimeRule</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification.
 For example:
 -*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents:
 March 2nd Sunday 02h:00m for 9 months
 ONLY DURING November 1st Sunday 02h:00m from 9 months ago
 BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00
 The operator * represents reccuring occurrence, <code>+</code> represents a logical OR operation and <code>-</code> represents exclusion meaning, BUT NOT operations.
 This example string represents a time period that meets the following criteria:
 <ul>
<li><code>M3f21h2</code>: M3 denotes third month of the year, i.e. March,
 f2 stands for the second Sunday of the month (as "f" might indicate "first", "second", "third", etc.),
 1 stands for the day of the week (1...7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.</li>
<li><code>{M9}</code>: This denotes "for 9 months", with "M9" standing for nine months. The brackets {} indicate a duration.</li>
<li><code>M11f12h2</code>: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month,
 2 stands for the day of the week (1...7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.</li>
<li>{-M9}: This denotes "9 months ago from the current stated time", with "-M9" standing for nine months in the past.</li>
<li><code>(h15){h2}(h20){h2}</code>: 15:00 to 17:00 OR 20:00 to 22:00
 The brackets {} denotes duration, and the negative sign - represents a past duration.</li>
</ul>
Note: The time period is a logical AND (&amp;&amp;) combination of two components or points in time and it only applies if a point in time is in both components.
 For more advanced examples of <code>TimeRule</code> see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-core-timerule#%3Cinit%3E(java.lang.String,int,java.lang.String)">TimeRule</a><wbr/>(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> timeRule,
 int timeZoneOffsetSeconds,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dstSpec)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(java.lang.String,int,java.lang.String)">
<h3>TimeRule</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TimeRule</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> timeRule,
 int timeZoneOffsetSeconds,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> dstSpec)</span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>timeRule</code> - <p>The time rule as a string in ISO 14825 format.</p></dd>
<dd><code>timeZoneOffsetSeconds</code> - <p>The time zone offset in seconds for the location where the time rule applies.</p></dd>
<dd><code>dstSpec</code> - <p>Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.</p></dd>
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
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> rhs)</span></div>
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
<li>
<section className="detail" id="appliesTo(java.util.Date)">
<h3>appliesTo</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">appliesTo</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Date.html" title="class or interface in java.util">Date</a> dateTime)</span></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>dateTime</code> - <p>date and time that should be used for rule verification.</p></dd>
<dt>Returns:</dt>
<dd><p><code>true</code> if the time domain rules applies to the given date and time., <code>false</code> - otherwise.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTimeRuleString()">
<h3>getTimeRuleString</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getTimeRuleString</span>()</div>
<div className="block"><p>Gets the value of time rule as a string in ISO 14825 format.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The time rule as a string in ISO 14825 format.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTimeZoneOffsetSeconds()">
<h3>getTimeZoneOffsetSeconds</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getTimeZoneOffsetSeconds</span>()</div>
<div className="block"><p>Gets the value of time zone offset in seconds for the location where the time rule applies.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The time zone offset in seconds for the location where the time rule applies.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDstSpec()">
<h3>getDstSpec</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getDstSpec</span>()</div>
<div className="block"><p>Gets the value of day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.</p></dd>
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
