---
title: "fromMinMaxDegreesClockwise static method"
slug: "sdk-for-flutter-navigate-core-anglerange-fromminmaxdegreesclockwise"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- fromMinMaxDegreesClockwise.html -->


<div>
<h1>fromMinMaxDegreesClockwise static method</h1></div>

<a href="sdk-for-flutter-navigate-core-anglerange-class">AngleRange</a>
fromMinMaxDegreesClockwise(<ol class="parameter-list single-line"> <li>double min, </li>
<li>double max</li>
</ol>)

      

    

<p>Constructs an AngleRange from the provided minimum and maximum angles.</p>
<p>Corrects values if they exceed the ranges. The angles are always
interpreted in clockwise orientation.</p>
<ul>
<li>
<p><code>min</code> Angle where to start the circular sector, running clockwise, in
degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</li>
<li>
<p><code>max</code> Angle where the circular sector ends, running clockwise, in
degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-anglerange-class">AngleRange</a>. Created AngleRange from the provided minimum and maximum angles.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static AngleRange fromMinMaxDegreesClockwise(double min, double max) =&gt; $prototype.fromMinMaxDegreesClockwise(min, max);</code></pre>

 



</div>
`
}</HTMLBlock>
