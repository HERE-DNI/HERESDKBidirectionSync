---
title: "ScheduleDetails constructor"
slug: "sdk-for-flutter-explore-search-scheduledetails-scheduledetails"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ScheduleDetails.html -->


<div>
<h1>ScheduleDetails constructor</h1></div>

ScheduleDetails(<ol class="parameter-list single-line"> <li>String start, </li>
<li>String duration, </li>
<li>String recurrence</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>start</code> Specifies when the iCalendar component begins, for example "T000000" (starts at midnight).</li>
<li><code>duration</code> Specifies a positive duration of time for the iCalendar component, for example "PT24H00M" (lasts 24h).</li>
<li><code>recurrence</code> The recurrence information for a iCalendar component, for example "FREQ:DAILY;BYDAY:MO,TU,WE,TH,FR,SA".</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ScheduleDetails(this.start, this.duration, this.recurrence);</code></pre>

 



</div>
`
}</HTMLBlock>
