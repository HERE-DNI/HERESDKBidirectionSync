---
title: "timeZoneOffsetsInMinutes property"
slug: "sdk-for-flutter-navigate-mapdata-administrativerules-timezoneoffsetsinminutes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- timeZoneOffsetsInMinutes.html -->


<div>
<h1>timeZoneOffsetsInMinutes property</h1></div>

        
        List&lt;Duration&gt;
timeZoneOffsetsInMinutes
<div class="features">getter/setter pair</div>


<p>The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative
(e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes).
Defaults to 0 minutes.
<strong>Note:</strong> A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of
90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset
of -210 minutes. In order to properly calculate the time zone offset, the <code>AdministrativeRules.daylight_saving_period</code>
should be taken into consideration and if the daylight savings time is observed at the time of the
calculation, then a value of 60 minutes should be substracted from the time zone offset.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;Duration&gt; timeZoneOffsetsInMinutes;</code></pre>

 



</div>
`
}</HTMLBlock>
