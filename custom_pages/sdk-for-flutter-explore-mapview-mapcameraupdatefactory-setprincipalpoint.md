---
title: "setPrincipalPoint static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraupdatefactory-setprincipalpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setPrincipalPoint.html -->


<div>
<h1>setPrincipalPoint static method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>
setPrincipalPoint(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-point2d-class">Point2D</a> principalPoint</li>
</ol>)

      

    

<p>Creates an update to change the map camera's principal point (where the view vector intersects
the image plane - default is the center of the view).</p>
<p>Point values are in screen coordinates
and values that fall outside of the viewport, are clamped.
(0,0) is top left of the viewport.</p>
<ul>
<li><code>principalPoint</code> Principal point in absolute viewport pixel coordinates.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a>. MapCameraUpdate instance.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraUpdate setPrincipalPoint(Point2D principalPoint) =&gt; $prototype.setPrincipalPoint(principalPoint);</code></pre>

 



</div>
`
}</HTMLBlock>
