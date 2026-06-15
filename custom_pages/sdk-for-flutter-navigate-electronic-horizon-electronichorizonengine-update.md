---
title: "update abstract method"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-update"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- update.html -->


<div>
<h1>update abstract method</h1></div>

void
update(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a> mapMatchedLocation</li>
</ol>)

      

    

<p>Updates the electronic horizon paths based on the provided map-matched location.</p>
<p>This method returns immediately and does not block.
When internal calculation is complete, callbacks are called on the main thread.
When multiple updates are triggered while processing is still running,
intermediate locations are skipped and only the last location is processed.</p>
<ul>
<li><code>mapMatchedLocation</code> The map-matched location that defines the current vehicle position on the road network.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void update(MapMatchedLocation mapMatchedLocation);</code></pre>

 



</div>
`
}</HTMLBlock>
