---
title: "GeoOrientationUpdate constructor"
slug: "sdk-for-flutter-navigate-core-geoorientationupdate-geoorientationupdate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- GeoOrientationUpdate.html -->


<div>
<h1>GeoOrientationUpdate constructor</h1></div>

GeoOrientationUpdate(<ol class="parameter-list single-line"> <li>double? bearing, </li>
<li>double? tilt</li>
</ol>)
    

<ul>
<li>
<p><code>bearing</code> Bearing in degrees. When the passed value is <code>null</code> bearing is not updated and the current value is kept.
NaN value is converted to <code>null</code>.</p>
</li>
<li>
<p><code>tilt</code> Tilt in degrees. When the passed value is <code>null</code> tilt is not updated and the current value is kept.
NaN value is converted to <code>null</code>.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory GeoOrientationUpdate(double? bearing, double? tilt) =&gt; $prototype.$init(bearing, tilt);</code></pre>

 



</div>
`
}</HTMLBlock>
