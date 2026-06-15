---
title: "TimeRule class abstract"
slug: "sdk-for-flutter-navigate-core-timerule-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TimeRule-class.html -->


<div>
<h1>TimeRule class abstract</h1></div>

<p>Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification.</p>
<p>For example:
-*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents:
March 2nd Sunday 02h:00m for 9 months
ONLY DURING November 1st Sunday 02h:00m from 9 months ago
BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00</p>
<p>The operator * represents reccuring occurrence, <code>+</code> represents a logical OR operation and <code>-</code> represents exclusion meaning, BUT NOT operations.</p>
<p>This example string represents a time period that meets the following criteria:</p>
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
<p>Note: The time period is a logical AND (&amp;&amp;) combination of two components or points in time and it only applies if a point in time is in both components.</p>
<p>For more advanced examples of <code>TimeRule</code> see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.</p>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-timerule-timerule">TimeRule</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-timerule-dstspec">dstSpec</a></li><li><a href="sdk-for-flutter-navigate-core-timerule-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-core-timerule-runtimetype">runtimeType</a></li><li><a href="sdk-for-flutter-navigate-core-timerule-timerulestring">timeRuleString</a></li><li><a href="sdk-for-flutter-navigate-core-timerule-timezoneoffsetseconds">timeZoneOffsetSeconds</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-timerule-appliesto">appliesTo</a></li><li><a href="sdk-for-flutter-navigate-core-timerule-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-core-timerule-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-core-timerule-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
