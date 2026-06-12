---
title: "LocationTime constructor"
slug: "sdk-for-flutter-explore-core-locationtime-locationtime"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationTime.html -->


<div>
<h1>LocationTime constructor</h1></div>

      const
      LocationTime(<ol class="parameter-list single-line"> <li>DateTime localTime, </li>
<li>DateTime utcTime, </li>
<li>Duration utcOffset</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>localTime</code> The time as observed in the tied location. For example, if a route is requested in Cracow,
Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.</li>
<li><code>utcTime</code> The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland,
the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.</li>
<li><code>utcOffset</code> The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC)
in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is
UTC-05:00, it is -18000.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">const LocationTime(this.localTime, this.utcTime, this.utcOffset);</code></pre>

 



</div>
`
}</HTMLBlock>
