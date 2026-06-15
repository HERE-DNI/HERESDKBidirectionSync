---
title: "setNormalizedPrincipalPoint static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setnormalizedprincipalpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setNormalizedPrincipalPoint.html -->


<div>
<h1>setNormalizedPrincipalPoint static method</h1></div>

<a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
setNormalizedPrincipalPoint(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-anchor2d-class">Anchor2D</a> principalPoint</li>
</ol>)

      

    

<p>Creates an update to change the map camera's principal point (where the view vector
intersects the image plane - default is (0.5, 0.5)).</p>
<p>Point values are in normalized screen coordinates.</p>
<p>If the principalPoint is outside [0,1] interval, it is clamped.
(0,0) is top left of the viewport, (1,1) is bottom right.</p>
<ul>
<li><code>principalPoint</code> Principal point in normalized screen coordinates.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate setNormalizedPrincipalPoint(Anchor2D principalPoint) =&gt; $prototype.setNormalizedPrincipalPoint(principalPoint);</code></pre>

 



</div>
`
}</HTMLBlock>
