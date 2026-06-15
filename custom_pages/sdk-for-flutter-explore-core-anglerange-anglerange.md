---
title: "AngleRange constructor"
slug: "sdk-for-flutter-explore-core-anglerange-anglerange"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AngleRange.html -->


<div>
<h1>AngleRange constructor</h1></div>

AngleRange(<ol class="parameter-list single-line"> <li>double start, </li>
<li>double extent</li>
</ol>)
    

<p>Constructs an AngleRange from the provided start and extent angles.</p>
<p>Corrects values if they exceed the ranges.</p>
<ul>
<li>
<p><code>start</code> Start angle, running clockwise, in degrees from north.
The value will be normalized to [0.0, 360.0).</p>
</li>
<li>
<p><code>extent</code> The range's extent, running clockwise, in degrees from start.
The value will be clamped to the range of [0, 360] degrees.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory AngleRange(double start, double extent) =&gt; $prototype.$init(start, extent);</code></pre>

 



</div>
`
}</HTMLBlock>
