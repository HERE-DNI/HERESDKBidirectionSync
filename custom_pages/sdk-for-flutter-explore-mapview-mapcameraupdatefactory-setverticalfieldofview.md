---
title: "setVerticalFieldOfView static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setverticalfieldofview"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setVerticalFieldOfView.html -->


<div>
<h1>setVerticalFieldOfView static method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
setVerticalFieldOfView(<ol class="parameter-list single-line"> <li>double verticalFieldOfView</li>
</ol>)

      

    

<p>Creates an update to change the vertical field of view of the map camera.</p>
<p>If verticalFieldOfView is not finite, no update will be applied to the map camera.</p>
<p>If the verticalFieldOfView is outside [1, 150] interval, it is clamped.</p>
<ul>
<li><code>verticalFieldOfView</code> Vertical field of view in degrees.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate setVerticalFieldOfView(double verticalFieldOfView) =&gt; $prototype.setVerticalFieldOfView(verticalFieldOfView);</code></pre>

 



</div>
`
}</HTMLBlock>
