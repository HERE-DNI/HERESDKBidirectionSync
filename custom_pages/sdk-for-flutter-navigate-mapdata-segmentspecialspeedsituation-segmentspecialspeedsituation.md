---
title: "SegmentSpecialSpeedSituation constructor"
slug: "sdk-for-flutter-navigate-mapdata-segmentspecialspeedsituation-segmentspecialspeedsituation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentSpecialSpeedSituation.html -->


<div>
<h1>SegmentSpecialSpeedSituation constructor</h1></div>

SegmentSpecialSpeedSituation(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapdata-specialspeedtype">SpecialSpeedType</a> specialSpeedType, </li>
<li>double speedLimitInMetersPerSecond, </li>
<li>List&lt;<a href="/sdk-for-flutter-navigate-core-timerule-class">TimeRule</a>&gt; appliesDuring</li>
</ol>)
    

<p>Creates a new instance with default values.</p>
<ul>
<li><code>specialSpeedType</code> Represents the speed situation type.</li>
<li><code>speedLimitInMetersPerSecond</code> Overrides normal speed limit for this situation.</li>
</ul>
<p>May be 0 to indicate no special speed limit in the case of special_speed_type = SPEED_BUMPS_PRESENT
and special_speed_type = LANE_DEPENDENT.
Speed limit in meter per seconds.</p>
<ul>
<li><code>appliesDuring</code> The times during which the condition applies.
May be empty for all special_speed_type values except <code>TIME_DEPENDENT</code> and <code>APPROXIMATE_SEASONAL_TIME</code>.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SegmentSpecialSpeedSituation(this.specialSpeedType, this.speedLimitInMetersPerSecond, this.appliesDuring);</code></pre>

 



</div>
`
}</HTMLBlock>
