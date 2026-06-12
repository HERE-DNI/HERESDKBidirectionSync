---
title: "setDistanceToTarget abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcamera-setdistancetotarget"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setDistanceToTarget.html -->


<div>
<h1>setDistanceToTarget abstract method</h1></div>

void
setDistanceToTarget(<ol class="parameter-list single-line"> <li>double distanceInMeters</li>
</ol>)

      

    

<p>Makes the camera look at current target from certain distance</p>
<p>This function neither modifies target coordinates nor target orientation.</p>
<ul>
<li><code>distanceInMeters</code> Distance in meters to the target point.
Minimal distance value is clamped to 100 meters.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setDistanceToTarget(double distanceInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
