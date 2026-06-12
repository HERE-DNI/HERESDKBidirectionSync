---
title: "DashPattern.uniform constructor"
slug: "sdk-for-flutter-navigate-mapview-dashpattern-dashpattern-uniform"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DashPattern.uniform.html -->


<div>
<h1>DashPattern.uniform constructor</h1></div>

DashPattern.uniform(<ol class="parameter-list single-line"> <li>double dashLength</li>
</ol>)
    

<p>Creates a uniform dash pattern in which the length of a gap is the same
as the length of a dash.</p>
<p>This allows for patterns like <code>' — — — —'</code> or <code>'   ———   ———   ———'</code>.</p>
<ul>
<li><code>dashLength</code> The length of a dash in pixels. The gap will have the same length.
Clamped to the range of [1, 500].</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DashPattern.uniform(double dashLength) =&gt; $prototype.uniform(dashLength);</code></pre>

 



</div>
`
}</HTMLBlock>
