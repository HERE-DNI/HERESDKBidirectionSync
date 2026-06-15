---
title: "fromDirectionDegreesClockwise static method"
slug: "sdk-for-flutter-explore-core-anglerange-fromdirectiondegreesclockwise"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fromDirectionDegreesClockwise.html -->


<div>
<h1>fromDirectionDegreesClockwise static method</h1></div>

<a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a>
fromDirectionDegreesClockwise(<ol class="parameter-list single-line"> <li>double center, </li>
<li>double extent</li>
</ol>)

      

    

<p>Constructs an AngleRange from the provided center angle defining the
direction and an angular width to extent the range by 50% clockwise and
50% counter-clockwise from its center angle.</p>
<p>Corrects values if they exceed the ranges.
Example: direction = 90, extent = 10 means the circle sector is pointing
east, with an extent of 5 degrees north-wards and 5 degrees south-wards.</p>
<ul>
<li>
<p><code>center</code> Start angle, running clockwise, in degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</li>
<li>
<p><code>extent</code> The range's extent, running clockwise, in degrees from start.
The value will be clamped to the range of [0, 360] degrees.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-anglerange-class">AngleRange</a>. Created AngleRange from the provided center angle and the range's extent.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static AngleRange fromDirectionDegreesClockwise(double center, double extent) =&gt; $prototype.fromDirectionDegreesClockwise(center, extent);</code></pre>

 



</div>
`
}</HTMLBlock>
