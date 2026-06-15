---
title: "onOffRoadProgressUpdated abstract method"
slug: "sdk-for-flutter-navigate-navigation-offroadprogresslistener-onoffroadprogressupdated"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onOffRoadProgressUpdated.html -->


<div>
<h1>onOffRoadProgressUpdated abstract method</h1></div>

void
onOffRoadProgressUpdated(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-offroadprogress-class">OffRoadProgress</a> offRoadProgress</li>
</ol>)

      

    

<p>Called whenever the current location has been updated and the user is off-road.</p>
<p>Off-road
progress events starts after the user has reached the map-matched destination and the current
location is not map-matched.</p>
<ul>
<li><code>offRoadProgress</code> The current off-road progress update.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onOffRoadProgressUpdated(OffRoadProgress offRoadProgress);</code></pre>

 



</div>
`
}</HTMLBlock>
