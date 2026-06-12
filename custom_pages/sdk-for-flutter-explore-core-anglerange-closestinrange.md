---
title: "closestInRange method"
slug: "sdk-for-flutter-explore-core-anglerange-closestinrange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- closestInRange.html -->


<div>
<h1>closestInRange method</h1></div>

double
closestInRange(<ol class="parameter-list single-line"> <li>double angleClockwiseInDegreesFromNorth</li>
</ol>)

      

    

<p>Get the angle that is closest to the given one and in range.</p>
<p>If the
angle to both ends of the range is the same, the value in the clockwise
direction is returned. If the given angle is in range already,
it will be returned as normalized angle.</p>
<ul>
<li><code>angleClockwiseInDegreesFromNorth</code> An angle in degrees from north. Will be normalized.</li>
</ul>
<p>Returns <code>double</code>. The closest, normalized in-range angle in degrees, clockwise from north.</p>
<p>If the given angle is in range already, the given angle will be returned as
normalized angle in degree, clockwise from north.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">double closestInRange(double angleClockwiseInDegreesFromNorth) =&gt; $prototype.closestInRange(this, angleClockwiseInDegreesFromNorth);</code></pre>

 



</div>
`
}</HTMLBlock>
